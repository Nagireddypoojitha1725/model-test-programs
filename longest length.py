def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
n=int(input("enter the elements in list"))
element1=str(input())
element2=str(input())
element3=str(input())
element4=str(input())
result = find_longest_word(['apple','ball','cat','dinosaur'])
print("\nLongest word: ",result)
print("Length of the longest word: ",result[0])
