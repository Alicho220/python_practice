sentence = "THis is a common intervie question"

freq = {}
for char in sentence:
    if char in freq:
        freq[char] +=1       
    else:
        freq[char] = 1

print(freq)

