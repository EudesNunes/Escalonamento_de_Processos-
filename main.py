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
vez_fila=0
ciclo=1
teste_entrada = True
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
espera_p1 = False
espera_p2 = False
espera_p3 = False
tm_esperap1 =0
tm_esperap2 =0
tm_esperap3 =0
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
#Se o tipo for FIFO  ordena a fila
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
    
#Se o tipo for SJF  ordena a fila
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
      res = menor(soma_p2,soma_p3)
      if res == True:
        if fim_p2 == False and espera_p2 == False:
          fila = "p2"
        elif fim_p3 == False and espera_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False and espera_p3 == False:
          fila = "p3"
        elif fim_p2 == False and espera_p2 == False:
          fila= "p2"    
    elif qual == "p2":
      res = menor(soma_p1,soma_p3)
      if res == True:
        if fim_p1 == False and espera_p1 == False:
          fila = "p1"
        elif fim_p3 == False and espera_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False and espera_p3 == False:
          fila = "p3"
        elif fim_p1 == False and espera_p1 == False:
          fila= "p1"   
          
    elif qual == "p3":
      res = menor(soma_p1,soma_p2)
      if res == True:
        if fim_p1 == False and espera_p1 == False:
          fila = "p1"
        elif fim_p2 == False and espera_p2 == False:
          fila= "p2"
      else:
        if fim_p2 == False and espera_p2 == False:
          fila = "p2"
        elif fim_p1 == False and espera_p1 == False:
          fila= "p1"   
    return fila
    
#Se o tipo for prioridade  ordena a fila
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
      res = menor(pri_p2,pri_p3)
      if res == True:
        if fim_p2 == False and espera_p2 == False:
          fila = "p2"
        elif fim_p3 == False and espera_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False and espera_p3 == False:
          fila = "p3"
        elif fim_p2 == False and espera_p2 == False:
          fila= "p2"    

    elif qual == "p2":
      res = menor(pri_p1,pri_p3)
      if res == True:
        if fim_p1 == False and espera_p1 == False:
          fila = "p1"
        elif fim_p3 == False and espera_p3 == False:
          fila= "p3"
      else:
        if fim_p3 == False and espera_p3 == False:
          fila = "p3"
        elif fim_p1 == False and espera_p1 == False:
          fila= "p1"   
          
    elif qual == "p3":
      res = menor(pri_p1,pri_p2)
      if res == True:
        if fim_p1 == False and espera_p1 == False:
          fila = "p1"
        elif fim_p2 == False and espera_p2 == False:
          fila= "p2"
      else:
        if fim_p2 == False and espera_p2 == False:
          fila = "p2"
        elif fim_p1 == False and espera_p1 == False:
          fila= "p1"   
    return fila
    
def verificar(v1,v2,v3):
  res= "Ø"
  if v1 == True and res.find('P1') == -1:
    res +=' P1'
    res=res.replace('Ø','')
  if v2 == True and res.find('P2') == -1:
    res += ' P2'
    res=res.replace('Ø','')
  if v3 == True and res.find('P3') == -1:
    res += ' P3'
    res=res.replace('Ø','')
  return res
"""--------------------inicio-----------------------------------------"""
print('Entradas:')
print('P1',p1,'Prioridade:',pri_p1)
print('P2',p2,'Prioridade:',pri_p2)
print('P3',p3,'Prioridade:',pri_p3)
print()
while teste_entrada:
  tipo = str(input('Digite 1 para FIFO, 2 para SJF ou 3 para Prioridade: '))
  if tipo == '1' or tipo == '2' or tipo == '3':
    teste_entrada= False
  else:
    print('Digite apenas 1,2 ou 3')
tipo = int(tipo)
"""---------------------------------------------------------"""

fila= mudar_processo('inicio')
#Fazer o tratamento de quem é a vez
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

  #Entrar na fila
  if all([fim_p1,fim_p2,fim_p3])== False:
    if vez_fila%3==0:
      if tm_esperap1 == 0:
        espera_p1 = False
      if tm_esperap2 == 0:
        espera_p2 = False
      if tm_esperap3 == 0:
        espera_p3 = False
      vez_fila =0
  if any([fim_p1,fim_p2,fim_p3]):
    espera_p2 = False
    espera_p3 = False
    espera_p1 = False

    
  """----------------------------------------------------------------"""
  #Processo para testar p1
  if fila_p1 == True and fim_p1 == False:
    vez_fila +=1
    while i_p1 < len(p1):
        print('---------------------------------------')
        print('Ciclo: ',ciclo)
        print('Aguardando:',verificar(fim_p1==False and fila_p1 ==False, fim_p2==False and fila_p2 ==False,fim_p3==False and fila_p3 ==False))
        print('Finalizados:',verificar(fim_p1,fim_p2,fim_p3))
        print('Em espera:',verificar(tm_esperap1 >0,tm_esperap2 >0,tm_esperap3 >0))
        print('Processo P1')
        vl= p1[i_p1]
        i_p1 += 1
        sair = comparador(vl)
        if sair:
          print('Em Espera')
          print('Espera de: ',vl,'Unidade de tempo')
          espera_p1 = True
          tm_esperap1 -= vl
          if vez_fila%3==0:
            espera_p2 = False
            espera_p3 = False
          fila =mudar_processo('p1')
          ciclo +=1
          sleep(1)
          break 
        else:
          if tm_esperap2 >= vl:
            tm_esperap2 -= vl
          else:
            tm_esperap2 =0
            
          if tm_esperap3 >= vl:
            tm_esperap3 -= vl
          else:
            tm_esperap3 =0
          print('CPU',vl,'Unidade de tempo')
          ciclo +=1
          sleep(1)
    
    if i_p1 == len(p1):
      fim_p1 = True
      print('***********************')
      print("P1 Finalizado")
      print('***********************')
      fila =mudar_processo('p1')
    
    """----------------------------------------------------------------"""
  #Processo para testar p2
  elif fila_p2 == True and fim_p2 == False:
     vez_fila +=1
     while i_p2 < len(p2):
        
        print('---------------------------------------')
        print('Ciclo: ',ciclo)
        print('Aguardando:',verificar(fim_p1==False and fila_p1 ==False, fim_p2==False and fila_p2 ==False,fim_p3==False and fila_p3 ==False))
        print('Finalizados:',verificar(fim_p1,fim_p2,fim_p3))
        print('Em espera:',verificar(tm_esperap1 >0,tm_esperap2 >0,tm_esperap3 >0))
        print('Processo P2')
        vl= p2[i_p2]
        i_p2 += 1
        sair = comparador(vl)
        if sair:
          print('Em Espera')
          print('Espera de: ',vl,'Unidade de tempo')
          espera_p2 = True
          tm_esperap2 -= vl
          if vez_fila%3==0:
            espera_p1 = False
            espera_p3 = False
          fila =mudar_processo('p2')
          ciclo +=1
          sleep(1)
          break 
        else:
          if tm_esperap1 >= vl:
            tm_esperap1 -= vl
          else:
            tm_esperap1 =0
            
          if tm_esperap3 >= vl:
            tm_esperap3 -= vl
          else:
            tm_esperap3 =0
          ciclo +=1
          print('CPU',vl,'Unidade de tempo')
          sleep(1)
    
     if i_p2 == len(p2):
       fim_p2 = True
       print('***********************')
       print("P2 Finalizado")
       print('***********************')
       fila =mudar_processo('p2')
       
       """-------------------------------------------------"""    
  #Processo para testar p3
  elif fila_p3 == True and fim_p3 == False:
    vez_fila +=1
    while i_p3 < len(p3):
        vez_fila +=1
        print('---------------------------------------')
        print('Ciclo: ',ciclo)
        print('Aguardando:',verificar(fim_p1==False and fila_p1 ==False, fim_p2==False and fila_p2 ==False,fim_p3==False and fila_p3 ==False))
        print('Finalizados:',verificar(fim_p1,fim_p2,fim_p3))
        print('Em espera:',verificar(tm_esperap1 >0,tm_esperap2 >0,tm_esperap3 >0))
        print('Processo P3')
        vl= p3[i_p3]
        i_p3 += 1
        sair = comparador(vl)
        if sair:
          print('Em Espera')
          print('Espera de: ',vl,'Unidade de tempo')
          espera_p3 = True
          tm_esperap3 -= vl
          if vez_fila%3==0:
            espera_p2 = False
            espera_p1 = False
          fila =mudar_processo('p3')
          ciclo +=1
          sleep(1)
          break 
        else:
          if tm_esperap1 >= vl:
            tm_esperap1 -= vl
          else:
            tm_esperap1 =0
            
          if tm_esperap2 >= vl:
            tm_esperap2 -= vl
          else:
            tm_esperap2 =0
          ciclo+=1
          print('CPU',vl,'Unidade de tempo')
          sleep(1)
    if i_p3 == len(p3):
       fim_p3 = True
       print('***********************')
       print("P3 Finalizado")
       print('***********************')
       fila =mudar_processo('p3')
  
print()
print("---------")
print('Finalizados:',verificar(fim_p1,fim_p2,fim_p3))
