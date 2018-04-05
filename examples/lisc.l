(define assoc
  (lambda (item lis)
    (if (eq lis nil)
        nil
        (if (eq (car (car lis)) item)
            (car lis)
            (assoc item (cdr lis))))))

(define updatev
  (lambda (alist name value)
    (if (eq alist nil)
        nil
        (if (eq (car (car alist)) name)
            (cons (cons name (cons value nil)) (cdr alist))
            (cons (car alist) (updatev (cdr alist) name value))))))

(define setv
  (lambda (name value)
    ((lambda (pair)
       (if (eq pair nil)
           (define *env* (cons nil (cons (cons (cons name (cons value nil)) (car (cdr *env*))) nil)))
           (define *env* (cons nil (cons (updatev (car (cdr *env*)) name value) nil)))))
     (assoc name (car (cdr *env*))))))

(define *env* (quote (nil nil)))

(define eval
  (lambda (form env)
    (if (atom form)
        (if (eq form nil)
            nil
            (if (eq (car form) t)
                   (car form)
                   (car (assoc form env))))
        (if (eq (cdr form) nil)
            nil
            (if (eq (car form) (quote if))
                (if (eval (car (cdr form)) env)
                    (eval (car (cdr (cdr form))) env)
                    (eval (car (cdr (cdr (cdr form)))) env))
                (if (eq (car form) (quote quote))
                    (car (cdr form))
                    (if (eq (car form) (quote lambda))
                        (cons (quote :lambda:) (cons (car (cdr form)) (cons (car (cdr (cdr form))) nil)))
                        (if (eq (car form) (quote define))
                            (setv (car (cdr form)) (eval (car (cdr (cdr form))) env))
                            (quote :function-call:)))))))))
