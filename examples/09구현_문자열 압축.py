# 구현
# 문자열 압축        - https://programmers.co.kr/learn/courses/30/lessons/60057
'''
    문자열에서 연속하는 값은 문자 개수 + 반복되는 값으로 표현하여 문자열 압축
    예) aabbaccc -> 2a2ba3c  (반복되지 않을 때의 1은 생략)

    ababcdcdababcdcd : 문자를 1개 단위로 자르면 압축 안됨. 하지만,
        2개 단위로 자른다면 --> 2ab2cd2ab2cd
        8개 단위로 자른다면 --> 2ababcdcd

    압축한 문자열 중 가장 짧은 것의 길이를 리턴하시오.
'''
'''
    입력 문자열 길이가 1,000 이하 --> 완전 탐색 가능
    단위(step)을 1부터 n/2 까지
'''

s = input()

def solution(s):
    answer = len(s)
    n = len(s)
    result = [] # 각 단계 단위의 길이 저장

    # 길이가 1인 문자열
    if n == 1 :
        return 1

    # 압축 단위 늘려가며 확인
    for step in range(1, n // 2 + 1) :
        compressed = ""
        cut = s[0 : step]   # 앞에서부터 자른 문자열
        same = 1 # 중복 횟수

        for i in range(n // step + 1) :
            # 같은 문자열이 나온 경우( 압축 가능 )
            if cut == s[step * (i + 1) : step * (i + 2)] :
                same += 1
            # 다른 문자열이 나온 경우
            else :
                if same > 1 :
                    compressed += str(same)
                compressed += cut
                # 다음 cut
                cut = s[step * (i + 1) : step * (i + 2)]
                same = 1

        result.append(len(compressed))

    answer = min(result)
    return answer

print(solution(s))


### 해설 코드
s = input()
def solution(s) :
    answer = len(s)
    for step in range(1, len(s) // 2 + 1) :
        compressed = ""
        prev = s[0 : step]
        count = 1
        for j in range(step, len(s), step) :    # step씩 더해서 반복문
            if prev == s[j : j + step] :
                count += 1
            else :
                compressed += str(count) + prev if count >= 2 else prev     # 파이썬 답게
                prev = s[j : j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))   # 리스트 저장 않고 바로바로 최솟값 확인
    return answer

print(solution(s))