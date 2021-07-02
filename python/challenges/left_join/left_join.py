from re import I
#

try :
    from hashtable import Hashtable
except:
    from challenges.left_join.hashtable import Hashtable

def left_join(hash_1,hash_2):
    arr = []
    for item in hash_1.get_data():
        if item :
            arr.append(item.head.data)
    for item in arr:
        key = item[0]
        if hash_2.contains(key):
            item.append(hash_2.get(key))
        else:
            item.append(None)
    return arr

if __name__ =="__main__":
    hash_1 = Hashtable(4)
    hash_1.add('key1','word1')
    hash_1.add('key2','word2')
    hash_1.add('key3','word3')
    hash_1.add('key4','word4')
    hash_1.add('key5','word5')

    hash_2 = Hashtable(4)
    hash_2.add('key1','word11')
    hash_2.add('key2','word22')
    hash_2.add('key3','word33')
    hash_2.add('key6','word66')

    r = left_join(hash_1,hash_2)
    print(r)
