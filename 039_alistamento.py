import datetime
ano_nasc = int(input("Em que ano você nasceu? "))

ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

if idade == 18:
   print ("É hora de se alistar jovem")
elif idade > 18:
    tempo = idade - 18
    if tempo == 1: ano = 'ano' 
    else: ano = 'anos'
    print  ("Compareça o mais rápido possível a junta militar de sua cidade")
    print (f"Você deveria ter se alistado a {tempo} {ano} atrás")
else: 
    tempo = 18 - idade
    if tempo == 1: ano = 'ano' 
    else: ano = 'anos'
    print   (f"Ainda falta {tempo} {ano} para que você possa se alistar")




