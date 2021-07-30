import time

def verificar():
  while True: 
    b = False
    resposta = (input("\n\nQuer jogar de novo? Digite S ou N: ")).lower()
    if resposta == "n":
      time.sleep(0.5)
      print("\nFim de jogo!")
      b = True
      break
    elif resposta != "s":
      print("\n\nDesculpe,não entendi.")
    else:
      break
  return b 