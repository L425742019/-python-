# 贪心吧
N = int(input())

# 每箱冰块的搬运耗时Ti及融化速度Di.
# Ti 越小越优先，Di越大越优先
# 即Ti/Di 越大越优先

precedence = []
Ti  = []
Di  = []
for i in range(N):
    T_D = input()
    T,D = T_D.split()
    # Ti
    Ti.append(int(T))
    # Di
    Di.append(int(D))
    # 优先级
    precedence.append(Di[i]/Ti[i])

count = 0
# 根据precedence列表中相应索引的值对范围内的元素进行降序排序
order = sorted(range(N), key=lambda k: precedence[k], reverse=True)
# order = [5, 1, 2, 3, 0, 4],即先取第6个，再取第2个....
total_melt = 0
time_melt = 0
for i in order:
    total_melt += time_melt * Di[i]
    time_melt += Ti[i]

print(total_melt)