import re

try :
    from hashtable import Hashtable
except:
    from repeated_word.hashtable import Hashtable



def repeated_word(sentence):
    words = sentence.split()
    for w in range(len(words)):
        pattern = r'[^\w\s]'
        words[w] = re.sub(pattern,'', words[w])
    hash = Hashtable()
    for word in words :
        if hash.contains(word.upper()):
            return word
        hash.add(word,word.upper())


if __name__ == "__main__" :
    w = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    print(w)
