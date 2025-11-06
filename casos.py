# generador_casos_P2.py
# Genera T casos para probar el proyecto DALGO P2 respetando EXACTAMENTE M líneas por caso.
# 2 ≤ N ≤ 1000, 1 ≤ M ≤ 100000

from pathlib import Path

def write_case(f, N, M, seed_base=0):
    """
    Escribe exactamente M conexiones para un caso con N nodos.
    Estrategia:
      A) Prefijo de árbol de fibra (k=1) hasta min(M, N-1)
      B) Prefijo de árbol coax (k=2) hasta completar M o 2*(N-1)
      C) Si falta, relleno alternando k=1/2 evitando i==j
    """
    span = N - 1
    written = 0

    # A) Fibra (k=1)
    takeA = min(M - written, span)
    for i in range(1, 1 + takeA):
        f.write(f"{i} {i+1} 1\n")
    written += takeA
    if written == M:
        return

    # B) Coax (k=2)
    takeB = min(M - written, span)
    for i in range(1, 1 + takeB):
        f.write(f"{i} {i+1} 2\n")
    written += takeB
    if written == M:
        return

    # C) Relleno alterno (k=1/2)
    remaining = M - written
    for t in range(remaining):
        k = 1 if (t % 2 == 0) else 2
        i = (t % N) + 1
        j = ((t * 7 + 13 + seed_base) % N) + 1
        if j == i:
            j = (j % N) + 1
        f.write(f"{i} {j} {k}\n")

def generate_file(path, T, N, M):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{T}\n")
        for t in range(T):
            f.write(f"{N} {M}\n")
            write_case(f, N, M, seed_base=t*97)

if __name__ == "__main__":
    # 👉 Ajusta estos parámetros a lo que quieras generar
    T = 1
    N = 1000
    M = 100000

    nombre_archivo = "stress_T{}_N{}_M{}.txt".format(T, N, M)
    ruta = Path(nombre_archivo)
    generate_file(ruta, T, N, M)
    print(f"✅ Generado: {ruta.resolve()}")
