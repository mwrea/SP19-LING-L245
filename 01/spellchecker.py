import sys
import re
IN = open('words.hist', 'r')
dict = []
for line in IN:
    word = line.split(' ')[1]
        #print(word)
    re.sub('[,.]', '', word)
    dict.append(word.strip('\n'))
#print(repr(dict))
input = sys.stdin.read()
words = input.split(' ')
output = []

for w in words:
    realw = w.strip( '[.,]' )
        #print(realw)
    if realw not in dict:
        w = '*'+w
    output.append(w)

checked = ' '.join(output)
print(checked)
