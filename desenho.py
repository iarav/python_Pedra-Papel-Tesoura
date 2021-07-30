def desenho(result,pontos):
  if result == "Parabéns, você ganhou!!":
    print("         VOCÊ")
    print("  ROBO   _____")
    print(" _______|     |")
    print("|   2   |  1  |")
    print("|_______|_____|")
    pontos[1] += 1
  elif result == "Sinto muito, você perdeu.":
    print("         ROBO")
    print("  VOCÊ   _____")
    print(" _______|     |")
    print("|   2   |  1  |")
    print("|_______|_____|")
    pontos[0] += 1
  elif result == "Foi um empate.":
    print("  VOCÊ    ROBO")
    print(" _______________")
    print("|   1   |   1   |")
    print("|_______|_______|")

  return pontos