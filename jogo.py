def jogo(robo,usuario,messages):
  if robo == "pedra":
    if usuario == "papel":
      return messages[0]
    elif usuario == "tesoura":
      return messages[1]
    elif usuario == "pedra":
      return messages[2]
  elif robo == "papel":
    if usuario == "tesoura":
      return messages[0]
    elif usuario == "pedra":
      return messages[1]
    elif usuario == "papel":
      return messages[2]
  elif robo == "tesoura":
    if usuario == "pedra":
      return messages[0]
    elif usuario == "papel":
      return messages[1]
    elif usuario == "tesoura":
      return messages[2]