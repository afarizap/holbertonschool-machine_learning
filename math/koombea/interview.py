inf, sup = 10, 20

def isPrime(inf, sup):
    # sacar lista de numeros
    #verificar si son divisibles solo por ellos
    new = []
    for i in range(inf, sup + 1):
        x = 0
        for n in range(2, int(i * 0.5)):
            if i % n == 0:
                x += 1
                break
        if x == 0:
            new += [i]
    return new

print(isPrime(inf, sup))
