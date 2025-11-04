from unsorted_array import UnsortedArray
from sorted_array import SortedArray
from dynamic_array import DynamicArray
from dynamic_sorted_array import DynamicSortedArray

def main():
    dynamic_list = DynamicSortedArray()
    dynamic_list.insert(3)
    dynamic_list.insert(5)
    dynamic_list.insert(6)
    dynamic_list.insert(1)
    dynamic_list.insert(2)
    dynamic_list.insert(4)
    dynamic_list.delete(3)
    dynamic_list.delete_by_index(3)
    dynamic_list.traverse(print)
main()