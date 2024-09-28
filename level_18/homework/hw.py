#  შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც


print("walcome to goa bank")
print("do you want creat goa bank acc")

user=input("yes or no:",)

if user == "yes" :
     print("ok lets creat your acc")

elif user == "no" :
    print("are you shor")

user=input("yes or no:",)

if user == "yes" :
     print("oky good bye")

elif user == "no" :
    print("oky then lets creat acc")


name=input("enter your name:",)
surname=input("enter your surname:",)
contact=input("What do you want to register phone emil or piradobis mowmoba:",)

if contact == "phone" :
    phone=input("ok enter your phone:",)

elif contact == "emil" :
    emil=input("enter your emile:",)

else :
    piradobis_mowmoba=input("enter your piradobis mowmoba:",)
    

age=(int(input("enter your age:",)))

if age < 18 :
    print("you ar not 18")

elif age > 18 :
    print("acc is created thanks for using goa bank")


