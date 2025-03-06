string = input("Enter the sentences : ")
words= string.split()
word_counts={}
stopwords = {"the", "is", "of", "like", "it", "has", "to", "a", "an", "on", "in", "for", "and", "at", "by"}
for word in words:
    if word not in stopwords:
        word_counts[word] = word_counts.get(word, 0)+1

most_repeated_value = max(word_counts,key=word_counts.get)
print(most_repeated_value )
