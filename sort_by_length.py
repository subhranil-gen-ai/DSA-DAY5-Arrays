def sort_by_length(arr):
  arr.sort(key=len)
  return arr
arr=['apple','banana','dog','king']
result=sort_by_length(arr)
print(result)
