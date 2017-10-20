# • Vypiš prvních n členů Fibonacciho posloupnosti (1,1,2,3,5,8,13,21,...).
# f(n+2) = f(n) + f(n+1).

n = int(input("Kolik cisel z Fibonacciho posloupnosti mam vypsat?: "))
prvniclen = 1
dalsiclen = 1
print(prvniclen, end = "")

for fibonacci in range(n):
    dalsiclen = prvniclen + dalsiclen
    print(dalsiclen)
