#lang htdp/bsl

;; A function which extracts the first character of strings
(define (string-first s)
  (string-ref s 0))

(string-first "abc")

;; A function which extracts the last character of strings
(define (string-last s)
  (string-ref s (- (string-length s) 1)))

(string-last "abcd")

;; A function which removes the first character of a string
(define (string-rest s)
  (substring s 1 (string-length s)))

(string-rest "abcd")

;; A function that removes the last character of a string
(define (string-remove-last s)
  (substring s 0 (- (string-length s) 1)))

(string-remove-last "abcd")
