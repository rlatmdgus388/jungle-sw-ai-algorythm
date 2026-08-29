"""
[분할 정복 - 배열의 최댓값 찾기]

문제 설명:
- 분할 정복(Divide and Conquer) 방식으로 배열의 최댓값을 찾습니다.
- 배열을 반으로 나누고, 각 부분의 최댓값을 구한 후 비교합니다.

입력:
- arr: 정수 배열
- left: 시작 인덱스
- right: 끝 인덱스

출력:
- 배열의 최댓값

예제:
입력: [3, 5, 1, 8, 2, 9, 4]
출력: 9

힌트:
- Base case: left == right일 때 arr[left] 반환
- 배열을 반으로 나누어 재귀 호출
- 왼쪽과 오른쪽의 최댓값 중 큰 값 반환
"""

# 분할 정복:
#  한 번에 해결하기 어려운 거대한 문제를 더 이상 쪼갤 수 없을 때까지 아주 작은 문제로 나눈 뒤, 각각을 해결하고 다시 합쳐서 전체의 해답을 구하는 알고리즘

# 분할 정복의 3 단계:
#  1. 분할 (Divide)
#   원래 문제를 동일한 형태의 더 작은 하위 문제(Subproblem)들로 나눈다.
#  2. 정복 (Conquer)
#   나뉜 하위 문제가 충분히 작아서 바로 답을 알 수 있는 상태(Base Case)가 되면 즉시 해결함.
#   만약 여전히 크다면 재귀(Recursion)적으로 다시 분할을 진행.
#  3. 결합 / 조합 (Combine)
#   작게 쪼개어 해결된 하위 문제들의 해답을 다시 하나로 병합하여, 원래 큰 문제의 최종 정답을 만든다.

def find_max_divide_conquer(arr, left, right):
    """
    분할 정복으로 최댓값 찾기
    
    Args:
        arr: 배열
        left: 시작 인덱스
        right: 끝 인덱스
    
    Returns:
        최댓값
    """
    # TODO: base case - 원소가 하나면 그 값 반환
    if len(arr) == 1:
        return arr[0]
    
    # TODO: 중간 지점 계산
    mid = left + right // 2
    
    # TODO: 왼쪽 절반의 최댓값
    left_max = max(arr[:mid])
        
    # TODO: 오른쪽 절반의 최댓값
    right_max = max(arr[mid+1:])
    
    # TODO: 둘 중 큰 값 반환
    if left_max > right_max:
        return left_max
    else:
        return right_max 

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [3, 5, 1, 8, 2, 9, 4]
    result1 = find_max_divide_conquer(arr1, 0, len(arr1) - 1)
    print(f"배열: {arr1}")
    print(f"최댓값: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [10, 20, 30, 40, 50]
    result2 = find_max_divide_conquer(arr2, 0, len(arr2) - 1)
    print(f"배열: {arr2}")
    print(f"최댓값: {result2}")
    print()
    
    # 테스트 케이스 3
    arr3 = [100]
    result3 = find_max_divide_conquer(arr3, 0, len(arr3) - 1)
    print(f"배열: {arr3}")
    print(f"최댓값: {result3}")


