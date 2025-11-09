from collections import Counter

# 接收输入
user_input = input("请输入待分析的字符串：")

# 统计字符频率（Counter直接生成频率字典）
freq_counter = Counter(user_input)

# 按频率降序排序
sorted_freq = sorted(freq_counter.items(), key=lambda item: item[1], reverse=True)

# 输出结果
print("字符频率（降序）：")
for char, count in sorted_freq:
    print(f"'{char}'：{count} 次")
