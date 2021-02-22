# 이진 탐색 Binary Search
# ******* 중요 ***********
# 탐색 범위 1,000만 단위 이상일 경우 필요
'''
    빠르게 입력 받기
    import sys
    input_data = sys.stdin.readline().rstrip()      # rstrip() : 엔터 제거
'''
'''
    - 데이터 정렬되어 있을 때 사용 가능
    - O( logN )
'''

# 1) 재귀
def binary_search(array, target, start, end):
    if start > end :    # 찾는 원소 없을 때 리턴
        return None

    mid = ( start + end ) // 2

    if array[mid] == target :    # 찾음
        return mid
    elif target < array[mid]:    # 작은 경우, 왼쪽 확인
        return binary_search(array, target, start, mid - 1)     # mid 포함시킬 필요 X
    else:                        # 큰 경우, 오른쪽 확인
        return binary_search(array, target, mid + 1, end)


# 2) 반복문
def binary_search_2(array, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        if target == array[mid] :
            return mid
        elif target < array[mid] :
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
# result = binary_search_2(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)




'''
10 7
1 3 5 7 9 11 13 15 17 19

10 4
1 3 5 7 9 11 13 15 17 19
'''
