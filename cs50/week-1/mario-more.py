def mario_more():
  
  try:
    n=int(input())
  except ValueError as err:
    print(err)
  
  if n > 0 and n<=8:
    height=n
    hash = "#"
    spaces = height-1
    for i in range(1, height+1): 
      print(spaces*" " + hash*i + "  " + hash*i + spaces*" ")
      spaces -= 1
  else:
    mario_more()


mario_more()
