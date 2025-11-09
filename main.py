# 接收用户输入的字符串
text = input("请输入需要分析的字符串：")

# 统计字符频率
char_count = {}
for char in text:
    # 若字符已在字典中，计数+1；否则初始化为1
    char_count[char] = char_count.get(char, 0) + 1

# 按频率降序排序（sorted返回列表，元素为(字符, 频率)的元组）
sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

# 打印结果
print("字符出现频率（降序）：")
for char, count in sorted_chars:
    print(f"字符 '{char}'：出现 {count} 次")
