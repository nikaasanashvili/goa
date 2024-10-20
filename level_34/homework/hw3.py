# დაწერეთ ფუნქცია რომელიც მომხმარებლისგან იღებს რიცხვს და თუ რიცხვი 1-დან 10-მდეა დაბეჭდავს თუარა დაუბეჭდავს "არასწორი რიცხვი"

def number():
    num=int(input("enter number:",))
    if num > 10:
        print("too high number")
    elif num < 0:
        print("too low number")

number()