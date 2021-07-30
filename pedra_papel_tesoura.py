from jogo import jogo
from desenho import desenho
from verificar import verificar
from placar import placar
import time
import random

options = ["pedra","papel","tesoura"]

messages = ["Parabéns, você ganhou!!","Sinto muito, você perdeu.", "Foi um empate."]

pontos = [0,0]

while True:

  robo = random.choice(options)

  user = (input("Escolha: pedra, papel o tesoura?\n")).lower()

  x = 0

  for i in options:
    if i == user:
      x+=1

  if x==0:
    print("ERRO! Verifique a sua escrita e tente novamente.")
  else:
    time.sleep(0.5)

    print(" _________________________________")
    print("|                                 |")
    print("| O Robo escolheu: {:^15}|".format(robo))  
    print("| Você escolheu:   {:^15}|".format(user))
    print("|_________________________________|")  

    time.sleep(1)

    print("\n\n        {} x {}\n\n".format(robo,user))

    time.sleep(1)

    print("   O Resultado é ....")

    time.sleep(2)

    result = jogo(robo,user,messages)

    print(" _________________________________")
    print("|                                 |")
    print("| {:^31} |".format(result))
    print("|_________________________________|\n\n") 

    time.sleep(0.5)

    pontos = desenho(result,pontos)

    time.sleep(1)
    
    print("\nO placar atual é: ")

    placar(pontos)

    time.sleep(1)

    b = verificar() 

    if b == True:
      print("\n\nO Placar final foi:")
      placar(pontos)

      if pontos[0]>pontos[1]:
        print("\nO robo foi o vencedor!!")
      elif pontos[1]>pontos[0]:
        print("\nVocê foi o vencedor!!")
      else:
        print("O jogo foi encerrado com um empate.")
      break
         