"""Fill out the function get_last_element(lst) which takes in a list lst
 as a parameter and prints the last element in the list. 
 The list is guaranteed to be non-empty, but there are no guarantees on its length
"""
def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """

    print(lst[-1])
def main():
    
    lastelment=get_last_element([1,2,3,4,5])
    print(lastelment)
if __name__ == '__main__':
    main()    
    
