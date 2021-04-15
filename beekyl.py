# ./p> raddish
import time as tm
p = '/ '
print('--- beekyl --- \n')
print('--- a delicious text editor --- \n')
print(p + 'what should we call this file?')
fname = input()
print('what kind of file is this? (type the extension ex: .py)')
f = open(fname + ext, 'a')
print(p + 'succesfully opened ' + fname + ext)
print('--- continue with file writing --- \n')
w = ''
while w != '/ end;':
  w = input()
  if w == '/ end;':
    print(p + 'saving file... \n')
    f.close()
  try:
    f.write(w + '\n')
  except:
    print('saved.')
  finally:
    print('')
