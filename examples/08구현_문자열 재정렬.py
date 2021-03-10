# 구현
# 문자열 재정렬
'''
    입력 : 알파벳 대문자 + 숫자(0~9)
    출력 : 알파벳 오름차순 -> 모든 숫자의 합
    예) K1KA5CB7 -> ABCKK13
        AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20
'''

s = input()
result = []
sum = 0
for i in s :
    if i.isnumeric() :
        sum += int(i)
    else :
        result.append(i)

result.sort()

if sum != 0 :
    result.append(str(sum))

# 리스트 -> 문자열 변환 !!
print(''.join(result))
