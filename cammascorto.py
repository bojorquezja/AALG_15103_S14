costo = [
  [9, 6, 4],
  [8, 3, 5],
  [2, 1, 7]
]

op_fb = 0
op_pd = 0

def qcam_fb(f, c):
  global op_fb
  op_fb += 1

  if f == 0 and c == 0:
    return costo[0][0]

  if f == 0:
    return costo[f][c] + qcam_fb(f, c - 1)

  if c == 0:
    return costo[f][c] + qcam_fb(f - 1, c)

  return costo[f][c] + min(qcam_fb(f - 1, c), qcam_fb(f, c - 1))


def qcam_pd(f, c, memo):
  global op_pd
  op_pd += 1

  if memo[f][c] != -1:
    return memo[f][c]

  if f == 0 and c == 0:
    memo[f][c] = costo[0][0]
  elif f == 0:
    memo[f][c] = costo[f][c] + qcam_pd(f, c - 1, memo)
  elif c == 0:
    memo[f][c] = costo[f][c] + qcam_pd(f - 1, c, memo)
  else:
    memo[f][c] = costo[f][c] + min(qcam_pd(f - 1, c, memo), qcam_pd(f, c - 1, memo))

  return memo[f][c]



n = 3
f_final, c_final = n - 1, n - 1

resultado_fb = qcam_fb(f_final, c_final)

memo = [[-1 for _ in range(n)] for _ in range(n)]

resultado_pd = qcam_pd(f_final, c_final, memo)



print(" RESULTADO:")
print(f"Costo mínimo acumulado: {resultado_pd}")


print("\n[Fuerza Bruta]")
print(f"Resultado: {resultado_fb}")
print(f"Operaciones totales: {op_fb}")

print("\n[Programación Dinámica]")
print(f"Resultado: {resultado_pd}")
print(f"Operaciones totales: {op_pd}")