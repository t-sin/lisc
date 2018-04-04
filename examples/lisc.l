(define assoc
  (lambda (item lis)
    (if (eq lis nil)
        nil
        (if (eq (car (car lis)) item)
            (car lis)
            (assoc item (cdr lis))))))

(define env (quote (nil nil)))

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
                            (quote :define)
                            (quote :function-call:)))))))))
