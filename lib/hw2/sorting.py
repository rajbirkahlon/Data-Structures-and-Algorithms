# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
#import matplotlib.pyplot as plt

class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []


    def sort_init(self, N):
        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')


        #self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id


    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)):

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp


        return self.id

    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """

        for i_idx, i_item in enumerate(self.id):
            j_idx = self.id[i_idx]

            while i_idx>0 and self.id[i_idx-1] > j_idx:
                self.id[i_idx] = self.id[i_idx-1]
                i_idx = i_idx-1

            self.id[i_idx] = j_idx

        return self.id

    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """

        a = len(self.id)//2

        while a >= 1:
            for i_idx, i_item in enumerate(self.id):

                for j_idx in range(a, len(self.id)):
                    temp = self.id[j_idx]
                    k_idx = j_idx
                    while k_idx >= a and self.id[k_idx-a] > temp:
                        self.id[k_idx] = self.id[k_idx-a]
                        k_idx -= a
                    self.id[k_idx] = temp
                a //= 2

        return self.id

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        for i_idx in range(len(self.id), -1, -1):
            self.heapify(self.id, len(self.id), i_idx)
        for i in range(len(self.id)-1, 0, -1):
            self.id[i], self.id[0] = self.id[0], self.id[i]
            self.heapify(self.id, i, 0)
        return self.id

    def heapify(self, n, i):
        larg = i
        left = 2*i + 1
        right = 2*i + 1

        if left < n and self.id[i] < self.id[left]:
            larg = left

        if right < n and self.id[larg] < self.id[right]:
            larg = right

        if larg != i:
            self.id[i],self.id[larg] = self.id[larg],self.id[i]
            self.heapify(self.id, n, larg)

        return self.id

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """

        if len(self.id) > 1:

            mid = len(self.id) // 2
            L = self.id[:mid]
            R = self.id[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i_idx = 0;
            j_idx = 0;
            k_idx = 0;
            while i_idx < len(L) and j_idx < len(R):
                if L[i_idx] < R[j_idx]:
                    self.id[k_idx] = L[i_idx]
                    i_idx = i_idx + 1
                else:
                    self.id[k_idx] = R[j_idx]
                    j_idx = j_idx + 1
                k_idx = k_idx + 1

            while i_idx < len(L):
                self.id[k_idx] = L[i_idx]
                i_idx = i_idx + 1
                k_idx = k_idx + 1

            while j_idx < len(R):
                self.id[k_idx] = R[j_idx]
                j_idx = j_idx + 1
                k_idx = k_idx + 1

        return self.id


    def quick_sort(self, l, h):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """

        if l < h:
            pi = self.part(self, l, h)

            self.quicksort(self, l, pi-1)
            self.quicksort(self, pi+1, h)


        return 1


    def part(self, l, h):
        i = (l-1)
        p = self.id[h]

        for j in range(l, h):
            if self.id[j] <= p:
                i = i + 1
                self.id[i],self.id[j] = self.id[j],self.id[j]
                return(i+1)

    # this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.


    # plt.plot(set_szs, timing)
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.title('log')
    # plt.ylabel('some numbers')
    # plt.show()