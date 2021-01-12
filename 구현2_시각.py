# 완전탐색 - 시각
n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1
                print(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2),sep=":")

print(count)