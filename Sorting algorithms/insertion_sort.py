def insertion_sort(numbers: list):
    for i in range(1, len(numbers)):
        cv = numbers[i]
        p = i
        while p>0 and numbers[p-1] > cv:
            numbers[p] = numbers[p-1]
            p - 1
        numbers[p] = cv
        
# O(n^2)
    
# implementation
if __name__ == "__main__":
    numbers = [1, 5, 3, 6, 9, 0, 2, 7, 8]
    insertion_sort(numbers)
    print(numbers)