n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 3)
sum = 0
dp[n] = dp[n + 1] = dp[n + 2] = 0
for i in range(n - 1, -1, -1):
    sum += a[i]
    dp[i] = sum - min(min(dp[i + 1], dp[i + 2]), dp[i + 3])
print(dp[0])