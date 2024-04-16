'''
4.7 stack
 : 입력 순서대로 쌓은 다음 나중에 들어온 것 부터 사용하는 구조 LIFO 
'''

def Stack() :
    stack = []
    for i in range(1, 6) :
        stack.append(i)
    print(stack)

    while stack :
        print("Stack POP Value is : ", stack.pop() )

'''
4.8 Queue
 : 입력 순서대로 쌓은 다음 먼저 들어온것 부터 사용하는 구조 FIFO
 , 배열 또는 연결리스트 이용
'''

def Queue() :
    queue = []
    for i in range(1, 6) :
        queue.append(i)
    print(queue)

    while queue :
        print("Queue POP value is : ", queue.pop(0))


Stack()
Queue()

