string = "   fly me   to   the moon  "

result=""
new_string = string[::-1]
print(new_string)
# for i in range(len(new_string)):
#         if new_string[i]!=" ":
#             result+=new_string[i]
#         if new_string[i+1] == " ":
#             break
# print(len(result))

for i in range(len(new_string)):
    if new_string[i] == " ":
        continue
    else:
        if new_string!= " ":
            result+=new_string[i]
        if new_string[i+1] == " ":
            break
print(result)