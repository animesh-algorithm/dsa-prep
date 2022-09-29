str = "Shri Vaishnav Vidyapeeth Vishwavidyalaya"

vowelsCount = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in str:
    if char.lower() in vowels:
        vowelsCount = vowelsCount+1

print(vowelsCount)