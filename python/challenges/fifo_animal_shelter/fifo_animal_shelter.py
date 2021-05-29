class Animal :
    def __init__(self,type):
        self.type = type
        self.next = None

class  AnimalShelter :
    def __init__ (self):
        self.front = None
        self.rare = None

    def enqueue(self,animal):
        if animal == 'dog' or animal == 'cat' :
            dog_cat = Animal(animal)
            if self.front == None :
                self.front = dog_cat
                self.rare = dog_cat
            else :
                self.rare.next = dog_cat
                self.rare = dog_cat

    def dequeue(self,pref):
        # **********************  Dogs ******************************
        if pref == 'dog' :
            first = self.front
            pre = first
            if first.type == 'dog' :
                if self.front :
                    if not self.front.next :
                        temp = self.front
                        self.front = None
                        temp.next = None
                        return temp.type

                temp = self.front
                self.front = self.front.next
                temp.next = None
                return temp.type

            while first :
                if first.type == 'dog' :
                    if self.rare != first :
                        pre.next = pre.next.next
                        first.next = None
                    else :
                        self.rare = pre
                        pre.next = None
                    return 'dog'
                pre = first
                first = first.next
            return 'No dogs in the shelter'

        # **********************  Cats ******************************

        if pref == 'cat' :
            first = self.front
            pre = first
            if first.type == 'cat' :
                if self.front :
                    if not self.front.next :
                        temp = self.front
                        self.front = None
                        temp.next = None
                        return temp.type

                temp = self.front
                self.front = self.front.next
                temp.next = None
                return temp.type

            while first :
                if first.type == 'cat' :
                    if self.rare != first :
                        pre.next = pre.next.next
                        first.next = None
                    else :
                        self.rare = pre
                        pre.next = None
                    return 'cat'
                pre = first
                first = first.next
            return 'No cats in the shelter'

        # ****************************************************

        return 'The Animal Shelter contain just dogs and cats'

    def __str__ (self):
        text = ''
        node = self.front
        while node :
            text = text +' - ' + node.type
            node = node.next
        return text


# dogCat = AnimalShelter()
# dogCat.enqueue('dog')
# dogCat.enqueue('dog')
# dogCat.enqueue('dog')
# dogCat.enqueue('cat')
# dogCat.enqueue('cat')
# dogCat.enqueue('dog')
# dogCat.enqueue('cat')
# dogCat.enqueue('cat')
# print (dogCat)

# dogCat.dequeue('dog')
# print (dogCat)

# dogCat.dequeue('dog')
# print (dogCat)
# dogCat.dequeue('cat')
# print (dogCat)

# print('ok')
