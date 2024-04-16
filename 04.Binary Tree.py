'''
4.11 binary tree
 : 모든 노드가 최대 2개의 자식노드를 가짐
  , 왼쪽 서브 트리의 값보다 오른쪽 서브 트리의 값이 더 큼
  - Full binary tree : 꽉 찬 트리
  - Complete binary tree : 마지막 전까진 모두 채워져있고, 마지막 레벨의 왼쪽에서 오른쪽으로
  - Skewed binary tree : 왼쪽 혹은 오른쪽 서브트리만 
'''

class Node(object) :
    # node 정의
    def __init__(self, data) :
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object) :
    def __init__(self) :
        self.root = None
    
    def insert(self, data) :
        # 데이터 삽입 후 root가 존재하면 True 반환, 만약  data와 root 모두 None 일경우 False 반환 
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data ) :
        if node is None :
            # node 값이 없으면 data를 노드형식으로 바꿔 node에 저장
            node = Node(data)
        else :
            if data <= node.data :
                # data 값이 node의 data 값보다 작거나 같을 경우, 왼쪽으로 이동 후 재귀함수 
                node.left = self._insert_value(node.left, data)
            else :
                # data 값이 node의 data 값보다 클 경우, 오른쪽으로 이동 후 재귀함수 
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key) :
        # self.root 에서 key 값이 있는지 확인 
        return self._find_value(self.root, key)

    def _find_value(self, root, key) :
        if root is None or root.data == key :
            # root 값이 존재하지 않으면 False, 찾으려는 대상이 key 값이 root 값과 동일하면 True 
            return root is not None
        elif key < root.data :
            # key 값이 현재 root 값보다 작으면 왼쪽으로 이동
            return self._find_value(root.left, key)
        else :
            # key 값이 현재 root 값보다 크면 오른쪽으로 이동
            return self._find_value(root.right, key)

    def delete(self, key) :
        # root 에서 key 값 제거 후 key 출력 (root 갱신) 
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node, key) :
        # 
        if node is None :
            # node(root) 값이 없을 경우 Node과 False 반환
            return node, False
        
        # deleted = False # deleted 값은 기본적으로 False 로 설정 (불필요한 코드 아닌가..?)
        if key == node.data :
            # key 값과 node값이 같은 경우
            deleted = True # 지우기 성공으로 바꾸고
            if node.left and node.right :
                # node 의 오른쪽과 왼쪽이 모두 있으면, 왼쪽값이 없을때까지 내려갔다 node의 왼쪽 값들과 parent를 연결
                parent, child = node, node.right
                while child.left is not None :
                    parent, child = child, child.left
                child.left = node.left
                if parent != node :
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right :
                # node 의 오른쪽 또는 왼쪽중 한개만 존재 할 경우, node 값을 지우고 아래 노드를 연결
                node = node.left or node.right
            else :
                # 노드가 마지막 이었을경우 그냥 삭제
                node = None
        elif key < node.data :
            # key 값이 node 값보다 작으면 왼쪽으로 이동
            node.left, deleted = self._delete_value(node.left, key)
        else :
            # key 값이 node의 값보다 클 경우 오른쪽으로 이동
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def DFTravel(self) :
        # 데이터 출력, 깊이 우선탐색 왼쪽의 부모부터
        def _DFTravel(root) :
            if root is None :
                # root 값이 없으면 패쓰 
                pass
            else :
                # root 값이 존재하면 root 값 출력
                print(root.data, end=' ')
                _DFTravel(root.left)
                _DFTravel(root.right)
        _DFTravel(self.root)

    def LFTravel(self) :
        # 데이터 출력, 깊이 우선 탐색 왼쪽의 뿌리부터
        def _LFTravel(root) :
            if root is None :
                pass
            else :
                _LFTravel(root.left)
                print(root.data, end=' ')
                _LFTravel(root.right)
        _LFTravel(self.root)
    
    def LRTravel(self) :
        # 데이터 출력, 깊이 우선 탐색 오른쪽의 뿌리부터
        def _LRTravel(root) :
            if root is None :
                pass
            else :
                _LRTravel(root.left)
                _LRTravel(root.right)
                print(root.data, end=' ')
        _LRTravel(self.root)
    
    def layerTravel(self) :
        # 데이터 출력, 넓이 우선 탐색 
        def _layerTravel(root) :
            queue = [root]
            while queue :
                # queue에 값이 있으면 계속 시행
                root = queue.pop(0)
                if root is not None :
                    print(root.data, end=' ')
                    if root.left :
                        # root 의 왼쪽 값이 존재할 경우 이 값을 queue에 업데이트 
                        queue.append(root.left)
                    if root.right :
                        # root 의 오른쪽 값이 존재할 경우 이 값을 queue에 업데이트 
                        queue.append(root.right)
        _layerTravel(self.root)


# data
data = [20, 6, 8, 12, 78, 32, 65, 32, 7, 9]
tree = BinarySearchTree()

# 트리구조
for i in data :
    tree.insert(i)

# 트리안에 존재 여부 확인 및 삭제
print(tree.find(9))
print(tree.find(3))


print(tree.delete(78))
print(tree.delete(6))
print(tree.delete(11))

# 트리 구조 출력
print('데이터 출력, 깊이 우선 탐색 왼쪽의 부모부터')
tree.DFTravel()
print(' ', end='\n')
print('데이터 출력, 깊이 우선 탐색 왼쪽의 뿌리부터')
tree.LFTravel()
print(' ', end='\n')
print('데이터 출력, 깊이 우선 탐색 오른쪽의 뿌리부터')
tree.LRTravel()
print(' ', end='\n')
print('데이터 출력, 넓이 우선 탐색 ')
tree.layerTravel()
