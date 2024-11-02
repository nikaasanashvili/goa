# დაწერე ფუნქცია, რომელიც აბრუნებს ორ რიცხვს შორის მინიმალურ მნიშვნელობას.


num=[12, 41, 14, 23, 18, 15, 51, 35, 19]
larges=num[0]

def num():
    for i in num:
        if i < larges:
            larges=i
    print(larges)

num()

