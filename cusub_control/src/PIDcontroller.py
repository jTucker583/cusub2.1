# where PID controller will live
# want to take in sensor data and 
# probbaly just need position control (P)
import math

# code from https://brickexperimentchannel.wordpress.com/2022/07/13/rc-submarine-4-0-pid-control-9-10/
error = targetDepth - depthFiltered
integral += error * timeDelta
if math.isnan(prevError) or buttonDive.value == 1 or buttonSurface.value == 1:
    prevError = error
derivative = (error - prevError) / timeDelta
derivative = 0.05 * derivative + 0.95 * prevDerivative
PIDoutput = KP * error + KI * integral + KD * derivative
prevError = error
prevDerivative = derivative



## essentially just want to scale our response depending on how far we are
# so Kp*(desired - actual), where Kp scales our response