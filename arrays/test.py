from sorted_array import SortedArray

def main():
    sorted_list = SortedArray(6)
    sorted_list.insert(-1)
    sorted_list.insert(2)
    sorted_list.insert(-3)
    sorted_list.insert(-4)
    sorted_list.insert(-5)
    sorted_list.insert(6)
    sorted_list.traverse(print)
    
main()