# 十四届省赛B组
# 2023
# 请求出在12345678(含)至98765432 (含) 中，有多少个数中完全不包含2023
# 完全不包含2023是指无论将这个数的哪些数位移除都不能得到
# 2023。例如20322175，33220022都完全不包含2023，而
# 20230415，20193213 则含有2023(后者取第1268个数
# 位)。
# 答案提交
# 这是一道结果填空的题，你只需要算出结果后提交即可。本题的结
# 果为一个整数，在提交答案时只填写这个整数，填写多余的内容将
# 无法得分。
import time
start_time = time.time()
count = 0

for num in range(12345678, 98765433):
    if '2023' not in str(num):
        # 如果在指定的序列中找到值返回 True，否则返回 False。
        # 比如： 2023 in 20223 这个是true
        count += 1

print(count)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

