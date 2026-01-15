def reverse(x):

    if x<0:
        sign = -1
        x*= -1
    elif x>0:
        sign = +1
    else:
        return 0



    answer = 0
    while x:
        if answer<= (2**31 - (x%10))/10:
            answer = answer*10 + x%10
            x//=10
        else:
            return 0
    return answer*sign

choice = int(input("Enter number you want to reverse (with sign): "))
print(reverse(choice))