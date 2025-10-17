# 初始化计数器
alpha = 0
digit = 0
space = 0
other = 0
# 获取输入（兼容不同环境的输入处理）
try:
    input_str = input()
except:
    input_str = ""
# 遍历每个字符
for c in input_str:
    # 英文字符判断
    if (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')):
        alpha += 1
    # 数字判断
        elif ord('0') <= ord(c) <= ord('9'):
            digit += 1
    # 空格判断（仅针对半角空格）
elif ord(c) == 32:
space += 1
    # 其他字符
else:
other += 1

# 严格按照格式输出
print(f"英文字符: {alpha}")
print(f"数字: {digit}")
print(f"空格: {space}")
print(f"其他字符: {other}")
