def sort_custom(arr):
  n=len(arr)
  for i in range(n):
    swapped=False
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped=True
    if not swapped:
      break
arr=[5,4,2,3,8]
result=sort_custom(arr)
print(arr)
