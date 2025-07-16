def sort_by_absolute_value(arr):
  arr.sort(key=abs)
  return arr
arr=[-4,-1,0,3,-2]
result=sort_by_absolute_value(arr)
print(result)
