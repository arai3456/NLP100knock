def cipher(s):
  s_list = list()
  for i in range(len(s)):
    if s[i].islower():
      s_ = chr(219 - ord(s[i]))
      s_list.append(s_)
    else:
      s_ = s[i]
      s_list.append(s_)
  return s_list

if __name__ == '__main__':
  s = 'Aabcxyz3'
  print(''.join(cipher(s)))
  
