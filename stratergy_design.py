
# def binary_Search(arr:list[int], num):
#     low = 0
#     high = len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==num:
#             return mid
#         elif arr[mid]>=num:
#             high = mid-1
#         else:
#             low=mid+1
#     return -1

# def binary_Search(arr:list[int], num, low, high):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if arr[mid]==num:
#         return mid
#     if arr[mid]< num:
#         return binary_Search(arr, num, mid+1, high)
#     else:
#         return binary_Search(arr, num, low, mid-1)
# print(binary_Search(arr, 8, 0, len(arr)-1))

from abc import ABC, abstractmethod
from typing import List
import random

# ---------- Strategy Interface ----------
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        ...

# ---------- Concrete Strategies ----------
class BubbleSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        arr = data[:]  # don't mutate caller's list
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

class MergeSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        def merge_sort(a: List[int]) -> List[int]:
            if len(a) <= 1:
                return a
            mid = len(a) // 2
            left  = merge_sort(a[:mid])
            right = merge_sort(a[mid:])
            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            out, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:    # stable
                    out.append(left[i]); i += 1
                else:
                    out.append(right[j]); j += 1
            out.extend(left[i:]); out.extend(right[j:])
            return out

        return merge_sort(data[:]) # always call the method as it wil return the and start the process it is not a mroaml function but mut be called again
                                    # As here due to the abstarct method it should have only one method and then method in methods
class QuickSort(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        def qs(a: List[int]) -> List[int]:
            if len(a) <= 1:
                return a
            pivot = a[len(a)//2]
            left  = [x for x in a if x < pivot]
            mid   = [x for x in a if x == pivot]
            right = [x for x in a if x > pivot]
            return qs(left) + mid + qs(right)
        return qs(data[:])

# ---------- Strategy chooser (simple heuristic) ----------
class StrategyChooser:
    def __init__(self, data: List[int]):
        self.data = list(data)
        self.n = len(self.data)
        # "nearly sorted" signal: local inversions
        self.inversions = sum(1 for i in range(self.n - 1)
                              if self.data[i] > self.data[i + 1])

    def choose(self) -> SortingStrategy:
        if self.n <= 32:
            return BubbleSort()         # tiny inputs
        if self.inversions <= self.n * 0.02:
            return MergeSort()          # almost sorted & stable
        return QuickSort()              # general case

# ---------- Context ----------
class SortContext:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def perform(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)

# ---------- Demo ----------
arr = [random.randint(0, 100) for _ in range(50)]
chooser = StrategyChooser(arr)
strategy = chooser.choose()

ctx = SortContext(strategy)
result = ctx.perform(arr)

print("Chosen strategy:", type(strategy).__name__)
print("Original (head):", arr[:10])
print("Sorted   (head):", result[:10])

def binary_Search(arr:list[int], num, low, high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==num:
        return mid
    if arr[mid]< num:
        return binary_Search(arr, num, mid+1, high)
    else:
        return binary_Search(arr, num, low, mid-1)
print(binary_Search(result,51,0,49))



