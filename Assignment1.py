# Q4. The user enters a string containing a number(e.g."45").Convert it to: a)an integer b)float c) a string again
#a)an integer
num=input("Enter a number")
num_int=int(num)
num_float=float(num)
num_str=str(num)
print("The integer value is-",num_int,"& it's type is-",type(num_int))
print("The float value is-",num_float,"& it's type is-",type(num_float))
print("The string value is-",num_str,"& it's type is-",type(num_str))