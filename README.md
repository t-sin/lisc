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


## Compromises

For restriction of list comprehension, some LISC's behaviours are felt little strange.

- Conses are represented as a Python's lists
    - therefore, behaviours of `cons`, `car` and `cdr` are different from Pure LISP little a bit
- Errors are returned as a normal value like '__*__'
    - because raising and excepting exception are statements, not expression


## Files

- [lisc.py](lisc.py) -- interpreter as a single list comprehension
- [lisc_parts.py](lisc_parts.py) -- interpreter as several parts, such as parser, evaluator, printer etc...
- [lisc_ref.py](lisc_ref.py) -- base and reference implementation of pure LISP


## License

LISC is licensed under the GNU General Public License version 3.
