class SingleNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Linked:
    def __init__(self,node=None):
        self.__head = node
    
    def is_empty(self):
        """判断链表是否为空"""
        #只要判断头节点是否为空就行
        return self.__head is None

    def length(self):
        """判断链表的长度"""
        #初始化游标
        cur = self.__head
        #长度计算变量
        count = 0
        # 判断游标指向是否为空
        while cur is not None:
            #指向下一个结点，同时计数器加一
            cur = cur.next
            count += 1
        return count
    
    def append(self,val):
        """尾部添加元素
        :param val
        """
        # 新建结点
        newNode = SingleNode(val)
        # 判断是否为空链表
        if self.is_empty():
            #如果是空链表就将头指针指向新节点
            self.__head = newNode #左指向右，实例传递的是地址
        else:
            #初始化游标
            cur = self.__head
            #将游标移动到末尾
            while cur.next is not None:
                cur = cur.next
            #将末尾元素的next设置为新结点
            cur.next = newNode
    
    def add_head(self,val):
        """头部添加元素
        :param val
        """
        #新建结点
        newNode = SingleNode(val)
        #将原头结点坐标给新结点，新结点坐标给头结点
        newNode.next,self.__head = self.__head,newNode

    def travel(self):
        """遍历整个链表"""
        #初始化游标
        cur = self.__head
        #输出每个结点的val
        while cur is not None:
            print(cur.val,end = ' ')
            cur = cur.next #游标指向下一个结点
        print(' ')
    
    def insert(self,pos,val):
        """指定位置添加元素
        :param pos:指定位置
        :param val:元素
        """
        #判断插入的位置
        if pos <= 0:
            self.add(val)
        elif pos > (self.length() - 1):
            self.append(val)
        else:
            #新建结点
            newNode = SingleNode(val)
            #初始化游标
            cur = self.__head
            #创建计数器
            count = 0
            #游标定位到指定位置前一个结点
            while count<(pos-1):
                count += 1
                cur = cur.next
            #游标位置后面一大串的首个结点地址给newNode，newNode位置给游标
            newNode.next, cur.next = cur.next,newNode
    
    def position(self,pos):
        """根据位置读取元素"""
        if pos == 0:
            return self.__head.val
        elif 0 < pos <= (self.length()-1):
            #初始化游标
            cur = self.__head
            #创建计数器
            count = 0
            #将游标移动到指定位置
            while count < pos:
                count += 1
                cur = cur.next
            return cur.val
        else:
            return False
    
    def element(self,val):
        """输出元素所在位置"""
        #初始化游标与计数器
        cur = self.__head
        count = 0
        pos_list = []
        while True:
            #判断游标指向元素是否为输入元素
            if cur.val == val:
                pos_list.append(count)
            #判断测试的长度是否已经超出
            elif cur.next is None:
                return [pos_list,False][pos_list is not None]
            cur = cur.next
            count += 1
    
    def delete(self,pos):
        """根据位置删除
        :param pos:位置
        """
        #初始化游标和副游标
        cur = self.__head
        pre = None
        #判断输入是否在链表中
        if 0 <= pos <= (self.length() - 1):
            if pos == 0:
                self.__head = self.__head.next
            else:
                count = 0
                while count < pos:
                    count += 1
                    pre,cur = cur,cur.next
                pre.next = cur.next
    
    def clear(self):
        """清空链表"""
        self.__head = None

