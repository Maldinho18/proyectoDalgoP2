import sys

class DSU:
    __slots__ = ("p", "r")
    
    def __init__(self, n:int):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)
        
    def find(self, a: int) -> int:
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a:int, b:int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return 
        if self.r[ra] < self.r[rb]:
            self.p[ra] = rb
        elif self.r[ra] > self.r[rb]:
            self.p[rb] = ra
        else:
            self.p[rb] = ra
            self.r[ra] += 1
    
def es_redundante(dsu1: DSU, dsu2: DSU, n: int) -> bool:
    map12 = {}
    map21 = {}
    
    for v in range(1, n + 1):
        a = dsu1.find(v)
        b = dsu2.find(v)
        
        prev_b = map12.get(a)
        if prev_b is None:
            map12[a] = b
        elif prev_b != b:
            return False
        
        prev_a = map21.get(b)
        if prev_a is None:
            map21[b] = a
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
    
    out = []
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
                
    
    
