# 그리디
# 무지의 먹방 라이브
import heapq

def solution(food_times, k) :
    time = 0

    if sum(food_times) <= k :
        return -1

    q = []
    for i in range(len(food_times)) :
        heapq.heappush(q, (food_times[i], (i + 1)))   # (음식 양, 인덱스) 삽입

    food, index = heapq.heappop(q)



    return 1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))


# from collections import deque
#
# def solution(food_times, k):
#     time = 0
#
#     # 덜 먹은 음식 인덱스 큐에 삽입
#     q = deque()
#     for i in range(len(food_times)):
#         deque.append(q, i)
#
#     # 큐 빌 때까지 (음식 다 먹을 때까지)
#     while q:
#         # 네트워크 장애 시간
#         if time == k:
#             break
#         index = deque.popleft(q)
#         # 한 입 섭취
#         food_times[index] -= 1
#         # 음식 남으면 다시 큐에 삽입
#         if food_times[index] != 0:
#             deque.append(q, index)
#         time += 1
#
#     if time < k or not q :
#         return -1
#     else :
#         return deque.popleft(q) + 1
#
# food_times = [1, 1, 1, 1, 1]
# k = 5
# print(solution(food_times, k))

