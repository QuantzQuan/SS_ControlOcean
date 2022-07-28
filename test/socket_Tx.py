import socket
import time


class Server():
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)

    def server_close(self):
        self.server.close()


if __name__ == "__main__":
    host = socket.gethostname()
    port = 1212
    server = Server(host, port)
    while True:
        try:
            connection, addr = server.server.accept()
            print(addr, ' connected!')
            connection.send('$BUMP00'.encode('utf-8'))
            time.sleep(5)
            connection.close()
        except ConnectionResetError as e:
            print('close thread already use port')
            break
    server.server_close()
