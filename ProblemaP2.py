import sys

class DSU:
    __tuplas__ = ("p", "r")
    
    def __init__(instancia, n:int):
        instancia.p = list(range(n + 1))
        instancia.r = [0] * (n + 1)
        
    def find(instancia, a: int) -> int:
        while instancia.p[a] != a:
            instancia.p[a] = instancia.p[instancia.p[a]]
            a = instancia.p[a]
        return a

    def union(instancia, a:int, b:int) -> None:
        ra, rb = instancia.find(a), instancia.find(b)
        if ra == rb:
            return 
        if instancia.r[ra] < instancia.r[rb]:
            instancia.p[ra] = rb
        elif instancia.r[ra] > instancia.r[rb]:
            instancia.p[rb] = ra
        else:
            instancia.p[rb] = ra
            instancia.r[ra] += 1
    
def es_redundante(dsu1: DSU, dsu2: DSU, n: int) -> bool:
    dict12 = {}
    dict21 = {}
    
    for v in range(1, n + 1):
        a = dsu1.find(v)
        b = dsu2.find(v)
        
        prev_b = dict12.get(a)
        if prev_b is None:
            dict12[a] = b
        elif prev_b != b:
            return False
        
        prev_a = dict21.get(b)
        if prev_a is None:
            dict21[b] = a
        elif prev_a != a:
            return False
    return True

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    
    try:
        t = int(next(it))
    except StopIteration:
        return
    
    escribir = sys.stdout.write
    seguir = sys.stdout.flush
    
    for _ in range(t):
        n = int(next(it)); m = int(next(it))
        dsu_f = DSU(n)
        dsu_c = DSU(n)

        for id in range(1, m + 1):
            i = int(next(it)); j = int(next(it)); k = int(next(it))
            if k == 1:
                dsu_f.union(i, j)
            else:
                dsu_c.union(i, j)
            
            redundante = es_redundante(dsu_f, dsu_c, n)
            token = '1' if redundante else '0'
            
            if id < m:
                escribir(token)
                escribir(' ')
                seguir()
            else:
                escribir(token)
                escribir('\n')
                seguir()
if __name__ == "__main__":
    main()
                
    
    
