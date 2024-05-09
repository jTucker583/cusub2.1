import rclpy
from rclpy.node import Node 

from sensor_msgs.msg import Joy
from cusub2_teleop.motorController import motorController

class gripper(Node):

    def __init__(self):
        super.__init__('gripper')
        self.mc = motorController() 
        self.prevState = 0
        self.subscription = self.create_subscription(
            Joy, # msg type
            '/joy', # topic to listen to
            self.listener_callback, #callback fxn
            10 # overflow queue
        )

    def listener_callback(self ,msg):
        #button 0 axes 3
        rotateChannel = 1 #random IDK the channels
        gripChannel = 2 #random IDK the channels
        if(msg.axes[3] != 0):
            self.mc.run(rotateChannel, msg.axes[3], grip=True)

        if(msg.buttons[0] != self.prevState):
            if(msg.buttons[0] == 0):
                self.mc.run(gripChannel, -1, grip=True)
            else:
                self.mc.run(gripChannel, 1, grip=True)

            self.prevState = msg.buttons[0]
        




        
def main(args=None):
    rclpy.init(args=args)

    grip = gripper()

    rclpy.spin(grip)
    grip.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
