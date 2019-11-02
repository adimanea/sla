#lang htdp/bsl

;; Testing
(check-expect (sales-tax 20) 0)
(check-expect (sales-tax 10000) 800)

(define (sales-tax price)
  (cond
    [(and (<= 0 price) (< price 1000)) 0]
    [(> price 10000)
        (* price 0.08)]
    [else (* price 0.05)]))

(sales-tax 5000)
(sales-tax 100)
