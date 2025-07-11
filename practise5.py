# def cal_sum(a, b):
#     sum=a+b
#     print(sum)
#     return sum

# cal_sum(10,5)
# cal_sum(5,24)

#function defination
# def cal_sum(a,b):
#     return a+b
# sum=cal_sum(1,2) #function call
# print(sum)

# def print_hello():
#     print("hello")


# print_hello()
#Average of three numbers
# def cal_avg(a,b,c):
#     average=a+b+c/3
#     print(average)
#     return average
# (cal_avg(2,4,6))
# cal_avg(100,234,654)
# def cal(a,b):
#     return a * b
# print(cal(2,4))
lst=[12.3,34.5,54.6,67.9]

#print(len(lst))
# def print_lst(lst):
#     return lst
# print(len([12.3,34.5,54.6,67.9]))
 
# def print_lst(lst):
#     for item in lst:
#         print(item,end=" ")
# print_lst(lst)


#factorial

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# factorial(6)

#usd to inr
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD=",inr_val,"INR")

# converter(100)
# converter(1)

# def code(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
#     return num

# code(2)  # Output: 2 is even
# code(3)  # Output: 3 is odd
# Recursion
# def show(n):
#     # if (n==0):
#     #     return
#     print(n)
#     show(n-1)
#     print("end")

# show(5) 
# 
# Factorial
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1) * n
# print(fact(6)  )

#sum of natural no
# def natural(n):
#     if(n==0):
#         return 0
#     print(n)
#     return natural(n-1) + n
# sum=natural(5)
# print(sum)

#print all ele in list
def ele(lst,index=0):
    if (index == len(lst)):
        return
    print(lst[index])
    ele(lst,index+1)

fruits=["mandgo","lichi"]

ele(fruits)