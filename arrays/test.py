from unsorted_array import UnsortedArray

def main():
    unsorted_list = UnsortedArray(6)
    unsorted_list.insert(-1)
    unsorted_list.insert(2)
    unsorted_list.insert(-3)
    unsorted_list.insert(-4)
    unsorted_list.insert(-5)
    unsorted_list.insert(6)
    print(unsorted_list.max_and_min_in_array())
    
main()