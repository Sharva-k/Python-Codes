stri=input("Enter word, phrase, or sequence you want to check for palindrome: ")
rev_stri=stri[::-1]
if stri==rev_stri:
    print(f"Given word, phrase, or sequence is palindrome as '{stri}' = '{rev_stri}'.")
else:
    print(f"Given word, phrase, or sequence is  not palindrome as '{stri}' is not equal to '{rev_stri}'.")
