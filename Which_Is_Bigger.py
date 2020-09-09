# a simple program to show which text is bigger
text1 = input("give me a text:\n")
print("-----------------------------")
text2 = input("give me another text:\n")

if len(text1) > len(text2):
    print("text", '(', text1, ')', "is \"bigger\" than text", '(', text2, ')')
else:
    print("text", '(', text2, ')', "is \"bigger\" than text", '(', text1, ')')
