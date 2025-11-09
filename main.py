def analyze_text():
    # 接收输入并统一转为小写（忽略大小写）
    text = input("请输入待分析的文本：").lower()
    
    # 初始化字典，仅统计字母
    letter_freq = {}
    for char in text:
        # 仅处理字母字符
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1
    
    # 按频率降序排序，若频率相同则按字母升序排列
    sorted_letters = sorted(
        letter_freq.items(),
        key=lambda x: (-x[1], x[0])  # 先按频率降序，再按字母升序
    )
    
    # 输出结果
    if not sorted_letters:
        print("文本中未包含字母。")
        return
    
    print("字母出现频率（降序，频率相同按字母排序）：")
    for letter, count in sorted_letters:
        print(f"字母 '{letter}'：{count} 次")

# 调用函数
analyze_text()
