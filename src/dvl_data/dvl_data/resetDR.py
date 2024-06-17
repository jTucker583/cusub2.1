import socket
import json

# Define the IP address and port
ip = "192.168.194.95"
port = 16171

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((ip, port))
    
    # Create the command as a JSON string
    command = json.dumps({"command": "reset_dead_reckoning"})
    
    # Send the command to the server
    client_socket.sendall(command.encode('utf-8'))
    
    # Optionally, receive a response from the server
    response = client_socket.recv(1024)
    print("Received response:", response.decode('utf-8'))

finally:
    # Close the socket
    client_socket.close()

