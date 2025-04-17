import random # importa o módulo 'random', ele  permite gerar números aleatórios. 

numero_secreto = random.randint(1, 20) # será gerado um número aleatório entre 1 e 20.
tentativas = 0 # o desafio começara com zero tentativas.

acertou = False # ainda não começou, então iniciamos com False.

# essa mensagem aparecerá ao inicar o desafio. 
print("Bem vindo ao nosso jogo de adivinhação! 🤗")
print("Tente adivinhar um número entre 1 e 20.🧐🤭")

while not acertou: #enquanto "acertou" for False, o jogo continua (estrutura de repeticção).
    tentativa = int(input("Qual o seu palpite?"))
    #input() pede algo para o jogador digitar. 
    #int() converte o que ele digitou em número. 

    tentativas += 1 # soma 1 a quantidade de tentativas, assim contamos a quantidade de tentativas. 
    if tentativa == numero_secreto: # if significa "se"; # tentativa == numero_secreto se o número digitado for igual ao número sorteado.
        print(f"🎉🎉🎉🎉 Parabéns!!! Você acertou em {tentativas} tentativas.")
        acertou = True # muda pois o número é o sorteado.
        
    elif tentativa < numero_secreto: # elif significa "senão se" 
        print("Muito baixo, mas não desista. Tente novamente.")
    else: # else significa "caso contrário"
        print("Muito alto, mas não desista. Tente novamente.") 


