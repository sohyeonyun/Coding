# 부품 찾기
'''
    손님이 요청한 부품의 번호 순서대로 부품 확인. 있으면 yes, 없으면 no 출력
    --> list 정렬 후 이진탐색 사용

    대량 데이터 검색 --> 이진 탐색     정렬 O(NlogN) + 탐색 O(MlogN)
'''

def binary_search(array, target, start, end):
    if start > end :
        return None

    mid = (start + end) // 2
    if target == array[mid] :
        return mid
    elif target < array[mid] :
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())    # 전체 부품 개수
total = list(map(int, input().split()))

m = int(input())    # 요청 부품 개수
x = list(map(int, input().split()))

total.sort()    # 이진 탐색 위한 정렬
for i in x :
    result = binary_search(total, i, 0, n - 1)
    if result != None :
        print('yes', end=' ')
    else:
        print('no', end=' ')


'''
5
8 3 7 9 2
3
5 9 7
'''

# sol2 - 계수 정렬(Count Sort) 개념 이용
n = int(input())
array = [0] * 1000001     # 입력 최대 개수 + 1
for i in input().split() :  # 전체 부품 수 기록
    array[int(i)] += 1

m = int(input())
x = list(map(int, input().split()))
for i in x :    # 요청 부품 하나씩 확인
    if array[i] == 1 :  # 해당 부품이 있는지 확인
        print('yes', end=' ')
    else:
        print('no', end= ' ')

