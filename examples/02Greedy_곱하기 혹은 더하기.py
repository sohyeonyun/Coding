# 그리디
# EX2) 곱하기 혹은 더하기
'''
    숫자 0~9로 이루어진 문자열 S가 주어졌을 때,
    숫자 사이에 'x' 혹은 '+' 연산자를 넣어 계산했을 때 결과적으로 가장 큰 수를 출력하시오.
    모든 연산은 왼쪽에서부터 순서대로 이뤄짐.
    예) 02984 --> (0+2)*9*8*4 = 576
'''
'''
    02984 -> 576
    567 -> 210
'''

data = input()

result = int(data[0])

for i in range(1, len(data)) :
    num = int(data[i])
    # 더하기
    if num <= 1 or result <= 1:
        result += num
    # 곱하기
    else :
        result *= num

print(result)

'''
    [오류]
    result가 1일 때..
'''
