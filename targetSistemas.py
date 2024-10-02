#1
indice = 13
soma = 0 
k = 0

while(k<indice):
    k = k+1
    soma = soma + k

print(soma) 

#2
value = int(input())
x = 0
y = 0
z = 1
pertence = False
while(x<=value):
    if(x==value):
        pertence = True
        print("Numero pertence a sequencia")
        break
    x = y+z
    y = z
    z = x
if not pertence:
    print("Numero nao pertence a sequencia")
        
        
#3
faturamento = [6,1,2,1,10,0]
maiorValor = 0
menorValor = 1
totalFat = 0
numDiasSupMed = 0
for x in faturamento:
    if(x==0):
        faturamento.remove(0)
        continue
    totalFat += x
    
media = totalFat/len(faturamento)
for x in faturamento:
    if(x>= maiorValor):
        maiorValor = x
    elif(x<= menorValor):
        menorValor = x
    if(x>media):
        numDiasSupMed+=1
        
print(numDiasSupMed,maiorValor,menorValor,totalFat,media)

#4                                                                     
class estado:
   def __init__(self,name,fat):
       self._name = name
       self._fat = fat
   def getName(self):
       return self._name
   def getFaturamento(self):
       return self._fat
   def percentDoTotal(self, value):
       percentual = round(self._fat/value,2)
       return f"O percentual de representacao de {self._name} foi de  {percentual}%"

faturamentos = []

faturamentos.append(estado("São Paulo",67836.43 ))
faturamentos.append(estado("Rio de Janeiro",36678.66  ))
faturamentos.append(estado("Minas Gerais",29229.88 ))
faturamentos.append(estado("Espirito Santo",27165.48 ))
faturamentos.append(estado("Outros",19849.53))
totalFat = 0

for x in faturamentos:
    totalFat += x.getFaturamento()

for x in faturamentos:
    print(x.percentDoTotal(totalFat))
    
#5
palavra = "Target Sistemas"
palavra_invertida = palavra[::-1]
print(palavra_invertida)  