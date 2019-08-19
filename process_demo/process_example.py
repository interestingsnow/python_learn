import multiprocessing

def send_msg(data):
    print("----data = %s-------" % data)

#因为在两个完全不同的进程中，所以引用的传递是不起作用的，所以我们需要将数据放在队列中
#两个进程操作同一个数据队列
def recv_msg(data):
    print("----data = %s-------" % data)
    while True:
        print(data.get())
        if data.empty():
            print("---队列为空")


def ref_data(data):
    print("-----列表数据------")
    send_process = multiprocessing.Process(target=send_msg, args=(data,))
    recv_process = multiprocessing.Process(target=recv_msg, args=(data,))
    send_process.start()
    recv_process.start()

def queue_data(data):
    print("-----队列数据------")
    send_process = multiprocessing.Process(target=send_msg, args=(data,))
    recv_process = multiprocessing.Process(target=recv_msg, args=(data,))
    send_process.start()
    recv_process.start()

def main():
    # # 第一种：数据放在列表中
    # data_ref = list()
    # data_ref.append("1")
    # data_ref.append("2")
    # data_ref.append("3")
    # ref_data(data_ref)
    # 第二种
    data_queue = multiprocessing.Queue()
    data_queue.put("1")
    data_queue.put("2")
    data_queue.put("3")
    queue_data(data_queue)

if __name__ == "__main__":
    main()