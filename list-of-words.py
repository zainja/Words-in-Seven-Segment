import re

dictionary = open("words.txt")
result = open("result.txt", "w")
words = dictionary.read()
words = words.split("\n")
pattern = re.compile("[A-Za-z]*[gkmqvwxzio]+[A-Za-z]*")
print(pattern.match("dite"))
longest_word = ""
list_of_longest = []
for word in words:
    if pattern.match(word):
        continue
    result.write(word)
    result.write("\n")
    if len(word) >= len(longest_word):
        longest_word = word
print(longest_word)
dictionary.close()
result.close()
result = open("result.txt")
for word in result.read().split("\n"):
    if len(word) == len(longest_word):
        list_of_longest.append(word)

for word in list_of_longest:
    print(word)