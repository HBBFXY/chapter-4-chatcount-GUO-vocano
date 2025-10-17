# 字符统计程序

# 从键盘输入一行字符
text = input("请输入一行字符：")

# 初始化计数器
letter_count = 0  # 英文字符计数
digit_count = 0   # 数字计数
space_count = 0   # 空格计数
other_count = 0   # 其他字符计数

# 遍历每个字符并统计
for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

# 按照指定格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
