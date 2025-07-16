def sort_descending_manually_sel_sort(arr):
  n=len(arr)
  for i in range(n):
    max_index=i
    for j in range(i+1,n):
      if arr[max_index]<arr[j]:
        max_index=j
    arr[i],arr[max_index]=arr[max_index],arr[i]
    return arr
arr=[6,7,4,8,2]
result=sort_descending_manually_sel_sort(arr)
print(result)
