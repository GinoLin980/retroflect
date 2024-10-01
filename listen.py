import socket

def listen_for_udp_data(ip, port, timeout=5):
    # Create a UDP socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the specified IP and port
    sock.bind((ip, port))
    
    # Set a timeout for the socket
    sock.settimeout(timeout)
    
    print(f"Listening for UDP data on {ip}:{port}")
    
    try:
        # Receive data
        data, addr = sock.recvfrom(1024)
        print(f"Received data from {addr}")
        print(f"Data: {data.decode()}")
        return True
    except socket.timeout:
        print("No data received within the timeout period")
        return False
    finally:
        # Close the socket
        sock.close()

# Example usage
ip_to_listen = "127.0.0.1"  # localhost
port_to_listen = 8000

data_received = listen_for_udp_data(ip_to_listen, port_to_listen)
if data_received:
    print("Data was received successfully")
else:
    print("No data was received")