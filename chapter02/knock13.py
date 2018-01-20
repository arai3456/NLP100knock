'''
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

'''
def uni(w_f, txt1, txt2):
  for line1, line2 in zip(txt1, txt2):
    line1 = line1.strip()
    w_f.write('{}\t{}'.format(line1, line2))
      

if __name__ == '__main__':
  txt1 = open('col1.txt').readlines()
  txt2 = open('col2.txt').readlines()
  w_f = open('col1&2.txt', 'w')
  uni(w_f, txt1, txt2)

