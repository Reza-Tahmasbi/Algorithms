def bubble_sort(numbers: list):
    for i in range(len(numbers)-1, 0 ,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# O(n^2)

'''
1,5,3,6,9,0,2,7,8
1,3,5,6,9,0,2,7,8
1,3,5,6,0,9,2,7,8
1,3,5,6,0,2,9,7,8
1,3,5,6,0,2,7,9,8
1,3,5,6,0,2,7,8,9
...
0,1,2,3,5,6,7,8,9

'''
# implementation
if __name__ == "__main__":
    numbers = [1, 5, 3, 6, 9, 0, 2, 7, 8]
    bubble_sort(numbers)
    print(numbers)