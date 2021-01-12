# 큐 예제
'''
from collections import queue
queue -> deque() - double_ended queue
push -> append()
pop -> popleft()
First In First Out
'''

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(4)
queue.popleft()
queue.append(1)
queue.popleft()

print(queue)

queue.reverse()
print(queue)

# list(queue) -> deque 객체를 리스트로 변경

'''
# collections 모듈의 deque
# deque는 스택과 큐의 장점 합한 것, 데이터를 넣고 빼는 속도가 리스트에 비해 효율적
# queue 라이브러리보다 간단

# 특히 시작, 끝 부분에 데이터 삽입, 삭제 효과적
# 단, 인덱싱, 슬라이싱 등 불가
'''

from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
data.popleft()
print(data)
print(list(data))