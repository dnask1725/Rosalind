
#--------------UNDERSTANDING-------------------
#Given : A positive integer n ≤ 25
#Return: The nth Fibonacci number
#I will use an iterative approach. 


fib <- function (n){
  if(n == 0) return (0)
  if (n == 1) return(1)

a <- 0
b <- 1

for (i in 2:n){
  temp <- a+b
  a <- b
  b <- temp
}
return (b)
}
n <- 6

fib(n)
