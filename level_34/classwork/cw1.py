# შექმენით ფუნქცია რომელიც მომხმარებელს ეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def enter_number():
    num=int(input("enter nuber:",))
    if num % 2 == 0:
        print("kentia")
    elif num % 2 != 0:
        print("luwia")

enter_number()

