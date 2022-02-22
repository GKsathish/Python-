user_str = input()
words = user_str.split()
words_result = []
words_adjacent =[]
for i in range(len(words)-1):
    words_adjacent.append(sorted([words[i],words[i+1]]))
for i in range(len(words)):
    for j in range(i+2,len(words)):
        word = sorted([words[i],words[j]])
        if word not in words_result and word not in words_adjacent :
            words_result.append(word)
if words_result:
    for item in sorted(words_result):
        print(*item)
else:
    print("No Combinations")