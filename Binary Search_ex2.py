# 떡볶이 떡 길이는?
'''
    떡 절단기 높이 H 정할 수 있다.
    예) 19, 14, 10, 17 cm 떡을 15 cm 절단기로 자르면 잘린 떡은 4, 0, 0, 2 cm 이다. 손님은 6 cm 의 길이를 가져간다.

    손님이 요청한 총 길이가 M 일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값은?
    단, 1 <= N(떡 개수) <= 1,000,000  1 <= M(요청 길이) <= 2,000,000,000     0 <= 개별 떡 높이 <= 1,000,000,000

    (sol) 전형적인 이진 탐색 문제 && Parametric Search 유형 문제(최적화 문제 -> 결정 문제(Y/N))
          절단기 높이(H) 가 10억까지.. 큰 수다! --> 이진 탐색
'''
'''
입력 예시)
4 6
19 15 10 17
출력 예시)
15
'''

# 떡 개수, 요청한 떡의 길이
n, m = map(int, input().split())
# 떡 개별 높이
array = list(map(int, input().split()))

start = 0
end = max(array)    # 절단기 최대 높이 H < 가장 긴 떡의 길이

# 이진 탐색 수행 (반복문)
result = 0
while(start <= end) :
    total = 0   # 떡 길이의 합
    mid = (start + end) // 2  # 절단기 높이 설정

    # 잘랐을 때 떡의 양 계산
    for x in array :
        if x - mid > 0 :
            total += (x - mid)

    if total < m : # 떡 길이 부족하면, 더 많이 남기기(왼쪽 탐색)
        end = mid - 1
    else:   # 떡 길이 충분하면, 덜 남기기(오른쪽 탐색)
        result = mid    # 최대한 덜 잘랐을 때가 정답이므로..
        print(result)
        start = mid + 1


print(result)


