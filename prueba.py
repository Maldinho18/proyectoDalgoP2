

import sys

class DSU:
    __slots__ = ("p", "r")
    def __init__(self, n: int):
        self.p = list(range(n + 1))  # 1-indexed
        self.r = [0] * (n + 1)

    def find(self, a: int) -> int:
        # Path compression iterativa
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a: int, b: int) -> None:
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

    # Recorremos todos los nodos, normalizando representantes
    for v in range(1, n + 1):
        a = dsu1.find(v)
        b = dsu2.find(v)

        # Consistencia comp1 -> comp2
        prev_b = map12.get(a)
        if prev_b is None:
            map12[a] = b
        elif prev_b != b:
            return False

        # Consistencia comp2 -> comp1 (inyectividad en sentido inverso)
        prev_a = map21.get(b)
        if prev_a is None:
            map21[b] = a
        elif prev_a != a:
            return False

    return True

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    try:
        t = int(next(it))
    except StopIteration:
        return

    out = []
    write = sys.stdout.write
    flush = sys.stdout.flush

    for _ in range(t):
        n = int(next(it)); m = int(next(it))
        dsu_fibra = DSU(n)    # k = 1
        dsu_coax  = DSU(n)    # k = 2

        # Vamos imprimiendo token por token, sin esperar a terminar el caso
        for idx in range(1, m + 1):
            i = int(next(it)); j = int(next(it)); k = int(next(it))
            if k == 1:
                dsu_fibra.union(i, j)
            else:
                # Enunciado establece k=1 o k=2; tratamos cualquier otro como coaxial por robustez
                dsu_coax.union(i, j)

            # Chequeo de redundancia tras esta conexión
            redundante = es_redundante(dsu_fibra, dsu_coax, n)
            token = '1' if redundante else '0'

            if idx < m:
                write(token)
                write(' ')
                # "Va sacando los resultados": forzamos flush para visualización progresiva
                flush()
            else:
                # Último de la línea: no imprimimos espacio extra
                write(token)
                write('\n')
                flush()

if __name__ == "__main__":
    main()
