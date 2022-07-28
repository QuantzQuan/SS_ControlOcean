import pynput.keyboard as pk


def on_press(key):
    # 监听按键
    cur_key = str(key)[1]
    print("按键为", cur_key)
    # s.send(key.encode())


# 连接事件以及释放
with pk.Listener(on_press=on_press) as pklistener:
    pklistener.join()
