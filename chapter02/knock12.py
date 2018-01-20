'''
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

'''

def col(f, w_f1, w_f2):
  for lines in f:
    line = lines.strip().split()
    w_f1.write(line[0] + '\n')
    w_f2.write(line[1] + '\n')


if __name__ == '__main__':
  f = open('hightemp2.txt').readlines()
  w_f1 = open('col1.txt', 'w')
  w_f2 = open('col2.txt', 'w')
  col(f, w_f1, w_f2)
