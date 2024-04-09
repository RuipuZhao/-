def check_brackets(string):
    stack = []  #存储左括号
    marked_string = list(string) 

    # Iterate over the string
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)  # 左括号入栈
        elif char == ')':
            if stack:
                stack.pop()  # 左括号出栈
            else:
                marked_string[i] = '?'  # 匹配不到

    # 标记剩余左括号
    for index in stack:
        marked_string[index] = 'x'

    return "".join(marked_string)

def main():
    while True:
        user_input = input()
        result = check_brackets(user_input)
        print(result)

if __name__ == "__main__":
    main()