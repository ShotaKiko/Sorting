# TO-DO: Complete the selection_sort() function below 
def selection_sort(list):
    for i in range(0,len(list)):
        
        #Value at first index will be considered min position starting off
        min_position = i
        
        #staring with second value in list
        for p in range(i + 1, len(list)):
            if list[p] < list[min_position]:
                min_position = p
                #sets index of new minimum value
                
        hold = list[i] #holds value at index ---we are running trhough the first loop
        list[i] = list[min_position] #sets value to be minimum found as we pass through loop
        list[min_position] = hold #swaps up the value that got replaced by the found minimum
    return list




list1 = [3, 3, 16, 87, 2, 15, 2000, 1, 23, 13]

print(selection_sort(list1))

# # TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    length = len(arr)

    for i in range(0, length):

        for j in range(0, length - i - 1): #to evaluate j and adjacent// subtracting i because as you proceed through loop last value will be sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swap the values in each iteration pair

    return arr
print(bubble_sort(list1))



# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr



#Extra Practice--- Insertion sort again

def insertion_sort(li):
    for i in range(1, len(li)): # start at 1 because li[0] will never enter the loop conditions
        current_value = li[i]
        j = i

        while j > 0 and current_value < li[j - 1]:  #proceeds right to left till first index//
            li[j] = li[j-1]  #shifts to the right
            j -= 1
        li[j] = current_value  #assigns the suspended value back into the array
    return li
print(insertion_sort(list1))