
# program to test a letter is vowel or not

vowel=['a','e','i','o','u']

while True :
    letter= input("Please enter a letter: ")
    if len(letter)!=1:
        print("Please enter only one letter")
    else :    
        if letter.lower() in vowel:
            print(f"The letter {letter} is vowel")
        else: print(f"The letter {letter} is NOT vowel")