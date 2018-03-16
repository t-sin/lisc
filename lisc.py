#!/bin/python3

def l_read_symbol(s):
    return [(str, len(str)) for str in [l.append(''.join(n)) if c == ' ' or c == ')' else n.append(c) or l for n in [[]] for l in [[]] for c in s][0]][0][0]

def l_read(s):
    return [read_list(s[1:]) if s[0] == '(' else l_read_symbol(s) for s in [list(''.join(s).strip())] for read_list in [lambda s: [l if c == ')' else l.append(l_read(s[i:])[0]) if c != ' ' else l for l in [[]] for (i, c) in enumerate(s)][-1]]][0]
#
if __name__ == '__main__':
    print(l_read(list(input('> '))))
