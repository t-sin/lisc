# LISC - LISP as a List Comprehension


> There are those who will tell you that LISP is an acronnym for LISt Processor and others who insist that it stands for Lots of Infuriantingly Silly Parenthesis.  
> --- R. Jones, C. Maynard, I. Stewart, "The Art of Lisp Programming"


Because Python's list comprehensions are Turing complete ([Japanese article](https://qiita.com/KTakahiro1729/items/c9cb757473de50652374), [the proof as implementation of brainfxxk](https://ideone.com/zrQWwa)), we can implement everything on list comprehensions, off course LISP, as you wish.

This is an implementation of LISP, and this is wrote as a Python's list comprehension.


## Requirements

- python 3.x


## How to run

```sh
$ python3 <(curl -sL https://raw.githubusercontent.com/t-sin/lisc/master/lisc.py)
```

## Examples

```lisp
> (cons (quote a) nil)
(a)
> (eq (quote a) nil)
nil
> (eq () nil)
t
> (define val (quote foo))
foo
> (if (eq val bar) (quote true) (quote false))
false
> ((lambda (a) (quote lisp)) t)
lisp
```

Reversing a list with recursion and list operation.

```lisp
> (define -reverse-rec (lambda (lis rev) (if (eq lis nil) rev (-reverse-rec (cdr lis) (cons (car lis) rev)))))
[lambda ['lis', 'rev'] <function <listcomp>.<lambda>.<locals>.<lambda> at 0x7f8052332ea0>]
> (define reverse (lambda (lis) (-reverse-rec lis nil)))
[lambda ['lis'] <function <listcomp>.<lambda>.<locals>.<lambda> at 0x7f8052356048>]
> (reverse (quote (1 2 3 4 5)))
(5 4 3 2 1)
```

LISC can run programs in file.

```lisp
$ cat examples/reverse.l
(define _reverse
  (lambda (lis rev)
    (if (eq lis nil)
        rev
        (_reverse (cdr lis) (cons (car lis) rev)))))
(define reverse
  (lambda (lis) (_reverse lis nil)))
$ python3 lisc.py
> (load "examples/reverse.l")
...
> (reverse (quote (1 2 3 4 5)))
(5 4 3 2 1)
```

...and more

## TODO

- [x] load programs from stdin/files
- [x] string type
- [ ] input/output string
- [ ] Foreign Function Interfaces against Python

## Compromises

For restriction of list comprehension, some LISC's behaviours are felt little strange.

- Conses are represented as a Python's lists
    - therefore, behaviours of `cons`, `car` and `cdr` are different from Pure LISP little a bit
    - `cons` behaves like Clojure's one
- Errors are returned as a normal value like `__*__`
    - because raising and excepting exception are statements, not expression


## Files

- [lisc.py](lisc.py) -- interpreter as a single list comprehension
- [lisc_parts.py](lisc_parts.py) -- interpreter as several parts, such as parser, evaluator, printer etc...
- [lisc_ref.py](lisc_ref.py) -- base and reference implementation of pure LISP


## License

LISC is licensed under the GNU General Public License version 3.
