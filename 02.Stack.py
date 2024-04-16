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

Stack()

