def count_lines(f):
  lines = 0
  for line in f:
    lines += 1
  return lines

if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  print(count_lines(f))
  
