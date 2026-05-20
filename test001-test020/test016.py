# match 语句提供了更简洁的多条件匹配语法，类似于其他语言中的 switch/case。

pay_way = "ali Pay"

match pay_way:
    case "ali Pay":
        print("支付宝")
    case "wei xin Pay":
        print("微信支付")
    case "yin lian Pay":
        print("银联支付")
    case _:             # 相当于 default 分支
        print("未匹配成功")

print("===============================")
