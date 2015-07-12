def Formato(path):
  try:  
    output = open('Output', 'w')
    n = 0
  
    with open(path) as Data:    
        for num, line in enumerate(Data, 1):            
            if line == 'aprobado\n'or line == 'no aprobado\n': n = num + 1
            if num == 4:
                nombre = line.split('  ')
                nombre = ' '.join(nombre)
                output.write(nombre)
            elif num == 16:
                pregrado = line[8].upper() + line[9:]
                output.write(pregrado)
            if n != 0 and num == n:
                out = line[1:].split('\t')
                out = ' '.join(out)
                output.write(out)
  
    Data.close()
    output.close()
    
    return True
  except:
    return False
    
def Importar(path):
   
  codigos = []
  asignaturas = []
  creditos = []
  notas = []
  n = []
  
  with open(path) as Data:    
      for num, line in enumerate(Data, 1):
          if num == 1: nombre = line[:len(line) - 1]
          elif num == 2: pregrado = line[:len(line) - 1]
          else:
              l = line.split(' ')
              c = l[0].split('-')
              codigos.append(c[0])
              notas.append(l[len(l) - 1][:len(l[len(l) - 1]) - 1])                                   
              creditos.append(int(l[len(l) - 4]))
              n.append(int(l[len(l) - 3]))
              s = ' '.join(l[1:len(l) - 8])
              asignaturas.append(s)
                
  Data.close()                
  return nombre, pregrado, codigos, asignaturas, creditos, n, notas
   
def PAPA(creditos, notas):
  pond = 0
  s_creditos = 0
  for i in range(0, len(notas)):
      if notas[i] != 'AP':
          pond += (float(notas[i]) * creditos[i])
          s_creditos += creditos[i]
  
  return round(pond / s_creditos, 4)
    
def Promedio(codigos, creditos, n, notas):
  blacklist = []
  suma = 0
  s_creditos = 0
  for i in range(len(n) - 1, 0, -1):
      if n[i] > 1:
          for j in range(i - 1, 0, -1):
              if codigos[i] == codigos[j]:
                  blacklist.append(j)
                  break
                    
  for i in range(0, len(notas)):
      if notas[i] != 'AP':
          if i not in blacklist:
              suma += (float(notas[i]) * creditos[i])
              s_creditos += creditos[i]
    
  return round(suma / s_creditos, 4)
    
def Proyectar(creditos, n_creditos, notas, proy_notas):
  for i in range(0, len(n_creditos)):
      creditos.append(n_creditos[i])
      notas.append(str(proy_notas[i]))      

  return PAPA(creditos, notas)
