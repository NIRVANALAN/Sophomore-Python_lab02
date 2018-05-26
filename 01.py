'''
1实现一个堆栈Stack类，堆栈(Stack)是一种具有后进先出(last-in-first-out，LIFO)特性的数据结构。要求实现以下功能并通过程序验证：
(1) 	pushstack()  向堆栈中压入一个数据项
(2) 	popstack() 从堆栈中移出一个数据项
(3) 	isempty() 如果堆栈是空的，返回布尔值True,否则返回False
(4) 	peekstack() 取出堆栈顶部的数据项，但并不移除它
(5) 	printAll() 打印当前栈内所有元素，如果是空栈给出提示

'''


class Stack:
    def __init__(self, *args, **kwargs):
        self.__stack_list = []

    def pushstack(self, x):
        self.__stack_list.append(x)

    def popstack(self):
        return self.__stack_list.pop()

    def isempty(self):
        return len(self.__stack_list) is 0

    def peekstack(self):
        if len(self.__stack_list) is 0:
            pass
        l1 = self.__stack_list.copy()
        return l1.pop()

    def printAll(self):
        if self.isempty():
            print("The stack is already empty")
        else:
            for i in range(len(self.__stack_list)):
                print(self.__stack_list[i], ' ')

    def __del__(self):
        print("The destuctor is called")


if __name__ == '__main__':
    s = Stack()  # create a instance of stack()
    print("add 'a' to stack s")
    s.pushstack('a')  # add a to stack s
    print("call printAll()")
    s.printAll()
    print("call 'isempty()' :", s.isempty())
    print("add 'b' to stack s")
    s.pushstack('b')  # add b to stack s
    print("call printAll()")
    s.printAll()
    print('call "peekstack()"')
    print(s.peekstack())
    print("call printAll()")
    s.printAll()
    print('call popstack()')
    print(s.popstack())
    print("call printAll()")
    s.printAll()
    print('call popstack()')
    print(s.popstack())
    print("call isempty()", s.isempty())
    print('call printAll()')
    s.printAll()  # printall elements in s
'''
output:
add 'a' to stack s
call printAll()
a  
call 'isempty()' : False
add 'b' to stack s
call printAll()
a  
b  
call "peekstack()"
b
call printAll()
a  
b  
call popstack()
b
call printAll()
a  
call popstack()
a
call isempty() True
call printAll()
The stack is already empty
The destuctor is called
'''
