"""
주어진 파일을
1. 단어별로 빈도수를 찾고
2. 빈도순 대로 정렬, 빈도가 같다면 사전식 정렬
"""

def word_count():
    wordf = open('./test.txt', 'r')
    words = wordf.read().replace('\n', ' ').split(' ')
    wordf.close()
    print(words)

    dictn = dict()
    for word in words:
        if word in dictn:
            dictn[word] += 1
        else:
            dictn[word] = 1

    # first sort. lexicographical order
    swords = sorted(dictn.items())  # list of sorted words
    # second sort. frequency order (most to least)
    swords = sorted(swords, key=lambda x: x[1], reverse=True)

    for word in swords:
        print(word)


word_count()
