l=[]
for c in list(input()):
    if c=='>':c='a';
    if c=='<':c='c'
    if c=='+':c='e'
    if c=='-':c='i'
    if c=='.':c='j'
    if c==',':c='o'
    if c=='[':c='p'
    if c==']':c='s'
    l+=c;print(''.join(l))
    
