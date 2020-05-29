'''
txt tokenize
'''

# IOWrapper
def lines(file):
    for l in file:
        yield l
    yield  '\n'

# generate blocks
def blocks(file):
    block=[]
    for l in lines(file):
        if l.strip():
            block.append(l)
        elif block:
            yield ''.join(block).strip()
            block=[]

