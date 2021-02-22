'''
    정렬 문제
    1) 기본 정렬 --> sorted(), sort()
    2) 정렬 알고리즘 원리 묻는 문제 --> 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리
    2) 더 빠른 정렬 필요한 문제 --> 계수 정렬(Count Sort) : 데이터 범위 한정
'''

'''
    <python SWAP code>
    array[0], array[1] = array[1], array[0]
'''

### Selection Sort
# - 가장 작은 것을 선택해 앞으로 보냄
# O(N*N)
array = [7, 5, 9, 1, 6, 8, 10, 2, 4, 3]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print("Selection Sort :", array)


### Insertion Sort
# - 앞 데이터가 정렬돼있다는 가정하에, 각 데이터를 적절한 위치에 삽입
# O(N*N), 거의 정렬된 데이터에선 매우 빠르게 동작
array = [7, 5, 9, 1, 6, 8, 10, 2, 4, 3]

for i in range(1, len(array)):
    for j in range(i, 0, -1):   # i~1 까지, i--
        if array[j] < array[j-1] :  # 한 칸씩 왼쪽으로 이동...j!
            array[j], array[j-1] = array[j-1], array[j] # swap
        else:   # 자기보다 작은 데이터 만나면 멈춤
            break

print("Insertion Sort :", array)


### Quick Sort
# - 기준 데이터(pivot) 설정 후 그 기준으로 큰 숫자와 작은 숫자를 교환 -> 재귀
# - 호어 분항 : 첫 번째 데이터를 피벗으로 정함.
# O(NlogN), 데이터 수 많을수록 압도적으로 빠름. 이미 정렬된 데이터의 경우 매우 느림.
array = [7, 5, 9, 1, 6, 8, 10, 2, 4, 3]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start   # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:   # 피벗보다 큰 값 찾기
            left += 1
        while start < right and array[pivot] <= array[right]:  # 피벗보다 작은 값 찾기
            right -= 1
        if left > right:    # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left] # swap

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print("Quick Sort :", array)


### Quick Sort - 파이썬 버전
# - 파이썬 장점 살리고 직관적인 코드, 시간은 조금 비효율적
def quick_sort_python(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)



### Count Sort 계수 정렬
'''
- 양의 정수 데이터, 중복O
- 모든 범위를 담을 수 있는 크기의 리스트(배열) 선언 ( 0 ~ 최대값 )
- 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000 넘지 않을 때 효과적 --> 1,000,001 개의 리스트
- O(데이터 개수 + 최대값 크기), 현존 알고리즘 중 기수 정렬(Radix Sort)와 더불어 가장 빠름.
- 크기 한정, 동일한 값 가지는 데이터 여러 개일 때 효과적 --> 성적
- 공간 복잡도 문제

- 누적합 사용 --> stable
'''

array = [0, 7, 6, 5, 9, 1, 6, 8, 10, 2, 8, 4, 3, 3, 0]

# 모든 범위를 포함하는 리스트 선언 ( 0으로 초기화 )
count = [0] * (max(array) + 1)

# 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(array)) :
    count[array[i]] += 1

print("Count Sort : [ ", end='')

for i in range(len(count)) : # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]) :
        print(i, end=' ') # 띄어쓰기 구분으로 등장한 횟수만큼 인덱스 출력

print("]")


### 파이썬 정렬 라이브러리
# - O( NlogN ) 보장

# 1) sorted() : 입력(리스트, 집합, 딕셔너리) --> 출력(리스트)
array = [0, 7, 6, 5, 9, 1, 6, 8, 10, 2, 8, 4, 3, 3, 0]

result = sorted(array)
print("sorted() : ", result)

# 2) .sort() : 리스트 객체의 내장 함수.. 리턴 X
array.sort()
print(".sort() : ", array)

# key 매개변수 입력
'''
    - sorted(), sort() 둘 다 key 매개변수를 입력받을 수 있음.
    - key 값으로는 함수가 들어가야 함. or 람다 함수
'''
array = [('사과', 3), ('바나나', 1), ('수박', 5)]

def setting(data):
    return data[1]  # 두 번째 원소 기준

result = sorted(array, key = setting)
print(result)
























