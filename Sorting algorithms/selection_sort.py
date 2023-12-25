# selection sort algorithm desc and asc
def selection_sort(numbers: int, order : str = "asc"):
    for i in range(0,len(numbers)):
        for j in range(0,i + 1):
            if order == "asc":
                if numbers[i] < numbers[j]:
                    numbers[i] , numbers[j] = numbers[j] , numbers[i]
            elif order == "desc":
                if numbers[i] > numbers[j]:
                    numbers[i] , numbers[j] = numbers[j] , numbers[i]
            else:
                raise Exception("Not valid input for order, we accept asc as ascendding order and desc as descendding order!")


# implementation
if __name__ == "__main__":
    numbers = [1, 5, 3, 6, 9, 0, 2, 7, 8]
    selection_sort(numbers, "asc")
    print(numbers)
    selection_sort(numbers, "desc")
    print(numbers)
    
    
    