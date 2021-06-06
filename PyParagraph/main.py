file = open("Resources/paragraph_2.txt","rt")
data = file.read()
words_count = data.split()
sentence = data.count('.')
words_length = []

for words in words_count:
    words_length.append(len(words))

ave_words_length = sum(words_length)/len(words_count)

print("Paragraph Analysis\n")
print("---------------------------\n")
print("Approximate Word Count: " + str(len(words_count)) + "\n")
print("Approximate Sentence Count: " + str(sentence) + "\n")
print("Average Letter Count: " + str(ave_words_length) + "\n")
print("Average Sentence Length: " + str(len(words_count)/sentence) + "\n")

file = open("Analysis/PyParagraph_2.txt","w")
file.write("Paragraph Analysis\n")
file.write("---------------------------\n")
file.write("Approximate Word Count: " + str(len(words_count)) + "\n")
file.write("Approximate Sentence Count: " + str(sentence) + "\n")
file.write("Average Letter Count: " + str(ave_words_length) + "\n")
file.write("Average Sentence Length: " + str(len(words_count)/sentence) + "\n")
file.close()