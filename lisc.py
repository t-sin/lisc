#!/bin/python3

## streams
def _read_char(stream):
    return [(stream.pop() and None) or stream.append(-1) or (None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else c.append(stream[0][pos]) or (stream.pop() and None) or stream.append(pos+1) or (c[0], stream) for c in [[]] for pos in [stream[1]]][0]

def _peek_char(stream):
    return [(None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else (stream[0][pos], stream) for pos in [stream[1]]][0]

def _make_stream(s):
    return [([s, 0], read_char, peek_char) for read_char in [lambda stream: [(stream.pop() and None) or stream.append(-1) or (None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else c.append(stream[0][pos]) or (stream.pop() and None) or stream.append(pos+1) or (c[0], stream) for c in [[]] for pos in [stream[1]]][0]] for peek_char in [lambda stream: [(None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else (stream[0][pos], stream) for pos in [stream[1]]][0]]


def read_list(s):
    print('read-list: ',s)
    return [[clis.clear() or (l,i) if c==')' else (l,i) if c==' ' else [[clis.pop(0) for j in range(n)] and l.append(ss) or (l,i+n) for ss,n in [l_read(s[i:])]][0] for l in [[]] for i,c in clis] for clis in [list(enumerate(s))]][0][0]

def read_symbol(s):
    return [(l.append((''.join(n), len(n)-1))) or l if c == ' ' or c == ')' else n.append(c) or l for n in [[]] for l in [[]] for c in s][0][0]

def l_read(s):
    print('l_read:', s)
    return [read_list(s[1:]) if s[0] == '(' else read_symbol(s) for s in [list(''.join(s).strip())]][0]

env = (None, {})
def l_eval(l, env=env):
    return l

def l_print(l):
    return l

if __name__ == '__main__':
    print(l_print(l_eval(l_read(list(input('> '))))))
