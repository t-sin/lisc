#!/bin/python3

def l_read_list(s):
    list = []
    i = 0
    while True:
        if i >= len(s):
            return (list, len(s))
        c = s[i]
        if c == ')':
            return (list, i+2)
        elif c == ' ':
            i += 1
        else:
            (l, n) = l_read(s[i:])
            i += n
            list.append(l)

def l_read_symbol(s):
    name = []
    i = 0
    while True:
        if i >= len(s):
            return (''.join(name), len(s))
        c = s[i]
        if c == ' ' or c == ')':
            return (''.join(name), i)
        else:
            name.append(c)
        i += 1

def l_read(s):
    s2 = s.strip()
    if s2[0] == '(':
        return l_read_list(s2[1:])
    elif s2[0] == ')':
        raise Exception
    else:
        return l_read_symbol(s2)

env = (None, {})
env[1]['atom'] = ('lambda', None, lambda o: 't' if type(o) is not list else 'nil')
env[1]['cons'] = ('lambda', None, lambda a, b: [a, b])
env[1]['car'] = ('lambda', None, lambda l: l[0])
env[1]['cdr'] = ('lambda', None, lambda l: l[1:])
env[1]['eq'] = ('lambda', None, lambda a, b: 't' if a == b else 'nil')

def l_eval(l, env=env):
    if type(l) is list:
        if len(l) == 0:
            return 'nil'
        elif l[0] == 'if':
            return l_eval(l[2], env) if len(l) == 4 and l_eval(l[1], env) == 't'else l_eval(l[3], env)
        elif l[0] == 'quote':
            return l[1] if len(l) == 2 else '__quote_invalid_argument__'
        elif l[0] == 'lambda':
            return ('lambda', l[1], lambda new_env: l_eval(l[2], (env, new_env))) if len(l) == 3 else '__invalid_lambda_expression__'
        elif l[0] == 'define':
            env[1][l[1]] = l_eval(l[2], env)
            return env[1][l[1]] if len(l) == 3 else '__define_invalid_argument__'
        else:
            fn = l_eval(l[0], env)
            if type(fn) is tuple and fn[0] == 'lambda':
                eval_args = [l_eval(a, env) for a in l[1:]]
                if fn[1] is None:
                    return fn[2](*eval_args)
                else:
                    if len(fn[1])+1 == len(l):
                        new_env = dict(zip(fn[1], eval_args))
                        return fn[2](new_env)
                    else:
                        return '__wrong_number_of_args__'
            else:
                return '__undefined_operator__'
    elif type(l) is str:
        def _search_val(e, s):
            return ['__unbound_variable__' if e is None else v if v else _search_val(e[0], s) for v in [e[1].get(s, None)]][0]
        return _search_val(env, l)
    else:
        return '__invalid_object__'

def l_print(l):
    return '(' + ' '.join([l_print(e) for e in l]) + ')' if type(l) is list or type(l) is tuple else str(l)

if __name__ == '__main__':
    [b.append(None) or print(l_print(l_eval(l_read(input('> '))[0]))) for b in [[None]] for a in b]
