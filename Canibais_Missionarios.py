#Utilizarei uma estrutura que guarda:
#initial_state[0]: Número de canibais do lado esquerdo
#initial_state[1]: Número de missionários do lado esquerdo
#initial_state[2]: Número de missionários do lado direito 
#initial_state[3]: Número de canibais do lado direito
#initial_state[4]: Lado do barco 0- Esquerdo e 1- Direito 

initial_state = [3,3,0,0,0]

#Representação das possibilidades de indivíduos no barco
#(1,0)- Um missinário no barco
#(2,0)- Dois missinários no barco
#(1,1)- Um missinário e Um Canibal no barco
#(0,1)- Um canibal no barco
#(0,2)- Dois canibais no barco

possibilities = [(1,0), (1,1),(2,0), (0,2)]

border= []
visited = []

#Descolamento da Canoa
def boat_displacement(nSt, num_m=0, num_c=0):
  #garantir que não tenha mais de 2 pessoas no barco
  if(num_m + num_c) > 2:
    return
  #Saber onde as pessoas estão, para fazer o deslocamento correto
  if nSt[-1]==0:
    m_esq = 0
    c_esq = 1
    m_dir = 2
    c_dir = 3
  else:
    m_esq = 2
    c_esq = 3
    m_dir = 0
    c_dir = 1
  
  #Caso não tenha o que transportar
  if nSt[m_esq] == 0 and nSt[c_esq]==0:
    return
  #Atualize a posição do barco 
  nSt[-1] = 1 - nSt[-1]
  #Transporta os missionários
  for i in range(min(num_m,nSt[m_esq])):
    nSt[m_esq] -= 1
    nSt[m_dir] += 1
  #Transporta os canibais
  for i in range(min(num_c,nSt[c_esq])):
    nSt[c_esq] -= 1
    nSt[c_dir] += 1
    
  return nSt

def successors(initial_state):
  successors = []
  for (i,j) in possibilities:
    s = boat_displacement(initial_state[:],i,j)
    if s == None: continue
    if (s[0]<s[1] and s[0]>0) or (s[2]<s[3] and s[2]>0): continue
    if s in visited: continue
    successors.append(s)
  return successors
  
# print(successors(initial_state))

#busca em profundidade precisa de um nó adjacente não for visitado

def nodeAdjacentNotVisited(analise):
  l = successors(analise)
  if len(l)>0:
    return l[0]
  else:
    return -1 

#checa se a meta foi alcançada
def isSuccess(initial_state):
  if initial_state[2] >= 3 and initial_state[3] >= 3:
    return True
  else:
    return False 

#Busca em profundidade
def dfs(initial_state):
  border.append(initial_state)
  while len(border) != 0:
    analise = border[len(border)-1]
    if isSuccess(analise):break
    v = nodeAdjacentNotVisited(analise)
    if v == -1:
      border.pop()
    else:
      visited.append(v)
      border.append(v)
  else:
    print("Caminho não encontrado. Busca sem sucesso :(")
  return border

solucao = dfs(initial_state)
for sol in solucao:
  print(sol)
print("SUCESSO")