(define _assoc
  (lambda (item lis)
    (if (eq lis nil)
        nil
        (if (eq (car (car lis)) item)
            (car lis)
            (_assoc item (cdr lis))))))

(define _updatev
  (lambda (alist name value)
    (if (eq alist nil)
        nil
        (if (eq (car (car alist)) name)
            (cons (cons name (cons value nil)) (cdr alist))
            (cons (car alist) (_updatev (cdr alist) name value))))))

(define _setv
  (lambda (name value)
    ((lambda (pair)
       (if (eq pair nil)
           (define *env* (cons nil (cons (cons (cons name (cons value nil)) (car (cdr *env*))) nil)))
           (define *env* (cons nil (cons (_updatev (car (cdr *env*)) name value) nil)))))
     (_assoc name (car (cdr *env*))))))

(define _lookup
  (lambda (name env)
    ((lambda (pair)
       (if (eq pair nil)
           (if (eq (car env) nil)
               (quote :unbound:)
               (_lookup name (car cdr env)))
           (car (cdr pair))))
     (_assoc name (car (cdr env))))))

(define _bind
  (lambda (fn-args act-args env)
    (if (eq fn-args nil)
        nil
        (if (eq act-args nil)
            :too-few-args:
            (cons (cons (car fn-args (cons (_eval (car act-args) env) nil)) nil)
                  (_bind (cdr fn-args) (cdr act-args) env))))))

(define *env* (quote (nil nil)))

(define _eval
  (lambda (form env)
    (if (atom form)
        (if (eq form nil)
            nil
            (if (eq form t)
                form
                (_lookup form env)))
        (if (eq (cdr form) nil)
            nil
            (if (eq (car form) (quote if))
                (if (_eval (car (cdr form)) env)
                    (_eval (car (cdr (cdr form))) env)
                    (_eval (car (cdr (cdr (cdr form)))) env))
                (if (eq (car form) (quote quote))
                    (car (cdr form))
                    (if (eq (car form) (quote lambda))
                        (cons (quote :lambda:) (cons (car (cdr form)) (cons (car (cdr (cdr form))) nil)))
                        (if (eq (car form) (quote define))
                            (_setv (car (cdr form)) (_eval (car (cdr (cdr form))) env))
                            ((lambda (fn)
                               (_eval (car (cdr (cdr fn))) (cons env (cons (_bind (car (cdr fn)) (car (cdr form))) nil))))
                             (_lookup (car form) env))))))))))

(define eval
  (lambda (form) (_eval form *env*)))
