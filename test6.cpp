#include <iostream>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <serial.h>
#include <unistd.h>

int main() {
    // Define the serial port (change this to the appropriate serial port)
    if ((serial::serial::serial)) {
        std::cerr << "Unable to open serial port." << std::endl;
        return -1;
    }
    std::cout << serialPort << std::endl;

    // Define the channel to which your motor is connected
    int channel = 0;  // Adjust this to your motor's channel

    // Set the target PWM value (range: 4000 to 8000 for typical servos)
    int targetPWM = 4 * 1700;  // Adjust this as needed

    // Calculate the target PWM as a 4-byte value
    unsigned char targetPWMBytes[2];
    targetPWMBytes[0] = (targetPWM & 0x7F);
    targetPWMBytes[1] = ((targetPWM >> 7) & 0x7F);

    // Command to set the target PWM value
    unsigned char setPWMCmd[] = {0x84, static_cast<unsigned char>(channel)};
    setPWMCmd[2] = targetPWMBytes[0];
    setPWMCmd[3] = targetPWMBytes[1];

    try {
        // Send the command to set the target PWM value
        for (int i = 0; i < sizeof(setPWMCmd); ++i) {
            serialPutchar(serialPort, setPWMCmd[i]);
        }
        
        // Run the motor for 5 seconds
        sleep(2);

    } catch (...) {
        std::cerr << "Error sending PWM command." << std::endl;
    }
    // Stop the motor by setting the target PWM to the neutral position
    int neutralPWM = 4 * 1490;  // Adjust this if needed
    unsigned char neutralPWMBytes[2];
    neutralPWMBytes[0] = (neutralPWM & 0x7F);
    neutralPWMBytes[1] = ((neutralPWM >> 7) & 0x7F);

    unsigned char setNeutralCmd[] = {0x84, static_cast<unsigned char>(channel)};
    setNeutralCmd[2] = neutralPWMBytes[0];
    setNeutralCmd[3] = neutralPWMBytes[1];

    for (int i = 0; i < sizeof(setNeutralCmd); ++i) {
        serialPutchar(serialPort, setNeutralCmd[i]);
    }

    // Close the serial port when done
    serialClose(serialPort);

    return 0;
    
}
