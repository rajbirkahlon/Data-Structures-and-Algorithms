
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
                if self.id[mid] == val:
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
            print("Inserted at root: ", val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current.val > val:
            if current.left is None:
                current.left = BST_Node(val)
                print("Inserted to left: ", val)
                return True
            else:
                self.insertNode(current.left, val)
        else:
            if current.right is None:
                current.right = BST_Node(val)
                print("Inserted to right: ", val)
                return True
            else:
                self.insertNode(current.right, val)
        return False

    def bsearch(self, val):
        if self.root is None:
            return False
        x = self.root
        while x is not None:
            if x.val > val:
                x = x.left
                print("It is less than ")
            if x.val < val:
                x = x.right
            if x.val == val:
                return idx
        return False

    def searchNode(self, current, val):
        while(current != None):
            if current.val > val:
                self.searchNode(current.left, val)
            if current.val < val:
                self.searchNode(current.right, val)
            if current.val == val:
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
        print("Inserted to root!!!", val)

    def is_red(self, current):
        if current is None:
            return BLACK
        return current.color == RED

    def rotate_left(self, current):
        if current.right is None:
            return
        x = current.right
        #x = RBBST_Node(current.right.val, current.right.color)
        current.right = x.left
        x.left = current
        x.color = current.color
        current.color = RED
        return x


    def rotate_right(self, current):
        x = current.left
        #x = RBBST_Node(current.left.val, current.left.color)
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
        if self.root is None:
            self.init_rbbst(val, RED)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, current, val):
        if current.val > val:
            if current.left is None:
                current.left = RBBST_Node(val, RED)
                print("Inserted to left!!!", val)
                self.check_balance(current)
                print("Balanced\n")
                return True
            else:
                self.insertNode(current.left, val)
        else:
            if current.right is None:
                current.right = RBBST_Node(val, RED)
                print("Inserted to right!!!", val)
                self.check_balance(current)
                print("Balanced\n")
                return True
            else:
                self.insertNode(current.right, val)
        return False

    def check_balance(self,x):
        a = self.root
        if a.right is not None and a.right.color == RED and a.left is None:
            a = self.rotate_left(a)
            print("ROOT rotated left\n")
        if a.right is not None and a.left is not None and a.right.color == RED and a.left.color == BLACK:
            a = self.rotate_left(a)
            print("ROOT rotated left\n")
        if a.left is not None and a.left.left is not None and a.left.color == RED and a.left.left.color == RED:
            a = self.rotate_left(a)
            print("ROOT rotated right\n")
        if a.left and a.right and a.right.color == RED and a.left.color == RED:
            a = self.flip_colors(a)
            print("ROOT flipped\n")


        if self.root.right is not None:
            a = self.root.right
            if a.right and a.right.color == RED and a.left is None:
                a = self.rotate_left(a)
                print("R rotated left\n")
            if a.right and a.left and a.right.color == RED and a.left.color == BLACK:
                a = self.rotate_left(a)
                print("R rotated left\n")
            if a.left and a.left.left and a.left.color == RED and a.left.left.color == RED:
                a = self.rotate_left(a)
                print("R rotated right\n")
            if a.left and a.right and a.right.color == RED and a.left.color == RED:
                a = self.flip_colors(a)
                print("R flipped\n")

        if self.root.left is not None:
            a = self.root.left
            if a.right and a.right.color == RED and a.left is None:
                a = self.rotate_left(a)
                print("L rotated left\n")
            if a.right and a.left and a.right.color == RED and a.left.color == BLACK:
                a = self.rotate_left(a)
                print("L rotated left\n")
            if a.left and a.left.left and a.left.color == RED and a.left.left.color == RED:
                a = self.rotate_left(a)
                print("L rotated right\n")
            if a.left and a.right and a.right.color == RED and a.left.color == RED:
                a = self.flip_colors(a)
                print("L flipped\n")

        a = self.root
        if a.right and a.right.color == RED and a.left is None:
            a = self.rotate_left(a)
            print("ROOT rotated left\n")
        if a.right and a.left and a.right.color == RED and a.left.color == BLACK:
            a = self.rotate_left(a)
            print("ROOT rotated left\n")
        if a.left and a.left.left and a.left.color == RED and a.left.left.color == RED:
            a = self.rotate_left(a)
            print("ROOT rotated right\n")
        if a.left and a.right and a.right.color == RED and a.left.color == RED:
            a = self.flip_colors(a)
            print("ROOT flipped\n")

        if self.root.right is not None:
            a = self.root.right
            if a.right and a.right.color == RED and a.left is None:
                a = self.rotate_left(a)
                print("R rotated left\n")
            if a.right and a.left and a.right.color == RED and a.left.color == BLACK:
                a = self.rotate_left(a)
                print("R rotated left\n")
            if a.left and a.left.left and a.left.color == RED and a.left.left.color == RED:
                a = self.rotate_left(a)
                print("R rotated right\n")
            if a.left and a.right and a.right.color == RED and a.left.color == RED:
                a = self.flip_colors(a)
                print("R flipped\n")

        if self.root.left is not None:
            a = self.root.left
            if a.right and a.right.color == RED and a.left is None:
                a = self.rotate_left(a)
                print("L rotated left\n")
            if a.right and a.left and a.right.color == RED and a.left.color == BLACK:
                a = self.rotate_left(a)
                print("L rotated left\n")
            if a.left and a.left.left and a.left.color == RED and a.left.left.color == RED:
                a = self.rotate_left(a)
                print("L rotated right\n")
            if a.left and a.right and a.right.color == RED and a.left.color == RED:
                a = self.flip_colors(a)
                print("L flipped\n")

        #if a.right and a.right.color == RED or a.left.left and a.left and a.left.left.color == a.left.color == RED:
            #self.check_balance(a)
        return

    def bsearch(self, val):
        x = self.root
        while x is not None:
            if x.val < val:
                x = x.right
                if x is None:
                    return False
            if x.val > val:
                x = x.left
                if x is None:
                    return False
            if x.val == val:
                return x
        return False

    def searchNode(self, current, val):
        while current != None:
            if current.val > val:
                self.searchNode(current.left, val)
            if current.val < val:
                self.searchNode(current.right, val)
            if current.val == val:
                return current
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