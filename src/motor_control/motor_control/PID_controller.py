#PID Loop: only uses P and D term. I think integral term is not needed because, unlike cars and stuff, stopping the motors will cause
# the sub to glide and not instantly stop which should reduce the problem of the sub getting infinitely close to the goal. I think it works but it is untested
# and could have dumb errors. Kp and Kd values will need to be tuned.
import rclpy
from rclpy.node import Node
import time
from geometry_msgs.msg import Twist, Pose
from std_msgs.msg import Bool
import yaml
import math

KP = 0
KD = 0

with open('src/cfg/sub_properties.yaml') as f:
    file = yaml.safe_load(f)
    KP = file['kp']
    KD = file['kd']

class PIDController(Node):

    def __init__(self):
        super().__init__('pid_controller')
        self.goalpose_sub = self.create_subscription(Pose, 'goal_pose', self.goal_pose_callback, 10)
        self.currentpose_sub = self.create_subscription(Pose, 'pose', self.current_pose_callback, 10)
        self.auto_sub = self.create_subscription(Bool, 'autonamous_status', self.autonamous_status_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, 'sys_cmd_vel', 10)
        
        self.goal = Pose()
        self.currentPosition = Pose()
        self.deadzone = 0.1
        self.prev_time = time.time()
        self.prev_dim_diff = [0.0, 0.0, 0.0]
        self.prev_orient_diff = [0.0, 0.0, 0.0]
        self.auto_status = False

        self.timer = self.create_timer(0.1, self.pid_loop)

    def goal_pose_callback(self, msg):
        self.goal = msg

    def current_pose_callback(self, msg):
        self.currentPosition = msg
        
    def autonamous_status_callback(self, msg):
        self.auto_status = msg.data
        
    def quaternion_multiply(self, q1, q0):
        # Multiply two quaternions
        return [
            q1[3] * q0[0] + q1[0] * q0[3] + q1[1] * q0[2] - q1[2] * q0[1],
            q1[3] * q0[1] - q1[0] * q0[2] + q1[1] * q0[3] + q1[2] * q0[0],
            q1[3] * q0[2] + q1[0] * q0[1] - q1[1] * q0[0] + q1[2] * q0[3],
            q1[3] * q0[3] - q1[0] * q0[0] - q1[1] * q0[1] - q1[2] * q0[2]
        ]
    
    def quaternion_inverse(self, q):
        # Invert a quaternion
        return [-q[0], -q[1], -q[2], q[3]]

    def get_distance(self):
        return ((self.goal.position.x - self.currentPosition.position.x) ** 2 +
                (self.goal.position.y - self.currentPosition.position.y) ** 2 +
                (self.goal.position.z - self.currentPosition.position.z) ** 2) ** 0.5

    def get_orientation_error(self):
        # Calculate the orientation error using quaternions
        goal_quat = [
            self.goal.orientation.x,
            self.goal.orientation.y,
            self.goal.orientation.z,
            self.goal.orientation.w
        ]
        current_quat = [
            self.currentPosition.orientation.x,
            self.currentPosition.orientation.y,
            self.currentPosition.orientation.z,
            self.currentPosition.orientation.w
        ]
        # Calculate the relative rotation from current to goal
        relative_quat = self.quaternion_multiply(goal_quat, self.quaternion_inverse(current_quat))
        # Convert the relative quaternion to Euler angles (roll, pitch, yaw)
        roll_error, pitch_error, yaw_error = self.quaternion_to_euler(relative_quat)
        return [roll_error, pitch_error, yaw_error]

    def quaternion_to_euler(self, quat):
        # Convert quaternion to Euler angles
        x, y, z, w = quat
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw = math.atan2(t3, t4)

        return roll, pitch, yaw

    def pid_loop(self):
        current_time = time.time()
        time_delta = current_time - self.prev_time

        if time_delta == 0:
            return

        x_diff = self.goal.position.x - self.currentPosition.position.x
        y_diff = self.goal.position.y - self.currentPosition.position.y
        z_diff = self.goal.position.z - self.currentPosition.position.z

        orient_diff = self.get_orientation_error()

        # Position derivatives
        x_derivative = (x_diff - self.prev_dim_diff[0]) / time_delta
        y_derivative = (y_diff - self.prev_dim_diff[1]) / time_delta
        z_derivative = (z_diff - self.prev_dim_diff[2]) / time_delta

        # Orientation derivatives
        roll_derivative = (orient_diff[0] - self.prev_orient_diff[0]) / time_delta
        pitch_derivative = (orient_diff[1] - self.prev_orient_diff[1]) / time_delta
        yaw_derivative = (orient_diff[2] - self.prev_orient_diff[2]) / time_delta

        # PID outputs for position
        x_output = (KP * x_diff) + (KD * x_derivative)
        y_output = (KP * y_diff) + (KD * y_derivative)
        z_output = (KP * z_diff) + (KD * z_derivative)

        # PID outputs for orientation
        roll_output = (KP * orient_diff[0]) + (KD * roll_derivative)
        pitch_output = (KP * orient_diff[1]) + (KD * pitch_derivative)
        yaw_output = (KP * orient_diff[2]) + (KD * yaw_derivative)

        # Apply outputs to the Twist message
        # joyListener looks for sys_cmd_vel msgs that are non-zero and publishes them if there's no joystick input
        msg = Twist()
        if (self.auto_status):
            msg.linear.x = x_output
            msg.linear.y = y_output
            msg.angular.x = roll_output
            msg.angular.y = pitch_output
            msg.angular.z = yaw_output
        else:
            msg.linear.x = 0.0
            msg.linear.y = 0.0
            msg.angular.x = 0.0
            msg.angular.y = 0.0
            msg.angular.z = 0.0
        msg.linear.z = z_output

        # Publish the command
        self.cmd_pub.publish(msg)

        # Update previous differences and time
        self.prev_dim_diff = [x_diff, y_diff, z_diff]
        self.prev_orient_diff = orient_diff
        self.prev_time = current_time
        time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    pid_controller = PIDController()
    rclpy.spin(pid_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()