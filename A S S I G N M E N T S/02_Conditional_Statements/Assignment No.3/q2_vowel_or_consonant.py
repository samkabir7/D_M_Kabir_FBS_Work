#Write a program to input any alphabet and check whether it is vowel or consonant.

ch= input("Enter the given alphabet: ")

if(ch in"aeiouAEIOU"):
    print(f"{ch} is a vowel. ")

else:
    print(f"{ch} is a consonant.")