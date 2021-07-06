a = input("Enter the String:")
digit1 = 0
char1 = 0
for s in a:
    if s.isalpha():
        char1 +=1
    elif s.isdigit():
        digit1 +=1
    else:
        pass
print("Total characters: ", char1)
print("Total Digit: ", digit1)
