#lang htdp/bsl

;; Predicates for checking value types
(number? 4)
(number? pi)
(number? #true)
(string? "fortytwo")
(boolean? #false)
(rational? pi)
(complex? 3+2i)

;; Some functions
(define (opening first-name last-name)
  (string-append "Dear " first-name ","))
(opening "Matthew" "Fisler")
