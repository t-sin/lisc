#!/bin/python3

def l_read(s):
    return [read_list(s[1:]) if s[0] == '(' else read_symbol(s) for s in [list(''.join(s).strip())] for read_list in [lambda s: [l if c == ')' else l.append(l_read(s[i:])[0]) if c != ' ' else l for l in [[]] for (i, c) in enumerate(s)][-1]] for read_symbol in [lambda s: [(str, len(str)) for str in [l.append(''.join(n)) if c == ' ' or c == ')' else n.append(c) or l for n in [[]] for l in [[]] for c in s][0]][0][0]]][0]

env = (None, {})
def l_eval(l, env=env):
    return l

def l_print(l):
    return l

if __name__ == '__main__':
    print(l_print(l_eval(l_read(list(input('> '))))))
