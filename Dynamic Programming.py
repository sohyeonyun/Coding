# Dynamic Programming (동적 계획법) : 메모리 공간을 약간 더 사용해서 중복되는 연산 줄이자!
'''
    * 다음 조건에서 사용)
    1. 큰 문제를 작은 문제로 나눌 수 있다.
    2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

    * Memoization 기법 ( == Caching) := 일시적으로 값을 저장하는 방법
        : 다이나믹 프로그래밍 구현 기법 중 하나. 한 번 구한 결과를 메모리 공간에 메모해두고 나중에 그 결과를 그래도 가져오는 기법

    * 타 기법과 차이점.
        - Dynamic Programming (피보나치) : 한 번 해결한 문제 다시금 해결. 저장된 답을 반환.
        - Divide and Conquer  (퀵 정렬)  : 한 번 계산한 피벗 값 다시 계산할 일 X

    * Top-Down(메모제이션) 방식 : 큰 문제를 해결하기 위해 작은 문제 호출 (재귀)
    * Bottom-Up 방식 : 작은 문제부터 차근히 답 도출 (반복문), --> 다이나믹의 전형적 형태
                     - DP 테이블 : 결과 저장용 리스트
'''

### 예) 피보나치 함수
# (1) 일반 점화식 버전 --> O(2^N) 지수 시간 소요.. 동일한 함수가 반복적으로 호출됨.
def fibo(x) :
    if x == 1 or x == 2 :
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))


# (2-1) Memoization 기법 (Top-Down) --> O(N)
d = [0] * 100   # 한 번 계산된 결과를 저장하기 위한 리스트 초기화
def fibo2(x) :
    # print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2 :
        return 1
    if d[x] != 0 :  # 이미 계산한 문제면, 그대로 반환
        return d[x]
    d[x] = fibo2(x - 1) + fibo2(x - 2)  # 아직 계산하지 않은 문제면, 점화식 따라 결과 반환
    return d[x]

print(fibo2(99))


# (2-2) Bottom-Up --> O(N)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1) :
    d[i] = d[i - 1] + d[i - 2]

print(d[n])