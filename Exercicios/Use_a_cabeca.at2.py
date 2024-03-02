import random
verbos = ['É','Será','Não é']
adjetivos = ['Alto','Pardo','Bonito(a)']
substantivos = ['Rafa','Meire','João']
verbo = random.choice(verbos)
adjetivo = random.choice(adjetivos)
substantivo = random.choice(substantivos)
frase = substantivo +' '+ verbo +' '+ adjetivo
print(frase)
