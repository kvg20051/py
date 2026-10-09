print("ваше имя?")
name=input()
print("возраст?")
age=int(input())
if age > 65:
    print(name, ",Вы уже пенсионер!")

elif age <=0:
    print(name, ",Вы ввели неверный возвраст!")

else:
    print(name, ",Продолжайте работать!")
