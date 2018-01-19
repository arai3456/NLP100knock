def space(f):
  f_list = list()
  for line in f:
    line2 = line.replace('\t', ' ')
    f_list.append(line2)
  return f_list
if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  print(''.join(space(f)))

