def calc(*numbers):
	summ = 0
	for n in numbers:
		summ += n**2
	return summ


print(calc(1, 2, 3, 4))
a = [1, 2, 3, 4]
print(calc(*a))


def person(name, age, **kw):
	print(f'name:{name},', f'age:{age},', f'others:{kw}')


person('Michael', 30)
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'student'}
person('Sunpq', 23, **extra)
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
