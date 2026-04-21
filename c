x = 1
while x < 32:
    if x >= 20:
        break
    elif x % 2 == 0 and x % 6 == 0:
        print(x)
    x += 1

for i in range(1,33):
    if i >= 20:
        break
    elif i % 2 == 0 and i % 6 == 0:
        print(i)
    
my_str = "yes"
for a in my_str:
    print(a)


# Ask the user to type a sentence
sentence = input("Type a sentence made of a few words: ")

# Initialize counters for each vowel
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Convert the sentence to lowercase to simplify comparison
sentence = sentence.lower()

# Use a for loop to count vowels
for char in sentence:
    if char == 'a':
        a_count += 1
    elif char == 'e':
        e_count += 1
    elif char == 'i':
        i_count += 1
    elif char == 'o':
        o_count += 1
    elif char == 'u':
        u_count += 1

# Print the result
print(f"Your sentence has {a_count} a, {e_count} e, {i_count} i, {o_count} o, and {u_count} u")
