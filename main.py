from time import sleep
"""----------------------Variaveis--------------------------"""
#Processos
p1 = [1, 2, -1, -1, 1]
p2 = [2, 1, -2, 1]
p3 = [1, 1, -1, 2, 1]

#Prioridades 
pri_p1 = 2
pri_p2 = 4
pri_p3 = 1

#Variaveis globais
tipo =1
ciclo=0
#variaves confirmação
#finalizados
fim_p1 = False
fim_p2 = False
fim_p3 = False
#em processo ou não
fila_p1 = False
fila_p2 = False
fila_p3 = False
#local do vetor
i_p1 = 0
i_p2 = 0
i_p3 = 0
#tempo de espera negativo
espera_p1 = 0
espera_p2 = 0
espera_p3 = 0
#soma do vetor
soma_p1=0
soma_p2=0
soma_p3=0
for i in p1:
  if i > 0:
    soma_p1 +=i
for i in p2:
  if i > 0:
    soma_p2 +=i
for i in p3:
  if i > 0:
    soma_p3 +=i
"""-------------função-----------"""
def comparador(valor):
  if valor > 0:
    return False
  else:
    return True
def menor(valor1, valor2):
   saida= False
   if valor1 < valor2:
     saida = True
   return saida

def mudar_processo(qual):
  
  fila =''
  if tipo ==1:
    if qual == 'inicio':
       fila = 'p1'
    elif qual == 'p1':
      if fim_p2 == False:
       fila = 'p2'
      elif fim_p3 == False:
       fila= 'p3'
    elif qual == 'p2':
      
      if fim_p3 == False:
       fila = 'p3'
      elif fim_p1 == False:
       fila= 'p1'
        
    elif qual == 'p3':
      if fim_p1 == False:
       fila = 'p1'
      elif fim_p2 == False:
       fila= 'p2'
    return fila
    
  elif tipo == 2:
    if qual == "inicio":
      if soma_p1 < soma_p2:
        if pri_p1 < soma_p3:
          fila = "p1"
        else:
          fila= "p3"
      else:
        if soma_p2 < soma_p3:
          fila = "p2"
        else:
          fila= "p3"
    if qual == "p1":
      menor(soma_p2,soma_p3)
      res = menor(soma_p2,soma_p3)
      if res == True:
        if fim_p2 == False:
          fila = "p2"
        elif fim_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False:
          fila = "p3"
        elif fim_p2 == False:
          fila= "p2"    
    elif qual == "p2":
      menor(soma_p1,soma_p3)
      res = menor(soma_p1,soma_p3)
      if res == True:
        if fim_p1 == False:
          fila = "p1"
        elif fim_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False:
          fila = "p3"
        elif fim_p1 == False:
          fila= "p1"   
          
    elif qual == "p3":
      menor(soma_p1,soma_p2)
      res = menor(soma_p1,soma_p2)
      if res == True:
        if fim_p1 == False :
          fila = "p1"
        elif fim_p2 == False:
          fila= "p2"
      else:
        if fim_p2 == False:
          fila = "p2"
        elif fim_p1 == False:
          fila= "p1"   
    return fila

  elif tipo == 3:
    if qual == "inicio":
      if pri_p1 < pri_p2:
        if pri_p1 < pri_p3:
          fila = "p1"
        else:
          fila= "p3"
      else:
        if pri_p2 < pri_p3:
          fila = "p2"
        else:
          fila= "p3"
 
    if qual == "p1":
      menor(pri_p2,pri_p3)
      res = menor(pri_p2,pri_p3)

      if res == True:
        if fim_p2 == False:
          fila = "p2"
        elif fim_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False:
          fila = "p3"
        elif fim_p2 == False:
          fila= "p2"    

    elif qual == "p2":
      menor(pri_p1,pri_p3)
      res = menor(pri_p1,pri_p3)

      if res == True:
        if fim_p1 == False:
          fila = "p1"
        elif fim_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False:
          fila = "p3"
        elif fim_p1 == False:
          fila= "p1"   
          
    elif qual == "p3":
      
      menor(pri_p1,pri_p2)
      res = menor(pri_p1,pri_p2)
      if res == True:
        if fim_p1 == False:
          fila = "p1"
        elif fim_p2 == False:
          fila= "p2"
      else:
        if fim_p2 == False:
          fila = "p2"
        elif fim_p1 == False:
          fila= "p1"   
    return fila
"""--------------inicio-----------------------------------------"""
tipo = int(input('Digite 1 para fifo, 2 para sjf ou 3 para Prioridade: '))
"""---------------------------------------------------------"""
mudar_processo('inicio')
fila= mudar_processo('inicio')
while all([fim_p1, fim_p2, fim_p3]) == False :
  if fila == 'p1':
    fila_p1= True
    fila_p2 =False
    fila_p3 =False
  elif fila == 'p2':
    fila_p2= True
    fila_p1 =False
    fila_p3 =False
  elif fila == 'p3':
    fila_p3= True
    fila_p2 =False
    fila_p1 =False
  if all([fim_p2,fim_p3]):
    espera_p1=0
  if all([fim_p1,fim_p3]):
    espera_p2=0
  if all([fim_p1,fim_p2]):
    espera_p3=0
  """----------------------------------------------------------------"""
  #testar p1
  if fila_p1 == True and fim_p1 == False:
    while i_p1 < len(p1):
        print('------------')
        print('Ciclo: ',ciclo)
        print('Processo P1')
        vl= p1[i_p1]
        i_p1 += 1
        comparador(vl)
        sair = comparador(vl)
        if sair:
          print('Em Espera')
          print('Espera de: ',vl,'Unidade de tempo')
          espera_p1 -= vl
          mudar_processo('p1')
          fila =mudar_processo('p1')
          ciclo +=1
          break 
        else:
          if espera_p2 >= vl:
            espera_p2 -= vl
          else:
            espera_p2 =0
            
          if espera_p3 >= vl:
            espera_p3 -= vl
          else:
            espera_p3 =0
          print('CPU',vl,'Unidade de tempo')
          ciclo +=1
    
    if i_p1 == len(p1):
      fim_p1 = True
      print("P1 Finalizado")
      mudar_processo('p1')
      fila =mudar_processo('p1')
    
    """----------------------------------------------------------------"""
    #testar p2
  elif fila_p2 == True and fim_p2 == False:
     while i_p2 < len(p2):
      
        print('------------')
        print('Ciclo: ',ciclo)
        print('Processo P2')
        vl= p2[i_p2]
        i_p2 += 1
        comparador(vl)
        sair = comparador(vl)
        if sair:
          print('Em Espera')
          print('Espera de: ',vl,'Unidade de tempo')
          espera_p2 -= vl
          mudar_processo('p2')
          fila =mudar_processo('p2')
          ciclo +=1
          break 
        else:
          if espera_p1 >= vl:
            espera_p1 -= vl
          else:
            espera_p1 =0
            
          if espera_p2 >= vl:
            espera_p2 -= vl
          else:
            espera_p2 =0
          ciclo +=1
          print('CPU',vl,'Unidade de tempo')
    
     if i_p2 == len(p2):
       fim_p2 = True
       print("P2 Finalizado")
       mudar_processo('p2')
       fila =mudar_processo('p2')
       """-------------------------------------------------"""    
    #testar p3
  elif fila_p3 == True and fim_p3 == False:
    while i_p3 < len(p3):
        print('------------')
        print('Ciclo: ',ciclo)
        print('Processo P3')
        vl= p3[i_p3]
        i_p3 += 1
        comparador(vl)
        sair = comparador(vl)
        if sair:
          print('Em Espera')
          print('Espera de: ',vl,'Unidade de tempo')
          espera_p3 -= vl
          mudar_processo('p3')
          fila =mudar_processo('p3')
          ciclo +=1
          break 
        else:
          if espera_p1 >= vl:
            espera_p1 -= vl
          else:
            espera_p1 =0
            
          if espera_p2 >= vl:
            espera_p2 -= vl
          else:
            espera_p2 =0
          ciclo+=1
          print('CPU',vl,'Unidade de tempo')


    if i_p3 == len(p3):
       fim_p3 = True
       print("P3 Finalizado")
       mudar_processo('p3')
       fila =mudar_processo('p3')
  sleep(1)
