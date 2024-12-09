# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.

num=int(input("ener number:",))

def luwi_kenti(num):
    if num % 2==0:
        print("kentia")
    else:
        print("luwia")

luwi_kenti(num)