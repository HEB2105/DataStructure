# Data Structure
- 그림으로 정리한 알고리즘과 자료구조 2018 (조민호)

  
## 자료구조의 분류
- 자료구조 : 단순구조, 선형구조, 비선형구조, 파일구조
![image](https://github.com/HEB2105/DataStructure/assets/126545445/84226b37-f15e-49e8-b00f-eb3f10fb89e4)



## 자료구조의 구현 기술
- 리스트 : 데이터들이 연속적인 공간을 할당 받아 만들어지는 구조
- 연결리스트 : 데이터들이 각각 공간을 할당 받고, 데이터 사이의 연결고리가 만들어지는 구조
    - 종류
        1. **(code)** 연결리스트 Linked List : 한방향, (데이터) - (다음 데이터 포인터)
        2. 더블 연결 리스트 Doubly Linked List : 양방향, (이전 데이터 포인터) - (데이터) - (다음 데이터 포인터)
        3. 환형 연결리스트 Circular Linked List : 더블 연결 리스트의 양끝이 연결되어 있는 구조

## 자료구조의 종류
#### 1. 배열 Array
  - 형태 : 기본 자료형, 사용자 정의 자료형 
#### 2. 리스트 List
  - 순서 리스트 Order List
  - 선형 리스트 Linear List
  - 해시 테이블 Hash Tabel : 해쉬 함수를 이용해 
    
#### 3. **(code)** 스택 Stack
  - LIFO 형
  - 다중 스택 : 하나의 공간에 2개의 스택을 구현하여 각자 사용하는 것
#### 4. **(code)** 큐 Queue
  - FIFO 형, 새로운 프로세스가 사용되기 위해 가장 먼저 메모리에 올라온 프로세스를 아웃
#### 5. 데크 Deque
  - 2개의 포인터를 사용해 양쪽 끝에서 삽입과 삭제 수행
#### 6. 트리 Tree
  - 임의의 노드에서 다른 노드로의 경로가 하나인 경우
  - **(code)** 이진 트리 Binary Tree
      - 종류
        1. 포화 이진 트리 Full Binary Tree : 마지막 까지 꽉 참
        2. 완전 이진 트리 Complete Binary Tree : 마지막 레벨의 왼쪽에서 오른쪽으로
        3. 편향 이진 트리 Skewed Binary Tree : 왼쪽 혹은 오른쪽 서브 트리만
      - 힙 Heap : 이진트리에서 가장 큰 값이나 가장 작은 값을 빠르게 찾을 수 있는 구조
          - 최소 힙 Min Heap, 최대 힙 Max Heap 
#### 7. 그래프 Graph
  - 깊이 우선 탐색 DFS, 넓이 우선 탐색 BFS
  - 신장 트리 : 모든 정점을 포함하는 트리, 사이클은 포함 하지 않음
  - 최소 비용 신장 트리 : 무방향 그래프에서 신장 트리 비용 최소화
      - 방법) Prim, Kruskal
  - 사용 예시) PERT/CPM(프로젝트 일정 관리), 최단경로(Dijkstra 알고리즘)   


# Daily Report
## 2024.04.15
- singly linked list, stack, queue, binary tree 구현
  - 질문) binary tree 의 65번째 줄은 불필요한 코드가 아닌가?
    > node 값이 없을 때 까지 함수를 돌게 되는데, 만약 node 값이 없으면 바로 Flase를 return 하고, 만약 존재 할 경우 66번째 줄에서 if 문을 돌고 Ture를 return... 왜 필요 한걸까...  
