;; Use the Beginning Student Language from How To Design Programs
#lang htdp/bsl
;; For image functions
(require 2htdp/image)
(require 2htdp/universe)

;; Eval with C-c C-c
(+ 1 1)     ; 2
(expt 2 3)  ; 8
(sin (angle -1))    ; (angle z) = the argument for the complex number z


;; Basic operations and examples
(string-append "hello" "world")             ; "helloworld"
(+ (string-length "hello world") 10)        ; 21
(number->string 42)                         ; "42"
(string->number "hello world")              ; #f = false
(and #t #f)                                 ; #f
(> 2 3)                                     ; #f
(string=? "design" "tinker")                ; #f
(string=? "design" "design")                ; #t
(and (or (= (string-length "hello world")
            (string->number "11"))
         (string=? "hello world" "good morning"))
     (>= (+ (string-length "hello world") 60) 80))  ; #f

;; Draw
(circle 10 "solid" "red")
(rectangle 30 20 "outline" "blue")
(overlay (circle 5 "solid" "red")
         (rectangle 20 20 "solid" "blue"))
(place-image (circle 5 "solid" "green")     ; origin = upper left corner!
             50 80                          ; place a solid green disk at (50, 80)
             (empty-scene 100 100))         ; in a 100 x 100 empty square

;; Measure images
(image-width (square 10 "solid" "red"))     ; 10
(image-width
 (overlay (rectangle 20 20 "solid" "blue")
          (circle 5 "solid" "red")))        ; 20

;; Function definitions
(define (twice x) (+ x x))                  ; C-x C-e for eval
(twice 3)

;; Conditionals
(define (sign x)
  (cond
    [(> x 0) 1]
    [(= x 0) 0]
    [(< x 0) -1]))
(sign 10)

;; Animating a rocket (last exercise)
; properties of the "world" and the descending rocket
(define WIDTH 100)
(define HEIGHT 60)
(define V 3)
(define X 50)

; graphical constants
(define MTSCN (empty-scene WIDTH HEIGHT))
(define ROCKET (circle 10 "solid" "red"))
(define ROCKET-CENTER-TO-TOP
  (- HEIGHT (/ (image-height ROCKET) 2)))

; functions
(define (picture-of-rocket.v6 t)
  (cond
    [(<= (distance t) ROCKET-CENTER-TO-TOP)
     (place-image ROCKET X (distance t) MTSCN)]
    [(> (distance t) ROCKET-CENTER-TO-TOP)
     (place-image ROCKET X ROCKET-CENTER-TO-TOP MTSCN)]))

(define (distance t)
  (* V t))

(animate picture-of-rocket.v6)
