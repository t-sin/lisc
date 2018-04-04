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
                (quote :if:)
                (if (eq (car form) (quote quote))
                    (car (cdr form))
                    (if (eq (car form) (quote lambda))
                        (quote :lambda:)
                        (if (eq (car form) (quote define))
                            (quote :define)
                            (quote :function-call:)))))))))
