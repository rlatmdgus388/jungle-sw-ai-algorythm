"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []

    # 큐 생성
    queue = deque()

    # 1. 시작 노드를 큐에 삽입하고 방문 처리
    queue.append(start)
    visited.append(start)
    
    # 방문 기준: 번호가 낮은 인접 노드부터
    def bfs_helper(graph, queue):
        # basse case:
        # 큐가 전부 비었을때
        if not queue:
            return
        
        # 2. 큐에서 뺀 다음 
        node = queue.popleft()
        # 방문하지 않은 인접 노드를 큐에 삽입
        for v in graph[node]:
            # 인접 노드 중 이미 방문한 노드는 continue
            if v in visited:
                continue
            
            queue.append(v)
            # 방문 처리
            visited.append(v)

        bfs_helper(graph, queue)

    bfs_helper(graph, queue)
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

