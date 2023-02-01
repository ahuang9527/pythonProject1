height = float(input("输入身高（米）："))
weight = float(input("输入体重（千克）："))
bmi = weight / (height * height)  # 计算BMI指数
if bmi < 18.5:
    print("BMI指数为：" + str(bmi))
    print("体重过轻")
elif bmi >= 18.5 and bmi < 24.9:
    print("BMI指数为：" + str(bmi))
    print("正常范围，注意保持")
elif bmi >= 24.9 and bmi < 29.9:
    print("BMI指数为：" + str(bmi))
    print("体重过重")
else:
    print("BMI指数为：" + str(bmi))
    print("肥胖")

