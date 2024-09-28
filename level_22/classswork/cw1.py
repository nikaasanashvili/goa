# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვი და თან გვერძე მიუწერეთ ლუწია თუ კენტი

num=(int(input("enter number:",)))
i=0
while i < num :  
    i = i + 1
    if i % 2 == 0 :
        print(str(i) + "luwia")
    else :
        print(str(i) + "kenti")





