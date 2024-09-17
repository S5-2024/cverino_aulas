def vet ():
  vetor = []
  for i in range(3):
      vetor.append(int(input("Digite um numero: ")))
  return vetor;

def inv(vetor):
  inicio = 0;
  fim = len(vetor) - 1;
  while inicio < fim:
    vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio];
    inicio += 1;
    fim -=1;
  return print("vetor Invertido: ", vetor); 

vetorfudido = vet()
inv(vetorfudido)  

#Parte 2

numero = "1,2,3,4,5"
