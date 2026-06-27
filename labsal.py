op_fb = 0
op_pd = 0

def qcam_fb(f, c, n):
    global op_fb
    op_fb += 1

    if f == n - 1 and c == n - 1:
        return 1

    if f == n - 1:
        return qcam_fb(f, c + 1, n)

    if c == n - 1:
        return qcam_fb(f + 1, c, n)

    return qcam_fb(f, c + 1, n) + qcam_fb(f + 1, c, n)


def qcam_pd(f, c, n, memo):
    global op_pd
    op_pd += 1

    if memo[f][c] != -1:
        return memo[f][c]

    if f == n - 1 and c == n - 1:
        memo[f][c] = 1
    elif f == n - 1:
        memo[f][c] = qcam_pd(f, c + 1, n, memo)
    elif c == n - 1:
        memo[f][c] = qcam_pd(f + 1, c, n, memo)
    else:
        memo[f][c] = qcam_pd(f, c + 1, n, memo) + qcam_pd(f + 1, c, n, memo)

    return memo[f][c]


n = int(input("Ingrese n: "))

resultado_fb = qcam_fb(0, 0, n)

memo = [[-1 for _ in range(n)] for _ in range(n)]
resultado_pd = qcam_pd(0, 0, n, memo)

print("Cantidad de caminos:", resultado_fb)

print("\nFuerza Bruta")
print("Resultado:", resultado_fb)
print("Operaciones:", op_fb)

print("\nProgramación Dinámica")
print("Resultado:", resultado_pd)
print("Operaciones:", op_pd)