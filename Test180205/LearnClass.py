str1 ='test1'

str2 = 'testfunc'

a= __import__(str1)
print(a.__name__)

func= getattr(a,str2)

print("执行：")
func()