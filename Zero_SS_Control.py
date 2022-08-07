import socket
import time
import serial

CONNECT_FLAG = 1


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        self.client.close()


if __name__ == "__main__":
    # under windows system
    ser = serial.Serial("com1", 115200, timeout=0.5)
    # # under raspy
    # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)

    # init to close serial
    if ser.isOpen():
        ser.close()

    # prepare socket
    hostname = "192.168.43.116"  # sending device's IP
    # hostname = "172.24.143.124" # sending device's IP zerotier
    port = 1212
    Raspi_Zero = Client()
    ser.open()

    while True:
        Raspi_Zero.client.connect_ex((hostname, port))
        cur_string = Raspi_Zero.client.recv(1024)
        print(cur_string)
        ser.write(cur_string + b'\n')
        ser.flushOutput()
        time.sleep(0.1)

