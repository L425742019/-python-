# 冒泡排序（字符串版），是贪心吗？
T = int(input())

for i in range(T):
    n = int(input())
    lis = []        # 空列表用于存储输入的字符
    str = ""        # 空字符串用于最后合并列表元素
    for j in range(n):
       lis.append(input())   # 输入数据
    for mm in range(0,n):
        for nn in range(mm+1,n):
            if lis[mm]+lis[nn] > lis[nn]+lis[mm]:
                lis[mm],lis[nn] = lis[nn],lis[mm]  # 经典冒泡排序-字符串版
    for i in range(n):
        str = str + lis[i]   # 合并列表
    print(str)
