from queue import Queue

import socket
import threading

target = '192.168.1.1'
queue = Queue()
open_ports = []

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

# for port in range(1,100):
   # if portscan(port):
  #      print("PORT {} OPEN".format(port))
 #   else:
#        print("PORT {} CLOSED".format(port))

def fill_queue(port_list):
    for i in port_list:
        queue.put(i)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print('Port {} is open'.format(port))
            open_ports.append(port)


port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
 thread.start()
for thread in thread_list:
    thread.join()



print("Open ports are:",open_ports )
