# შეამოწმეთ როგორი არის რიცხვი, ანუ დადებითია თუ უარყოფითი,და დააბრუნეთ საპირისპირო ნიშნის მქონე რიცხვი, ანუ თუ დადებითია დაპრინტეთ  უარყოფითი, ხოლო თუ უარყოფითია დაპრინტეთ დადებითი

number=(int(input("enter number:",)))
if number>0:
    print("-"+str(number))
elif number<0:
    print(-number)