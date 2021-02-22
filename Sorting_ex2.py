# 성적이 낮은 순서로 학생 출력하기

'''
첫 줄 : 학생 수 N
둘째 줄 ~ : 학생이름 성적
출력 : 성적이 낮은 순서대로 학생 이름 공백 간격 출력
'''
'''
입력 예시)
3
홍길동 95
이순신 77
김철수 80
'''

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1])) # 튜플로 저장

array = sorted(array, key=lambda student: student[1]) # 키를 이용하여 점수 기준으로 정렬

for student in array:
    print(student[0], end=' ')


# lambda x: x**2
# x 입력, 콜론 뒤의 값 리턴


