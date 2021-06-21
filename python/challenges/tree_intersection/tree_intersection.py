try:
  from tree import BinaryTree,TNode,Stack
  from hashtable import Hashtable
except:
  from challenges.tree_intersection.tree import BinaryTree,TNode,Stack
  from challenges.tree_intersection.hashtable import Hashtable


def tree_intersection(tree_1,tree_2=0):
    arr = []
    hashtable = Hashtable()
    top = tree_1.preOrder().top
    while top :
        if not hashtable.contains(top.value) :
            hashtable.add(0,top.value)
        top = top.next
    top = tree_2.preOrder().top
    while top :
        if  hashtable.contains(top.value) :
            arr.append(int(top.value))
        top = top.next
    return arr




if __name__ == "__main__":
    node1 = TNode(1)
    node1.left = TNode(2)
    node1.right = TNode(3)
    node1.right.left = TNode(5)
    node1.right.right = TNode(4)
    node1.left.right = TNode(6)
    node1.left.left = TNode(7)
    #     1
    #     |
    # --------
    # |      |
    # 2      3
    # |      |
    # ----  -----
    # |  |  |   |
    # 7  6  5   4

    binary_tree = BinaryTree(node1)
    p = tree_intersection(binary_tree)
    print (p.get('5'))
    x =[3,1,2]
    y= [2,1,3]
    print(set(x) == set(y))

print('')
