import threading

def send_mesg(data):
    """
    发送数据
    :param data:
    """
    print("--------数据发送开始--------")
    data.append("1")
    data.append("2")
    data.append("3")
    print("--------data= %s 发送完成--------" % data)


def recv_mesg(data):
    """
    接收数据
    :param data:
    """
    print("--------数据接收开始--------")
    for temp in data:
        print(temp)
    print("--------数据接收完成--------")


def main():
    data = list()
    send_thread = threading.Thread(target=send_mesg,args=(data,))
    recv_thread = threading.Thread(target=recv_mesg,args=(data,))
    send_thread.start()
    recv_thread.start()


if __name__ == "__main__":
    main()