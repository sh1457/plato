with open('P14.txt', 'r') as pfile:
  fields = pfile.read().split('|')
for i in range(0, len(fields), 5):
  print("%s %s %s %s %s" % (fields[i], fields[i+1], fields[i+2], fields[i+3], fields[i+4]))