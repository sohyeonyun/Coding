# 그리디 - 거스름돈
n = 1260
count = 0

coins = [500, 100, 50, 10]
for coin in coins:
  count += n // coin
  n %= coin

print(count)