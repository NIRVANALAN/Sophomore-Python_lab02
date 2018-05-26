'''
2 实现一个队列Queue类，数据从前端被移除，从后端被加入。要求实现以下功能并通过程序验证：
(1) 	enqueue() 在队列的尾部加入一个新的数据
(2) 	dequeue() 在队列的头部取出一个数据，返回它并且把它从队列中删除 
(3) 	putfile() 将队列中数据写入文件中 
(4) 	getfile() 将文件中数据加入队列中
(5) 	printAll() 显示当前队列内所有元素，如果是空队列给出提示。

'''


class Queue:
    def __init__(self, *args, **kwargs):
        self.__queue_list = []

    def enqueue(self, x):
        self.__queue_list.append(str(x))

    def dequeue(self):
        self.__queue_list.reverse()
        t = self.__queue_list.pop()
        self.__queue_list.reverse()
        return t

    def putfile(self):
        with open('ex02.txt', 'w+') as f:
            for i in range(len(self.__queue_list)):
                f.write(self.__queue_list[i]+'\n')

    def getfile(self):
        with open('ex02.txt') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            self.__queue_list.append(lines[i].split('\n')[0])

    def printAll(self):
        if len(self.__queue_list) is 0:
            print("The stack is already empty")
        else:
            for i in range(len(self.__queue_list)):
                print(self.__queue_list[i], end=' ')
            print()


if __name__ == '__main__':
    q = Queue()
    print("call enqueue() to push 1 and 2 into Queue")
    q.enqueue(1)
    q.enqueue(2)
    print("call printAll()")
    q.printAll()
    print('call putfile()')
    q.putfile()
    print('call getfile()')
    q.getfile()
    print('call printAll()')
    q.printAll()
    print("call dequeue() to pop from Queue")
    print('retrun from dequeue():', q.dequeue())
    print("call printAll")
    q.printAll()

    '''
call enqueue() to push 1 and 2 into Queue
call printAll()
1 2 
call putfile()
call getfile()
call printAll()
1 2 1 2 
call dequeue() to pop from Queue
retrun from dequeue(): 1
call printAll
2 1 2 
    '''
