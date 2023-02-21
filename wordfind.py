words = []
file = open("words.txt", "r")
for line in file:
  words.append(line.strip())

def find(s):
  discovered = []
  for word in words:
    if s in word:
      words.remove(word)
      return word