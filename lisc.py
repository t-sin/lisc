#!/bin/python3

## streams
def _read_char(stream):
    return [(stream.pop() and None) or stream.append(-1) or (None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else c.append(stream[0][pos]) or (stream.pop() and None) or stream.append(pos+1) or (c[0], stream) for c in [[]] for pos in [stream[1]]][0]

def _peek_char(stream):
    return [(None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else (stream[0][pos], stream) for pos in [stream[1]]][0]

def _make_stream(s):
    return [s, 0]

## readers
def _read_list(stream):
    return [[(_read_char(stream) and None) or loop[1:] if _peek_char(stream)[0] == ')' else loop[1:] if _peek_char(stream)[0] == None else loop.append(l_read(stream)) for l in loop] for loop in [[None]]][0][-1]

def _read_symbol(stream):
    return ''.join([[loop if _peek_char(stream)[0] == ')' else (_read_char(stream) and None) or loop if _peek_char(stream)[0] == ' ' else loop if _peek_char(stream)[0] == None else loop.append(_read_char(stream)[0]) for l in loop] for loop in [['']]][0][-1])

def l_read(stream):
    return [[loop.append(None) or _read_char(stream) if _peek_char(stream)[0] == ' ' else None for l in loop] for loop in [[None]]] and ((_read_char(stream) and None) or _read_list(stream) if _peek_char(stream)[0] == '(' else _read_symbol(stream))

env = (None, {})
def l_eval(l, env=env):
    return l

def l_print(l):
    return '(' + ' '.join([l_print(e) for e in l]) + ')' if type(l) is list or type(l) is tuple else str(l)

if __name__ == '__main__':
    print(l_print(l_eval(l_read(_make_stream(input('> '))))))
