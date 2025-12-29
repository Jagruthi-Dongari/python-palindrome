# simple program to check if a word is a palindrome

#take input from user
word = input("Enter a word: ")

#convert the word to lowercase so that comparsion is case-sensitive
word = word.lower()

#variable to store the reversed version of the word
reversed_word = ""

#reverse the word manually using a loop
for char in word:
    reversed_word = char + reversed_word

#compare original word with reversed word
if word == reversed_word:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
