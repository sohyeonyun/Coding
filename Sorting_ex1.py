# 내림차순으로 정렬하는 프로그램
'''
첫 줄 : 수열 원소 개수 N
둘 째 줄부터 ~ : N개의 수 입력됨.
'''
'''
입력 예시)
3
15
27
12
'''

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data = sorted(data, reverse=True)
for i in data:
    print(i, end=' ')