# შექმენით სია რომელშიც გექნებათ 1 დან 20-მდე რიცხვები დაბეჭდეთ თითოეული სიის ელემენტი და თითოეულ მათგანს მიუწერეთ ლუწია თუ კენტი, გამოიყენეთ for loop
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(len(numbers)):
    if numbers [i] % 2==0 :
        print(str(numbers[i]) + "luwia")
    else:
        print(str(numbers[i]) + "kentia")