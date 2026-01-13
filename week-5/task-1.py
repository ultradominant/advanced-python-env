import string

# Open and read the text file
with open("text1111.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count lines
line_count = len(lines)

word_count = 0
word_frequency = {}

for line in lines:
    # Ignore case
    line = line.lower()
    # Remove punctuation
    line = line.translate(str.maketrans("", "", string.punctuation))
    words = line.split()

    word_count += len(words)

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

# Write analysis to file
with open("analysis1111.txt", "w", encoding="utf-8") as file:
    file.write(f"Total lines: {line_count}\n")
    file.write(f"Total words: {word_count}\n")
    file.write("Word frequency:\n")

    for word, freq in word_frequency.items():
        file.write(f"{word}: {freq}\n")
