import random
word_List=["apple", "orange", "beautiful"]
choicen_word=random.choice(word_List)
print(choicen_word)
disply=[ ]
for i in range(len(choicen_word)):
    disply+=['_']
print(disply)
geussed_lettter=input("Enter a letter:")
for letter in choicen_word:
    if letter==geussed_lettter:
        print("Match")
    else:	
        print("No match")


