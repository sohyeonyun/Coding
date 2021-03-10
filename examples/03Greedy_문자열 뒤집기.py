# 그리디
# EX3 - 문자열 뒤집기
'''
    0과 1로만 이뤄진 문자열 S가 있다. 이 문자열 S에 있는 모든 숫자를 같게 하고 싶다.
    S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이 가능하다.
    뒤집기 연산의 최소 횟수는?

    예) S = 0001100
        4~5번째 문자 뒤집기 --> 횟수 : 1
'''
'''
0001100 --> 1           S의 길이 <= 1,000,000
'''

### 내 풀이(오류)
s = input()

# 연속된 0의 개수, 연속된 1의 개수
num0, num1 = 0, 0

# 이전 문자 기억
if int(s[0]) == 0 :
    before = 1
else :
    before = 0

# 연속된 개수 확인
for i in s :
    if int(i) == 0 and before == 1 :
        num0 += 1
        before = 0
    elif int(i) == 1 and before == 0 :
        num1 += 1
        before = 1

if num0 == 0 :
    num0 = int(1e9)
if num1 == 0 :
    num1 = int(1e9)
print(min(num0, num1))

### 책 풀이
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else :
    count1 += 1

for i in range(len(data) - 1) :
    if data[i] != data[i + 1] :     # 숫자가 바뀌는 경우
        if data[i + 1] == '1' :     # 다음 수가 1로 바뀌는 경우
            count0 += 1
        else :
            count1 += 1

print(min(count0, count1))


'''
    [오류]
    - 같은 숫자가 들어오는 경우도 1로 출력
    - 문자 비교 '1'
'''