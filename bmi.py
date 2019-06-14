def bmi1():
	high = float(input('請輸入身高(公分): '))
	weight = float(input('請輸入體重: '))
	high = high / 100
	bmi = weight / (high * high)
	bmi = str(round(bmi, 2))
	return bmi

def judge1(bmi):
	
	if bmi < 18.5:
		judge = '過輕'
	elif bmi >= 18.5 and bmi < 24:
		judge = '正常'
	elif bmi >= 24 and bmi < 27:
		judge = '過重'
	elif bmi >= 27 and bmi <30:
		judge = '輕度肥胖'
	elif bmi >= 30 and bmi <35:
		judge = '中度肥胖'
	elif bmi >= 35:
		judge = '重度肥胖'
	return judge

def main():
	bmi = bmi1()
	judge = judge1(float(bmi))
	print('您的bmi指數為' + bmi + ', ' + judge)

main()
