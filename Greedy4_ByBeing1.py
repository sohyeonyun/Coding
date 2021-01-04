# 1이 될 때까지
'''
    N 이 1 이 될 때까지 다음 반복
    1. N - 1
    2. N / K (단, N 이 K 로 나눠떨어질 때)
    최소 수행 횟수 출력
'''
import time

n, k = map(int, input().split())
start_time = time.time()

count = 0
while(n != 1):
    if n % k == 0:
        n /= k
    else:
        n -= 1
    count += 1

print(count)

end_time = time.time()
print(end_time - start_time)

# sol2
n, k = map(int, input().split())
start_time = time.time()

result = 0
while True:
    # n이 k로 나눠떨어질 때까지 1씩 빼기
    target = (n // k) * k 
    result += (n - target) # 나머지
    n = target
    # 더 이상 나눌 수 없을 때
    if n < k: 
        break
    # k로 나누기
    result += 1 
    n //= k

# 마지막으로 남은 수에 대해 1 빼기
result += (n - 1)
print(result)

end_time = time.time()
print(end_time - start_time)