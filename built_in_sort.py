def built_in_sort(arr):
  arr.sort()
  return arr
def built_in_new_sort(arr):
  return sorted(arr)
arr=[5, 4, 3, 2, 1]
result1=built_in_sort(arr)
result2= built_in_new_sort(arr)
print(result1)
print(result2)
