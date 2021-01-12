# 재귀 함수 - Recursive Function

'''
RecursiveError : 재귀의 최대 깊이 초과. 파이썬 인터프리터는 호출 횟수 제한 있다.
종료 조건 필요
내부적으로 스택 구조와 동일 -> 스택 활용하는 알고리즘을 재귀함수로 구현 가능 (ex. DFS)
'''

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서 ', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

# factorial 예제
'''
반복문보다 재귀함수가 더 간결 (수학의 점화식 그대로 옮겼기 때문)
'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
