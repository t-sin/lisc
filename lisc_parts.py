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

# constants and functions
env = (None, {})
env[1]['nil'] = []
env[1]['t'] = 't'
env[1]['atom'] = ('lambda', None, lambda o: 't' if type(o) is not list else [])
env[1]['cons'] = ('lambda', None, lambda a, b: [a] if b in ['nil', []] else [a] + b if type(b) is list else '__{}_is_not_a_list__'.format(b))
env[1]['car'] = ('lambda', None, lambda l: l[0])
env[1]['cdr'] = ('lambda', None, lambda l: l[1:] if len(l) > 1 else [])
env[1]['eq'] = ('lambda', None, lambda a, b: 't' if ('nil' in [a,b] and [] in [a,b]) or a == b else [])

# evaluator
def l_eval(l, env=env):
    return ('nil' if len(l) == 0 else (l_eval(l[2], env) if len(l) == 4 and l_eval(l[1], env) == 't' else l_eval(l[3], env)) if l[0] == 'if' else (l[1] if len(l) == 2 else '__quote_invalid_argument__') if l[0] == 'quote' else (('lambda', l[1], lambda new_env: l_eval(l[2], (env, new_env))) if len(l) == 3 else '__invalid_lambda_expression__') if l[0] == 'lambda' else (env[1].update({l[1]: l_eval(l[2], env)}) or (env[1][l[1]] if len(l) == 3 else '__define_invalid_argument__')) if l[0] == 'define' else [[fn[2](*eval_args) if fn[1] is None else fn[2](dict(zip(fn[1], eval_args))) if len(fn[1])+1 == len(l) else '__wrong_number_of_args__' for eval_args in [[l_eval(a, env) for a in l[1:]]]][0] if type(fn) is tuple and fn[0] == 'lambda' else '__undefined_operator__' for fn in [l_eval(l[0], env)]][0]) if type(l) is list else [search_val(env, l) for _ in [None] for search_val in [lambda e, s: [v if v is not None else '__unbound_variable__' if e[0] is None else search_val(e[0], s) for v in [e[1].get(s, None)]][0]]][0] if type(l) is str else '__invalid_object__'

# printer
def l_print(l):
    return 'nil' if l == [] else '(' + ' '.join([l_print(e) for e in l]) + ')' if type(l) is list else '[{}]'.format(' '.join([str(e) for e in l])) if type(l) is tuple else str(l)

if __name__ == '__main__':
    [b.append(None) or print(l_print(l_eval(l_read(_make_stream(input('> ')))))) for b in [[None]] for a in b]
