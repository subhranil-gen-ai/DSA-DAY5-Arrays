def insertion_sort(arr):
  n=len(arr)
  for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
      arr[j+1]=arr[j]
      j -= 1
    arr[j+1]=key
  return arr
arr=[2,1,4,5,9]
result=insertion_sort(arr)
print(result)
