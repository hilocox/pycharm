# 题目规定的高风险端口
HIGH_RISK = {21, 23, 445, 1433, 3306, 3389, 6379}
invalid = 0
wrong = 0
right = 0
while True:
    text = input("请输入端口号，输入 q 退出：").strip()

    if text == "q":
        print("程序结束")
        print(f"合规端口号有{right}个，不合规端口号有{wrong}个，输入错误有{invalid}个")
        break

    if not text.isdigit():
        print("输入错误：请输入数字！")
        invalid += 1
        continue

    port = int(text)

    if port < 1 or port > 65535:
        print("输入错误：端口号必须在 1～65535 之间！")
        wrong += 1
        continue

    if port in HIGH_RISK:
        print(f"[警告] {port} 是高风险端口")
    else:
        print(f"[正常] {port}")
        right += 1
