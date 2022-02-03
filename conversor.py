def conversor (valor):
  metros = int(input("Informe o valor em metros: \n"))
  m = metros
  km = (m / 1000)
  hm = (m / 100)
  dam = (m / 10)
  m = m
  dm = (m * 10)
  cm = (m * 100)
  mm = (m * 1000) 
  print(f"\n{km}km - {hm}hm - {dam}dam - {m}m - {dm}dm - {cm}cm - {mm}mm")
  pergunta = input("\nDeseja continuar? [S/N]\n")
  resposta = pergunta.upper()  
  if resposta == "S":
    conversor("")
  else:
    print("\nFinalizado")


conversor("")