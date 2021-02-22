# 두 배열의 원소 교체
'''
- N, K, 배열A, 배열B 의 정보가 주어졌을 때,
- 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력
'''
'''
입력 예시)
5 3
1 2 5 4 3
5 5 6 6 5
5 3
7 9 6 10 9
5 5 6 6 5
'''

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()    # 배열 A 오름차순 정렬
B.sort(reverse=True)    # 배열 B 내림차순 정렬

for i in range(k):  # 최대 k번의 바꿔치기 수행
    if A[i] < B[i]: # 원소 교체
        A[i], B[i] = B[i], A[i]
    else:   # 바꿀 필요 X
        break

print(sum(A))

