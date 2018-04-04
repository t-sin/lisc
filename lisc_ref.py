#!/bin/python3

def _read_char(stream):
    return [(stream.pop() and None) or stream.append(-1) or (None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else c.append(stream[0][pos]) or (stream.pop() and None) or stream.append(pos+1) or (c[0], stream) for c in [[]] for pos in [stream[1]]][0]

def _peek_char(stream):
    return [(None, stream) if pos >= len(stream[0]) else (None, stream) if pos == -1 else (stream[0][pos], stream) for pos in [stream[1]]][0]

def _make_stream(s):
    return [s, 0]

def l_read_list(s):
    list = []
    while True:
        ch, _ = _peek_char(s)
        if ch is None:
            return list

        if ch == ')':
            _read_char(s)
            return list
        elif ch in [' ', '\n']:
            _read_char(s)
        else:
            list.append(l_read(s))

def l_read_symbol(s):
    name = []
    while True:
        ch, _ = _peek_char(s)
        if ch is None:
            return ''.join(name)

        if ch in [' ', '\n', ')']:
            return ''.join(name)
        else:
            _read_char(s)
            name.append(ch)

def l_read_string(s):
    chars = []
    while True:
        ch, _ = _peek_char(s)
        if ch is None:
            return ('str', ''.join(chars))

        _read_char(s)
        if ch == '"':
            return ('str', ''.join(chars))
        else:
            chars.append(ch)

def l_read(s):
    while True:
       ch, _ =  _peek_char(s)
       if ch not in [' ', '\n']: break
       _read_char(s)

    ch, _ = _peek_char(s)
    if ch is None:
        None
    elif ch == '(':
        c,_ = _read_char(s)
        return l_read_list(s)
    elif ch == '"':
        _read_char(s)
        return l_read_string(s)
    elif ch == ')':
        raise Exception
    else:
        return l_read_symbol(s)

env = (None, {})
env[1]['nil'] = []
env[1]['t'] = 't'
env[1]['atom'] = ('lambda', None, lambda o: 't' if type(o) is not list else [])
env[1]['cons'] = ('lambda', None, lambda a, b: [a] if b in ['nil', []] else [a] + b if type(b) is list else '__{}_is_not_a_list__'.format(b))
env[1]['car'] = ('lambda', None, lambda l: l[0])
env[1]['cdr'] = ('lambda', None, lambda l: l[1:] if len(l) > 1 else [])
env[1]['eq'] = ('lambda', None, lambda a, b: 't' if ('nil' in [a,b] and [] in [a,b]) or a == b else [])

env[1]['load'] = ('lambda', None, lambda s: '__invalid_filename__' if type(s) is not tuple or s[0] != 'str' else [(lambda f: f if f is None else lis.append(l_eval(f)))(l_read(stream)) or lis for stream in [_make_stream(''.join([l.replace('\n', ' ') or l for l in open(s[1])]))] for lis in [[None]] for loop in lis][0])

def l_eval(l, env=env):
    if type(l) is list:
        if len(l) == 0:
            return []
        elif l[0] == 'if':
            return l_eval(l[2], env) if len(l) == 4 and l_eval(l[1], env) == 't'else l_eval(l[3], env)
        elif l[0] == 'quote':
            return l[1] if len(l) == 2 else '__quote_invalid_argument__'
        elif l[0] == 'lambda':
            return ('lambda', l[1], lambda new_env: l_eval(l[2], (env, new_env))) if len(l) == 3 else '__invalid_lambda_expression__'
        elif l[0] == 'define':
            return env[1].update({l[1]: l_eval(l[2], env)}) or (env[1][l[1]] if len(l) == 3 else '__define_invalid_argument__')
        else:
            fn = l_eval(l[0], env)
            if type(fn) is tuple and fn[0] == 'lambda':
                eval_args = [l_eval(a, env) for a in l[1:]]
                if fn[1] is None:
                    return fn[2](*eval_args)
                else:
                    if len(fn[1])+1 == len(l):
                        return fn[2](dict(zip(fn[1], eval_args)))
                    else:
                        return '__wrong_number_of_args__'
            else:
                return '__undefined_operator__'
    elif type(l) is tuple:
        return l
    elif type(l) is str:
        def _search_val(e, s):
            return [ v if v is not None else '__unbound_variable__' if e[0] is None else _search_val(e[0], s) for v in [e[1].get(s, None)]][0]
        return _search_val(env, l)
    else:
        return '__invalid_object__'

def l_print(l):
    return 'nil' if l == [] else '(' + ' '.join([l_print(e) for e in l]) + ')' if type(l) is list else repr(l[1]) if type(l) is tuple and l[0] == 'str' else '[{}]'.format(' '.join(['<fn {}>'.format(id(e)) if callable(e) else str(e) for e in l])) if type(l) is tuple else str(l)

if __name__ == '__main__':
    [b.append(l_read(_make_stream(input('> ')))) or (print(l_print(l_eval(b[-1]))) if b[-1] is not None else b.append('')) for b in [['']] for a in b]
