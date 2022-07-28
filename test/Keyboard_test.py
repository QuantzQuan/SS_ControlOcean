import keyboard  # 监听键盘


def test_a():
    print('aaa')


def test():
    print('bbb')


if __name__ == '__main__':
    keyboard.add_hotkey('up', test_a)
    keyboard.add_hotkey('down', test)
    keyboard.wait()
