# n = int(input())

# dp = [1, 2]

# while (len(dp) < n):
#     dp.append((dp[-1] + dp[-2]) % 10007)

# if n == 1 :
#     print(1)
# else :
#     print(dp[-1])

n = int(input())

dp = [1, 2]

while (len(dp) < 1000):
    dp.append((dp[-1] + dp[-2]) % 10007)

print(dp[n-1])