def quick_sort_words(word_list):
    # word_len_list = [len(word) for word in word_list]

    def compare_word(word1, word2):
        if(len(word1)<len(word2)):
            return -1
        elif(len(word1)>len(word2)):
            return 1
        else:
            if(word1<word2):
                return -1
            elif(word1>word2):
                return 1
            else:
                return 0

    def sort(start, end):
        #start이상 end이하
        if(start>=end):
            return

        pivot = word_list[start]
        l = start+1
        r = end

        while(l<r):

            while(compare_word(word_list[l], pivot)<0 and l<r):
                l += 1

            while(compare_word(word_list[r], pivot)>0 and l<r):
                r -= 1



            word_list[l], word_list[r] = word_list[r], word_list[l]
        
        if(compare_word(pivot, word_list[l])<0):
            word_list[start], word_list[l-1] = word_list[l-1], word_list[start]
        else:
            word_list[start], word_list[l] = word_list[l], word_list[start]

        sort(start, l-1)
        sort(l, end)

    sort(0, len(word_list)-1)
    return word_list
                
            


length = int(input())
word_list = [input() for _ in range(length)]
print("\n".join(quick_sort_words(list(set(word_list)))))