def manipulate_data(ints):
 
  if type(ints) is not list:
    return 'Only lists allowed'
 
  sum_of_positives = 0
  sum_of_negatives = 0
 
  for num in ints:
 
    if num >= 0:
      sum_of_positives += 1
    else:
      sum_of_negatives += num
 
  return [sum_of_positives, sum_of_negatives]


