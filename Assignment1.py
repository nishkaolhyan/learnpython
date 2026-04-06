'''Q7. Ask the user for a temperature in Celsius (string input).Convert it to float then calculate and print temperature in Fahrenheit. Conversion Formula: Fahrenheit Temp=[C∗(9/5)]+32
Here C= Celsius Temperature'''
temp=input("enter temperature in Celsius-")
C_temp=float(temp)
F_temp=(C_temp*(9/5))+32
print("Celsius temperature converted into Fahrenheit temperature is-",F_temp,"F")