def insertion_sort_descending(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        # Shift elements of A[0..i-1] that are less than key
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

# Test the function
if __name__ == "__main__":
    # Example array from the book
    test_array = [5, 2, 4, 66, 1, 3]
    print("Original array:", test_array)
    sorted_array = insertion_sort_descending(test_array)
    print("Sorted array (descending):", sorted_array)


    #Expected Output :
    # Original
    # array: [5, 2, 4, 66, 1, 3]
    # Sorted
    # array(descending): [66, 5, 4, 3, 2, 1]