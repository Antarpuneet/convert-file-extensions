import glob

list_of_files = glob.glob('./*.txt')           # create the list of file
for file_name in list_of_files:
  FI = open(file_name, 'r')
  FO = open(file_name.replace('txt', 'out'), 'w') 
  for line in FI:
    FO.write(line)

  FI.close()
  FO.close()