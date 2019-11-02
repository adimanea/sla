#lang htdp/bsl
(require 2htdp/batch-io)

;; Conversion from Celsius to Fahrenheit
(define (C f)
  (* 5/9 (- f 32)))

;; Write this in a file
(define (convert in out)
  (write-file out
              (string-append
               (number->string
                (C
                 (string->number
                  (read-file in))))
              "\n")))

(write-file "sample.dat" "212")     ;; write 212 in sample.dat
(convert "sample.dat" 'stdout)      ;; print the CONVERTED contents of sample.dat to STDOUT
(convert "sample.dat" "out.dat")    ;; copy sample.dat to out.dat
(read-file "out.dat")               ;; write the contents of out.dat
