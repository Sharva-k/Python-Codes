type=input("Enter 'F' if you wan to convert into Fahrenheit or enter 'C' if you want to convert into celsius: ")
if type.lower()=="c":
    tempf=int(input("Enter Fahrenheit temp you want to convert into celsius: "))
    final_temp=(tempf-32)/1.8
    print(f"{tempf} Fahrenheit = {final_temp} Celsius.")
else:
    tempc=int(input("Enter celsius temp you want to convert into Fahrenheit: "))
    final_tempc=(tempc*1.8)+32
    print(f"{tempc} Celsius ={final_tempc} Fahrenheit.")
