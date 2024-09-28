#პითონში აქამდე რაც კი გვისწავლია ყველაფრის გამოყენებით გააკეთეთ მაქსიმალურად დახვეწილი რეგისტრაციის ფუნქციონალი, ეცადეთ რაც შეიძლება დახვეწოთ და გააუმჯობესოთ
#  დაუმატოთ ბევრი ფუნქციონალები და ასე შემდეგ, აუცილებლად გამოიყენეთ ლუპები

print("registration")

name=input("enter your name:",)


age=(int(input("enter your age:",)))

while age < 18 : 
    age=(int(input("you ar not adult try agen:",)))


contact=input("mobile or emil:",)


if contact == "mobile" :
    mobile=input("enyer your mobile:",)

elif contact == "emile" :
    emile=input("enter your emil:",)

password=input("enter password:",)

print("registration don")



while name != name :
    name=input("incorect name Try again:",)

while password != password :
    password = input("incorect password Try again:", )
