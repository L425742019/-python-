# dp
# 输入部分
n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))
# 扩充
lis = [0] + lis
n = n + 1

if n == 1 or n == 2 or n == 0:
    print(0)
else:
    #  初始化
    dp = [[0,0] for _ in range(n+1)]

    # dp[][0] 后面的 0 代表没跃迁，所以dp[][1] 代表跃迁了
    dp[1][0] = lis[1]   # 第一层楼顶
    dp[1][1] = 0
    dp[2][1] = 0        # 第二层楼顶
    dp[2][0] = min(dp[1][0],lis[2])

    for i in range(3,n):
        # 走到第i层楼顶有两种方式：
        # 走到第i-1层楼顶再走到第i层楼栋 or 跃迁到第i-1层楼顶再走到第i层楼顶
        dp[i][0] = min(dp[i-1][0] +lis[i] , dp[i-1][1] +lis[i])
        # 跃迁到第i层楼顶有两种方式：
        # 走到第i-1层楼顶再跃迁到第i层楼顶 or 走到第i-2层再跃迁到第i层楼顶
        dp[i][1] = min(dp[i-1][0] , dp[i-2][0])
    min_distance = min(dp[i][0],dp[i][1])
    print(min_distance)