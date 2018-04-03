(define _reverse
  (lambda (lis rev)
    (if (eq lis nil)
        rev
        (_reverse (cdr lis)
                  (cons (car lis) rev)))))

(define reverse
  (lambda (lis) (_reverse lis nil)))
