a="Hello one Two Three Four one one  "
print(a.replace("one","1"))
print(a.replace("one","1",1))
print(a.replace("one","1",3))


myList=["Osmam","Mohamed","Sayed"]
print("-".join(myList))
print(" ".join(myList))
print(",".join(myList))
print("***".join(myList))

name="Osmam"
age= 36
rank=10
print("My name is:" +name)
print("My name is:" +name + "and my age" +str(age))


print("May name is: %s" % name)
print("May name is: %s and my age is : %d" %(name, age))


n= "osama"
l="python"
y=10
print("my name is %s Iam %s Developer with %d years Ex" %(n,l,y))

myNumber = 10
print("my number is :%d"%myNumber)
print("my number is :%f"%myNumber)
print("my number is :%2f"%myNumber)


mylongstring="Hello people of Elzero wen school I love you All"
print("message is %.5s"%mylongstring)
print("message is %.9s"%mylongstring)