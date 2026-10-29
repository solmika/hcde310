
colors= ["red", "green", "blue"]
for c in colors:
    print(c.upper())
print(len(colors))

counts = {}
for word in ["cat", "dog", "cat"]:
    counts[word] = counts.get(word, 0) + 1
print(counts)

def double(n):
    return n * 2

result = double(4)