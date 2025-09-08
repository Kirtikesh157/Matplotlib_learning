# fname=input ("enter your first name:-")
# lname=input ("enter your last name:-")
# print("your full namr is :-",fname,lname)
# print("your full namr is :-",fname+lname)
# print("your full namr is :-",fname+""+lname)


# Fnum=input ("enter your first number=>")
# Snum=input ("enter your second number=>")
# print('addition of two number is =>',Fnum+Snum)
# print('addition of two number is =>',int(Fnum)+int(Snum))
# print('addition of two number is =>',float(Fnum)+float(Snum))

# PYLIST=[1,2,3,4,5]
# print(PYLIST)
# PYTUPLE=[1,2,3,4,5]  

# print(PYTUPLE)
# PYSET=[1,2,3,4,5]
# print(PYSET)
# PYDICT=[1,2,3,4,5]
# print(PYDICT)


#//////////////   REVERS STRING   //////////////////
# text="Revers"
# reversed_user=text[::-1]
# print(text)
# print('After revers the text:- ')
# print(reversed_user)

# kit=(input("enter the value"))
# reversed_user=kit[::-1]
# print(kit)
# print('After revers the text:- ')
# print(reversed_user)


 # ////////     now using for loop in each character   ////////////
# var="kirtikesh"
# reversed_tech=""
# for i in var:
#     reversed_tech=i+reversed_tech
#     print(reversed_tech)
# def reverse_user(u):
  
#     return u[::-1]
# print(reverse_user("kirtikesh"))

# lst=[9,4,6,2,5,3]
# larg=max(lst)
# print("largest number in list is:-",larg)

#//////////  palindrome ////////////


# user=input('Enter the value')

# pal=user[::-1]

# if user==pal:
#       print(f"This {user} is palindrome")
# else:
#   print(f"This  {user} is not palindrome")
        

#////////////// checking prime number    /////////////////////////////////


# p=int(input("Enter the value"))

# is_prime = p > 1 and all(p % i != 0 for i in range(2, int(p**0.5) + 1))
    
# if is_prime:
#     print(f"{p} is a prime number") 
# else:
#     print(f"{p} is not a prime number")

# fruits=["apple", "banana", "cherry", "mango", "grapes","struberry"]
# print(type(fruits[0
#                   ]))
# slice_n=fruits[:6:2]
# print(slice_n)
# User=input("enter the value")

# reversed_tech=""
# for i in User:
#     reversed_tech=User.reversed
# kiy    print(reversed_tech)






# user=input('Enter the value')m

# pal=user[::-1]

# if user==pal:
#       print(f"This {user} is palindrome")
# else:
#   print(f"This  {user} is not palindrome")
        





# user=input('Enter the value')


# if sum(user)==sum(user) [::-1]:
      


#       print(f"This {user} is palindrome")
# else:
#   print(f"This  {user} is not palindrome")
  

num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10       
    rev = rev * 10 + digit  
    temp //= 10             

if num == rev:
    print(f" Yes! {num} is a Palindrome number.")
else:
    print(f" No! {num} is NOT a Palindrome number.")



# table= int(input("enter the number"))
# kd=0
# for i in range(1,11):
#     kd=i*table
#     print(kd) 


'''
Lambda functon => 👉 Python me lambda function ek single-line anonymous function hota hai.
                      Matlab ise banane ke liye def likhne ki zarurat nahi hoti, directly inline function bana sakte ho.
                      
syntax => lambda arguments : expression
'''
#  checking even or odd

# sq=lambda a:"Even"if a%2==0 else "Odd" 
# print(sq(7)
'''

'''

"""
Ex"""

# user=input('Enter the value')


# if sum(user)==sum(user) [::-1]:
      


#     print(f"This {user} is palindrome")
# else:
#     print(f"This  {user} is not palindrome")

table= int(input("enter the number"))
table1= int(input("enter the number"))
for i in range(1,11):
    for j in range(table,table1+1):

        print(j*i  ,    end="\t")
        
    print ()  