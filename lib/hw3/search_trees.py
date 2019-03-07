
import time
import random


class Array_Search:
    def __init__(self, array):
        self.array = array

    def init_array_search(self, val_array):
        self.array = Array_Search(val_array)

    def squential_search(self, key):

        idx = 0
        for num in self.array:
            if num == key:
                return idx
            idx = idx+1
        return False

    def bsearch(self, val):

        hi = len(self.array)
        lo = 0

        while lo <= hi:

            mid = (hi+lo)//2
            i_idx = 0

            for num in self.array:
                if self.id[mid] < val:
                    lo = mid
                if self.id[mid] > val:
                 hi = mid
                else:
                    return mid
            i_idx += 1

        return False


class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def init_bst(self, val):
        self.root = BST_Node(val)

    def insert(self, val):
        if (self.root is None):
            self.init_bst(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current.val > val:
            if current.left is None:
                current.left = BST_Node(val)
                return True
            else:
                self.insertNode(current.left, val)
        else:
            if current.right is None:
                current.right = BST_Node(val)
                return True
            else:
                self.insertNode(current.right, val)
        return False

    def bsearch(self, val):
        while(self.root):
            if self.root.data > val:
                self.root = self.root.left
            if self.root.data < val:
                self.root = self.root.right
            else:
                return self.root

        return False

    def searchNode(self, current, val):
        if current.val > val:
            self.searchNode(current.left, val)
        if current.val < val:
            self.searchNode(current.right, val)
        if current.val == val :
            return current

        return False

    def delete(self, val):
        current = self.root
        BST_Node(self.searchNode(current, val))
        self.this = None
        return False



class RBBST_Node:
    def __init__(self, val, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color


RED = True
BLACK = False


class RBBST:
    def __init__(self):
        self.root = None

    def init_rbbst(self, val, color):
        self.root = RBBST_Node(val, color)

    def is_red(self, current):
        if current is None:
            return False
        return current.color == RED

    def rotate_left(self, current):
        x = current.right
        current.right = x.left
        x.left = current
        x.color = current.color
        current.color = RED
        return x


    def rotate_right(self, current):
        x = current.left
        current.left = x.right
        x.right = current
        x.color = current.color
        current.color = RED
        return x

    def flip_colors(self, current):
        current.color = RED
        current.left.color = BLACK
        current.right.color = BLACK
        return False

    def insert(self, val):
        if (self.root is None):
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):




        return False

    def bsearch(self, val):

        return False

    def searchNode(self, current, val):

        return False

if __name__ == "__main__":


    set_sz = 10
    tut = BST()

    vals = random.sample(range(1, 100), set_sz)

    for idx in range(set_sz - 1):

        tut.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))

    tut_rb = RBBST()

    for idx in range(set_sz - 1):

        tut_rb.insert(vals[idx])

    print (tut.bsearch(vals[1]))
    print(tut.bsearch(11))