# 그리디 - 큰 수의 법칙
'''
주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정 인덱스를 연속 K번 초과하여 더할 수 없다.
또한, 서로 다른 인덱스의 수가 같아도 서로 다른 것으로 간주한다.
예) 2,4,5,2,6 & M=8, K=3
    -> 6+6+6+5+6+6+6+5 = 46
'''

file = open("input.txt", "r")
n, m, k = map(int, file.readline().split())
data = list(map(int, file.readline().split()))
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
file.close()

# sol 1 - 단순
data.sort(reverse=True)
sum = 0
i = 0 # 리스트 인덱스
j = 0 # 특정 인덱스 더한 횟수 < k
for _ in range(m): # 총 m 번 더함
  if(j == k): # k 번째 더했을 때
    sum += data[i + 1]
    j = 0
  else:
    sum += data[i]
    j += 1
  
print(sum)

# sol 2 - 수열
# {6 6 6 5}, {6 6 6 5}, 6, 6
data.sort()
first = data[-1] # 가장 큰 수
second = data[-2] # 두 번째 큰 수

# 가장 큰 수가 더해지는 횟수
count = (m // (k + 1)) * k # 수열 내부
count += m % (k + 1) # 수열 외부

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째 큰 수 더하기

print(result)
