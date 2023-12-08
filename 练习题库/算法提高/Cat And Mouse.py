# 读入地图
mp = []
for i in range(10):
    row = input().strip()
    mp.append(list(row))

# 坐标移动，上右下左即北东南西
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# cat和 mouse的初始方向
d1 = 0
d2 = 0
# cat 坐标
x1, y1 = 4, 5
# mouse 坐标
x2, y2 = 7, 2

# 存储相遇时间
ans = 0

while x1 != x2 or y1 != y2:
    # cat 向前一步
    x1 += dx[d1]
    y1 += dy[d1]
    # mouse 向前一步
    x2 += dx[d2]
    y2 += dy[d2]

    # 猫移动后超出了地图边界或者遇到障碍物，则猫需要回退一步，位置恢复原状，并且改变猫的方向。
    if x1 < 0 or x1 > 9 or y1 < 0 or y1 > 9 or mp[x1][y1] == '*':
        x1 -= dx[d1]
        y1 -= dy[d1]
        d1 = (d1 + 1) % 4

    # 老鼠同理
    if x2 < 0 or x2 > 9 or y2 < 0 or y2 > 9 or mp[x2][y2] == '*':
        x2 -= dx[d2]
        y2 -= dy[d2]
        d2 = (d2 + 1) % 4

    ans += 1

print(ans)
