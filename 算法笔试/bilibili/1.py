def QuickSort(list,low,high):
    if high > low:
        k = Partitions(list,low,high)
        QuickSort(list,low,k-1)
        QuickSort(list,k+1,high)

def Partitions(list,low,high):
    left = low
    right = high
    k = list[low]
    while left < right :
        while list[left] <= k:
            left += 1
        while list[right] > k:
            right = right - 1
        if left < right:
            list[left],list[right] = list[right],list[left]
    list[low] = list[right]
    list[right] = k
    return right

list_demo = [6,1,2,7,9,3,4,5,10,8]
print(list_demo)
QuickSort(list_demo,0,9)
print(list_demo)