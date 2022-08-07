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
    ser = serial.Serial("/dev/ttyUSB1", 115200, timeout=0.5)
    # # under raspy
    # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)

    # init to close serial
    if ser.isOpen():
        ser.close()

    # prepare socket
    hostname = "192.168.50.137"  # sending device's IP
    # hostname = "172.24.143.124" # sending device's IP zerotier
    port = 1212
    Raspi_Zero = Client()
    while CONNECT_FLAG != 0:
        try:
            CONNECT_FLAG = Raspi_Zero.client.connect_ex((hostname, port))
        except:
            pass

    while True:
        ser.open()
        cur_string = Raspi_Zero.client.recv(1024)
        print(cur_string)
        ser.write(cur_string + b'\n')
        ser.flushOutput()
        ser.close()
        time.sleep(0.1)
        if KeyboardInterrupt:
            Raspi_Zero.close()
