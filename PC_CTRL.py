import socket
import time
import keyboard

MOTOR_CONTROL_TIME = 0.5
BUMP_FULL_TIME = 2
LIGHT_STATE = 0
SERVO_CRUL_TIME = 5


class Server:
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)

    def server_close(self):
        self.server.close()



def socket_transport(cur_string=None, wait_time=None):
    host = socket.gethostname()
    port = 1212
    server = Server(host, port)
    try:
        connection, addr = server.server.accept()
        print(cur_string.encode('utf-8'))
        connection.send(cur_string.encode('utf-8'))
        time.sleep(wait_time)
        print("Send!")
        connection.close()
    except ConnectionResetError as error:
        pass
    server.server_close()


def motor_forward():
    cur_string = "$CTRL11"
    wait_time = MOTOR_CONTROL_TIME
    socket_transport(cur_string, wait_time)


def motor_backward():
    cur_string = "$CTRL00"
    wait_time = MOTOR_CONTROL_TIME
    socket_transport(cur_string, wait_time)


def motor_left():
    cur_string = "$CTRL10"
    wait_time = MOTOR_CONTROL_TIME
    socket_transport(cur_string, wait_time)


def motor_right():
    cur_string = "$CTRL01"
    wait_time = MOTOR_CONTROL_TIME
    socket_transport(cur_string, wait_time)


def bump_1():
    cur_string = "$BUMP00"
    wait_time = BUMP_FULL_TIME
    socket_transport(cur_string, wait_time)


def bump_2():
    cur_string = "$BUMP01"
    wait_time = BUMP_FULL_TIME
    socket_transport(cur_string, wait_time)


def bump_3():
    cur_string = "$BUMP10"
    wait_time = BUMP_FULL_TIME
    socket_transport(cur_string, wait_time)


def bump_4():
    cur_string = "$BUMP11"
    wait_time = BUMP_FULL_TIME
    socket_transport(cur_string, wait_time)


def servo_forward():
    cur_string = "$CRUL15"
    wait_time = SERVO_CRUL_TIME
    socket_transport(cur_string, wait_time)


def servo_backward():
    cur_string = "$CRUL05"
    wait_time = SERVO_CRUL_TIME
    socket_transport(cur_string, wait_time)


def light_on():
    cur_string = "$LIGH11"
    wait_time = 0
    socket_transport(cur_string, wait_time)


def light_off():
    cur_string = "$LIGH00"
    wait_time = 0
    socket_transport(cur_string, wait_time)


if __name__ == '__main__':
    keyboard.add_hotkey('up', motor_forward)
    keyboard.add_hotkey('down', motor_backward)
    keyboard.add_hotkey('left', motor_left)
    keyboard.add_hotkey('right', motor_right)
    keyboard.add_hotkey('1', bump_1)
    keyboard.add_hotkey('2', bump_2)
    keyboard.add_hotkey('3', bump_3)
    keyboard.add_hotkey('4', bump_4)
    keyboard.add_hotkey('o', servo_forward)
    keyboard.add_hotkey('p', servo_backward)
    keyboard.add_hotkey('k', light_on)
    keyboard.add_hotkey('l', light_off)
    keyboard.wait()
