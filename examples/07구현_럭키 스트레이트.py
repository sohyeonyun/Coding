# 구현
# 럭키 스트레이트 -    https://www.acmicpc.net/problem/18406
'''
    게임 필살기인 '럭키 스트레이트'는 특정 조건에서만 발휘 가능하다.
    특정 조건) 현재 캐릭터의 점수 N의 자릿수(항상 짝수)를 기준으로 반으로 나눴을 때
              왼쪽 부분의 각 자릿수의 합 == 오른쪽 부분의 각 자릿수의 합
    예) 123,402 --> (1+2+3) == (4+0+2)
    이 스킬을 발생할 수 있는지 알려주시오.
'''

n = input()
mid = len(n) // 2

left = 0
right = 0
for i in range(0, mid) :
    left += int(n[i])
for i in range(mid, len(n)) :
    right += int(n[i])

if left == right :
    print("LUCKY")
else :
    print("READY")
