#Designed by Jonathan Abramson
#Jonathanabramson14@gmail.com
#Sentence Analytics

print("This program will tell you about sentence analytics.")
string=input("Please enter your sentence:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:", word)
print("Number of characters in the string:", char)
words = string.split()
average = sum(len(word) for word in words)/len(words)
print("Average word length:",average )