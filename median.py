def median(lst):
  lst=sorted(lst)
  length=len(lst)
  print length
  if length%2==0:
    return (lst[(length/2)-1]+lst[length/2])/2.0
  else:
    return lst[length/2]
    
print median([1,2,3,4,5,6])