# [5]
# 1   2   3   4   5


# 程序员的核心

# (变量) MyLIst  a   b    Node2   c  ... d  Node3
#（地址）0       1   2    3       ....         n
#（值） <3>{}    1   1   <n>{}

# 操作系统 管理分配，地址，变量
# 人（桂崇皓）变量



# (变量) Node   AddNode GetCnt GetItemValue node next  val AddNode GetCnt node2 next val AddNode
#（地址）0      1-10     11-20  21-30        31    32   33  1      11     34    35   36   1
#（值）  self            

class Node(object):
    def __init__(self, val):
        self.next = -1
        self.val = val

    def AddNode(self, val):
        head = self
        ori_head = head
        if head == None:
            return Node(val)
        node = Node(val)
        while(head.next != -1):
            head = head.next
        head.next = node
        return ori_head

    def GetCnt(self):
        head = self
        cnt = 0 if head == None else 1
        while(head.next != -1):
            head = head.next
            cnt += 1
        return cnt

    def GetItemValue(self, i):
        head = self
        while(i > 0):
            head = head.next
            i -= 1
        return head.val

    
head =Node('up')
head = head.AddNode('down')
head = head.AddNode('left')
head = head.AddNode('right')
print(head.GetCnt())
print(head.GetItemValue(2))