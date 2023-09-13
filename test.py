import serial

# Open a serial connection to the Mini Maestro.
ser = serial.Serial('/dev/ttyACM0', baudrate=115200)  # Adjust the port as needed.

# Define the servo channel you want to control (0-23).
servo_channel = 0

# Define the target position (usually in microseconds).
target_position = 1500  # Adjust this value according to your servo's range.

# Command to set the target position of a servo channel.
command = bytearray([0x84, servo_channel, target_position & 0x7F, (target_position >> 7) & 0x7F])

# Send the command to the Mini Maestro.
ser.write(command)

# Close the serial connection when done.
ser.close()
