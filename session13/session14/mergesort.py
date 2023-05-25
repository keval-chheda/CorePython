arr1 = [10,7,8,14]
arr2 = [5,6,7,9]
merged_array = []
def merge_sorted_array(arr1, arr2):
     i = 0
     j = 0

     while i < len(arr1) and j < len(arr2):
          if arr1[i] <= arr2[j]:
               merged_array.append(arr1[i])
               i+=1
          else:
               merged_array.append(arr2[j])
     while i < len(arr1):
          merged_array.append(arr1[i])
          i+=1
     while j < len(arr2):
          