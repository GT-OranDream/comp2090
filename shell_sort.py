def shell_sort(arr):
   
    arr = arr.copy()
    n = len(arr)
   
    gap = n // 2

  
    while gap > 0:
    
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
       
        gap = gap // 2

    return arr


# text
if __name__ == "__main__":
    data = [9, 5, 1, 4, 3, 8, 2, 7, 6]
    print("first:", data)
    result = shell_sort(data)
    print("now:", result)