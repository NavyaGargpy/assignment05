word_list = []

num_of_words = int(input("enter number of words you want : "))

for i in range(num_of_words):
    word = str(input("enter word : "))
    word_list.append(word)

print(word_list)


word_set = set(word_list)
for word in word_set:
    print("number of times ",word , " comes in list is ",word_list.count(word))
    