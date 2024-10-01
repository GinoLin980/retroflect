import socket

def send_data(ip, port, message):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Using UDP
    
    # Send data to the specified IP and port
    sock.sendto(message.encode(), (ip, port))
    
    print(f"Sent message: '{message}' to {ip}:{port}")
    
    # Close the socket
    sock.close()

# Example usage
ip_to_send = '127.0.0.1'  # localhost
port_to_send = 8000
message_to_send = 'Hello, this is a test message!'

import time

while True:
    time.sleep(1)
    send_data(ip_to_send, port_to_send, message_to_send)