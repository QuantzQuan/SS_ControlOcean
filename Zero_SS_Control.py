import socket
import time
import serial

class Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        self.client.close()


if __name__ == "__main__":
    # under windows system
    ser = serial.Serial("com1", 115200, timeout=0.5)
    # # under raspy
    # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)

    # open com
    if ser.isOpen():
        ser.close()
    ser.open()

    # prepare socket
    hostname = "192.168.76.27"    # sending device's IP
    # hostname = "172.24.143.124" # sending device's IP zerotier
    port = 1212

    while True:
        client = Client()
        try:
            client.client.connect_ex((hostname, port))
            cur_string = client.client.recv(1024)
            print(client.client.recv(1024).decode())
            ser.write(cur_string+b'\n')
            client.close()
        except:
            time.sleep(1)
