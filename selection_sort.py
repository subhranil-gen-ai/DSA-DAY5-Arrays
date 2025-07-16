def selection_sort(arr):
  n=len(arr)
  for i in range(n):
    min_index=i
    for j in range(i+1,n):
      if arr[min_index]>arr[j]:
        min_index = j
    arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr
arr=[5, 4, 3, 2, 1]
result=selection_sort(arr)
print(result)
