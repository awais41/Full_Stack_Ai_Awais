statement = "Hello World"
print("Length:",len(statement)) 

statement2 = "I love python"
print("Uppercase:", statement2.upper())
print("Lowercase:", statement2.lower())

statement3 = "An Apple"
print("Character count:", statement3.count("p"))

character = "drawer" 
print("First character:", character[0])
print("Last character:", character[-1])


s = input("Enter a string")

def check_substring_ignore_case(s, sub):
    return sub.lower() in s.lower()

print(check_substring_ignore_case("Data Science", "SCIENCE"))  # True

string = "Programming"
print(string[0:5]) 

# 7 Reverse a String
str = "Python is human friendly "
print(str[-9:-1])

# 8 Replace Substring

statement = "I love python"
print("Replace:", statement.replace("python", "Pakistan"))

# 9 Split and Join

variable = "I am a student of sir shahzad"
print("Split:", variable.split())


words =  ['I', 'am', 'a', 'student', 'of', 'sir', 'shahzad']
result = " ".join(words)
print(result)

# 10

name = "  Awais  "
print("strip:", name.strip())

Intermediate Level (More Involved String Tasks)

 1 Count Vowels & Consonants



s = "Hi, Awais ! 123456"
def count_vowels_consonants(s):

 vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
           vowels += 1
        else:
            consonants += 1 

return vowels, consonants

v,c = count_vowels_consonants(s)
print(f"Vowels: {v}, Consonants: {c}")  

# 2
text = input("Enter a string")

clean = ''.join(ch.lower() for ch in text if ch.isalnum())
if clean == clean[::-1]:
 print("True")
else:
 print("False")

# 3  Title Case (Manual)

text = input("Enter a sentence: ")

words = text.split()

result = ""

for word in words:
    result += word[0].upper() + word[1:].lower() + " "

print(result.strip())

# 4 Find All Indices of a Substring (Allow Overlaps)

s = input("Enter the main string: ")
sub = input("Enter the substring: ")

indices = []

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        indices.append(i)

print(indices)


# 5 Character Frequency Dictionary
text = input("Enter a string")
freq = {}
for ch in text.lower():
    if ch != " ":
        freq[ch] = freq.get(ch,0)+1

print(freq)

# 6 Anagram Checker
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Normalize
clean1 = ''.join(ch.lower() for ch in s1 if ch.isalpha())
clean2 = ''.join(ch.lower() for ch in s2 if ch.isalpha())

if sorted(clean1) == sorted(clean2):
    print("True")
else:
    print("False")

    