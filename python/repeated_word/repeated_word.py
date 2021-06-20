def check_if_exist (arr , word):
    for w in arr :
        if w.upper() ==word.upper() :
            return True
    return False

def repeated_word(sentence):
    all_words = sentence.split(' ')

    for i in range(len(all_words)-1):
        arr = all_words[0:i+1]
        word = arr[i]
        arr.pop()
        # print(arr)
        # print(all_words[i])
        if check_if_exist(arr,word):
            print (word)
            return word
        # print ('\n','-------','\n')


    # for i in range(len(w)-1):

    #     words = w[0:i+1]

    #     for word in words :
    #         if check_if_exist(words,word) :
    #             return word


if __name__ == "__main__" :
    w = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    print(w)



# def repeated_word(sentence):
#     sentence_arr = sentence.split(',')
#     first_sentence = sentence_arr[1].split(' ')

#     for word in first_sentence :
#         print ('--word-- :',word)
#         check = True
#         for i in sentence_arr:
#             ii = i.split(' ')
#             print ('--arr-- :',ii)
#             print ('--check--',check_if_exist(ii,word))

#             if not check_if_exist(ii,word):
#                 check = False
#         if check :
#             return word
