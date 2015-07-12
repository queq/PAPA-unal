import HistAcad

# HistAcad.Formato('Data.txt')
nombre, pregrado, codigos, asignaturas, creditos, n, notas = HistAcad.Importar('Output.txt')
for i in range(0, 20):
  print HistAcad.PAPA(creditos, notas)
  if i == 8:
    creditos.pop()
    notas.pop()
# Promedio = HistAcad.Promedio(codigos, creditos, n, notas)
# print PAPA, Promedio
# Proy_PAPA = HistAcad.Proyectar(creditos, [4, 4, 4, 4, 4], notas, [5, 5, 5, 5, 5])
# print Proy_PAPA
