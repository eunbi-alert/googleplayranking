calc = input("입력: ")

a = calc.split()



if a[1] == '+':
	print(int(a[0]) + int(a[2]))
elif a[1] == '-':
	print(int(a[0]) - int(a[2]))
elif a[1] == '*':
	print(int(a[0]) * int(a[2]))
elif a[1] == "//":
	print(int(a[0]) / int(a[2]))