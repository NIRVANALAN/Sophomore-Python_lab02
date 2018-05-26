'''
 实现一个集合Set类，集合是不允许有相同元素存在的数据结构，要求实现以下功能:
(1) 	Set( aList ): 利用初始化数据（aList是一个数据列表）创建一个集合
(2) 	addElement( x ): 将x加入到集合中
(3) 	deleteElement( x): 将x从集合中删除。如果没有x，则集合保持不变
(4) 	isMember(x): 判断x是否属于集合，返回True或False
(5) 	intersection( Set2): 返回当前集合与集合Set2的交集
(6) 	union(Set2): 返回当前集合与集合Set2的并集
(7) 	substract(Set2):返回当前集合与集合Set2的差集（属于当前集合但不属于Set2的元素）
(8) 	printAll() 显示当前集合内所有元素，如果是空集给出提示


'''


class Set:
    def __init__(self, a, **kwargs):  # constructor
        # self.__set_list={}
        self.__set_list = set(a)

    def addElement(self, x):
        self.__set_list.add(x)

    def isMember(self, x):
        l = []
        l.append(x)
        t_set = set(l)
        # revoke set.issubset() to judge if x is in __set_list
        if t_set.issubset(self.__set_list):
            return True

    def deleteElement(self, x):
        if self.isMember(x):
            self.__set_list.remove(x)
        else:
            print(x, 'not in set')

    def union(self, s):
        if type(s) is set:
            return self.__set_list.union(s)
        else:
            print('arg type error, should be set')

    def substract(self, s):
        if type(s) is set:
            t_set = self.__set_list.intersection(s)
            if t_set is not None:
                s = self.__set_list.copy()
                for i in range(len(t_set)):
                    s.remove(t_set.pop())
                return s
            else:
                return None

    def intersection(self, s):
        if type(s) is set:
            t_set = self.__set_list.intersection(s)
            return t_set

    def printAll(self):
        if len(self.__set_list) is 0:
            print("The set is already empty")
        else:
            s = self.__set_list.copy()
            for i in range(len(self.__set_list)):
                print(s.pop(), end=' ')
            print()


if __name__ == '__main__':
    print('initial data list is l=[1,2,3,4,5,6,7,8,9]')
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = Set(l)
    print('call addElement() to add 10 and 12')
    s.addElement(10)
    s.addElement(12)
    print('call printAll()')
    s.printAll()
    print('call deleteElement() to delete 5')
    s.deleteElement(5)
    print('call printAll()')
    s.printAll()
    print('call deleteElement() to delete 20 which is not in set')
    print('return value:', end=' ')
    s.deleteElement(20)
    print('call printall()')
    s.printAll()
    print('create another set which has initial value {10,11,12,13,14,15}')
    t_set = {10, 11, 12, 13, 14, 15}  # new set
    print('call intersection()')
    print('intersection return value:', s.intersection(t_set))
    print('call union')
    print('union return value:', s.union(t_set))
    print('call substract')
    print('substract return value:', s.substract(t_set))
    print("Over")
