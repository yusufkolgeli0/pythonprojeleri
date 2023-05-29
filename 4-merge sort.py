
arr_test=[2,3,5,1,7,9,4,8,6,0]
def merge_sort(arr):
    if len(arr)>1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]

     
        i=0
        j=0
        k=0
        
        while i<len(left_arr) and j<len(left_arr):
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
                k+=1
            else:
                arr[k]=right_arr[j]
                j+=1
                k+=1    
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1



merge_sort(arr_test)
print(arr_test)

