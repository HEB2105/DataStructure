'''
4.4.3 singly linked list
: 값이 순서대로 연결되지 않아도 됨
 , 삭제 할 때 반드시 뒤에 있던 노드들을 연결해줘야함
 , 추가 할땐 맨 앞 노드의 앞에 추가  
'''

class Node :
    # 연결리스트를 구성하는 data
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

def init() :
    global node1
    # make 연결리스트, 연결포인터 구성
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

def delete(del_data) :
    global node1
    # 구성된 리스트에서 데이터를 지우고 나머지 데이터를 연결
    pre_node = node1
    next_node = pre_node.next

    if pre_node.data == del_data :
        # del_data가 첫번째 데이터일 떼  이를 지우고 함수 종료
        node1 = next_node
        del pre_node
        return
    
    while next_node :
        # next_node 가 존재하면 계속 반복
        if next_node.data == del_data :
            # next_node 값이 지울 대상이면, pre_node 에 다음값을 할당해주고 지움
            pre_node.next = next_node.next
            del next_node
            break
        # 지울 대상이 아닌경우 pre_node와 next_node를 한칸씩 이동
        pre_node = next_node
        next_node = next_node.next
    
def insert(ins_data) :
    # 리스트에 새로운 데이터 추가 
    global node1
    new_node = Node(ins_data)
    new_node.next = node1
    node1 = new_node

def print_list() :
    # 연결 리스트의 데이터 출력
    global node1
    node = node1
    while node :
        # node에 값이 있으면 반복
        print(node.data)
        node = node.next
    print() # 종료

def LinkedList() :
    init() 
    delete(2)
    insert("9")
    print_list()

LinkedList()
        