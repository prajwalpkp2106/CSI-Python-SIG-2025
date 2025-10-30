#define string
# s1 = 'Hello'
# s2 = "World"
# s3 = '''This is
# a multi-line string'''

# print(s3)


# Accessing Characters

# Strings behave like sequences (like lists).
# Access using indexing or slicing.

s = "Python"
# print(s[0])     
# print(s[-1])    

# # Slicing
# print(s[2:5])
# print(s[1:4])  
# print(s[:3])   
# print(s[2:])    


# # String Concatenation & Repetition
#a = "Hello"
# b = "World"
# c=a+b
# print(c) 


# # Repetition
#print(a * 3)    



# # String Iteration
# s = "Python"
# for char in s:
#     print(char)



# # # String Functions & Methods

# # # 1.Case Conversion
#  text = "hello wORld , python is easy"
# print(text.upper())     
# print(text.lower())     
# print(text.title())     
# print(text.capitalize())


# # # 2.Searching & Finding
# msg = "Python programming is fun"
# print(msg.find("pro"))      
# print(msg.rfind("is"))    
# print(msg.count("n"))       # 3
# print("fun" in msg)         
# print("java" not in msg)    


# # #3.Replacing & Splitting

# msg = "I love Java"
# # print(msg.replace("Java", "Python"))

# # # # # Splitting 
# words = msg.split()   
# print(words)



# # # #4.Trimming (Removing spaces/symbols)
# s = "   hello   "
# print(s.strip())   # "hello"
# print(s.lstrip())  # "hello   "
# print(s.rstrip())  # "   hello"

# s2 = "###Python###"
# print(s2.strip("#"))  



# # #5.Checking Types
# s = "Python123"
# print(s.isalpha())    
# print("Python".isalpha()) 
# print("123".isdigit())    
#print("123".isalnum()) 
# print(" ".isspace())      



# # #6.Formatting Strings
# name = "Kishor"
# age = 20
# print("My name is {} and I am {} years old ".format(age, name))
# print(f"My name is {name} and I am {age} years old")


   

# # # Escape Sequences
# print("Hello\nWorld")   # newline
# print("Hello\tWorld")   # tab
# print("He said \"Python is fun\"")


# # # String Comparison
# print("apple" == "apple")   # True
# print("apple" >"aanana")   # True (lexicographical order)
# print("A" < "a")            # True (ASCII comparison)


# # # Useful Built-in Functions 
# s = "python"
# print(len(s))     # 6
# print(max(s))     # y (highest ASCII)
# print(min(s))     # h (lowest ASCII)
# print(sorted(s))  # ['h', 'n', 'o', 'p', 't', 'y']



# # # Real-World Examples


# # # Remove duplicate words from a sentence










sentence = "this is is a test test"
words = sentence.split()
print(words)
unique = " ".join(set(words))
print(unique)


# # Check if string is palindrome
# s = "madam"
# print(s == s[::-1])  # True






