def analyze_letter_frequency():
    # 接收用户输入
    user_input = input("请输入待分析的字符串：")
    
    # 统计字母频率（仅保留字母）
    letter_counts = {}
    for char in user_input:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # 按频率降序排序
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
    # 输出结果
    if not sorted_letters:
        print("输入中未包含字母。")
        return
    
    print("\n=== 字母频率统计结果（降序） ===")
    for letter, count in sorted_letters:
        print(f"'{letter}'：出现 {count} 次")

# 主程序入口（确保在GitHub环境中可直接运行）
if __name__ == "__main__":
    analyze_letter_frequency()
