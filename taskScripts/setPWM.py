import Jetson.GPIO as GPIO
import time 

output_pin = 33
GPIO.setmode(GPIO.BOARD)

GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
prev_state = GPIO.LOW
print("running")

try:
    while True:
        if(prev_state == GPIO.LOW):
            GPIO.output(output_pin, GPIO.HIGH)
            prev_state = GPIO.HIGH
        elif(prev_state == GPIO.HIGH):
            GPIO.output(output_pin, GPIO.LOW)
            prev_state = GPIO.LOW
        print(GPIO.input(output_pin))
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

