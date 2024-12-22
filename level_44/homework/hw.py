# def double_integer(i):
#     num=int(i) + int(i)
#     return num


# def greet(name):
#     return f"Hello, {name} how are you doing today?"


# def century(year):
#     return (year + 99) // 100


# def maps(a):
#     ints=[]
#     for i in a:
#         ints.append(i * 2)
#     return ints
        


# def digitize(n):
#     result=[]
#     while n > 0:
#         num=n%10
#         result.append(num)
#         n//=10
    
#     if not result:
#         result.append(0)
        
#     return result


# def count_sheeps(sheep):
#     count=0
#     for i in sheep:
#         if i is True:
#             count+=1
#     return count



# def summation(num):
#     total=0
#     for i in range(1, num + 1):
#         total+=i
    
#     return total
        

# def lovefunc( flower1, flower2 ):
#     if flower1 % 2 == 0:
#         flower1_is_even = True
#     else:
#         flower1_is_even = False

#     if flower2 % 2 == 0:
#         flower2_is_even = True
#     else:
#         flower2_is_even = False

#     if flower1_is_even != flower2_is_even:
#         return True
#     else:
#         return False
    


# def sum_array(a):
#     result=0
#     for i in a:
#         result += i
#     return result





# def paperwork(n, m):
#     if n < 0 or m < 0:
#         return 0
#     total_blank_pages = 0
#     for i in range(n): 
#         total_blank_pages += m
#     return total_blank_pages



# def make_upper_case(s):
#     return s.upper()