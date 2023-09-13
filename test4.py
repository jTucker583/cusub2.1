import serial
import time

# Define the serial port (change this to the appropriate serial port)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Define the channel to which your motor is connected
channel = 0  # Adjust this to your motor's channel

# Set the target PWM value (range: 4000 to 8000 for typical servos)
target_pwm = 1900  # Adjust this as needed

# Calculate the target PWM as a 4-byte value
target_pwm_bytes = [(target_pwm & 0x7F), ((target_pwm >> 7) & 0x7F)]

# Command to set the target PWM value
set_pwm_cmd = [0x84, channel] + target_pwm_bytes

try:
    # Send the command to set the target PWM value
    ser.write(bytearray(set_pwm_cmd))    
    # Run the motor for 5 seconds
    time.sleep(5)
    target_pwm = 1500  # Adjust this as needed

# Calculate the target PWM as a 4-byte value
    target_pwm_bytes = [(target_pwm & 0x7F), ((target_pwm >> 7) & 0x7F)]

# Command to set the target PWM value
    set_pwm_cmd = [0x84, channel] + target_pwm_bytes
    ser.write(bytearray(set_pwm_cmd))

finally:
    # Stop the motor by setting the target PWM to the neutral position
    neutral_pwm = 1490  # Adjust this if needed
    neutral_pwm_bytes = [(neutral_pwm & 0x7F), ((neutral_pwm >> 7) & 0x7F)]
    set_neutral_cmd = [0x84, channel] + neutral_pwm_bytes
    ser.write(bytearray(set_neutral_cmd))

    # Close the serial port when done
    ser.close()

