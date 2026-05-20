def get_max_value(num_1,num_2):
    return num_1 if num_1 > num_2 else num_2


def main():
    while True:
        try:
            num_1 = float(input("请输入num_1: "))
            num_2 = float(input("请输入num_2: "))
            max_value = get_max_value(num_1, num_2)
            print(f"最大值是：{max_value}")
            break
        except ValueError:
            print("请输入数字,重新来： ")


if __name__ == "__main__":
    main()