hi = input('請輸入身高: ')
wei = input('請輸入體重: ')
him = float(float(hi) / 100)
wei = float(wei)
bmi = wei / (him * him)
bmi = float(bmi)

print('BMI=' ,bmi)

if bmi < 18.5:
    print('過輕')
elif bmi >= 18.5 and bmi < 24:
    print('適中')
elif bmi >= 24 and bmi < 27:
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥胖')
elif bmi >= 30 and bmi <35:
    print('中度肥胖')
else :
	print('重度肥胖')