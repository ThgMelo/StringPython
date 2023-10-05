endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular Expression -- RegEx
# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0987654321][0987654321][0987654321][0987654321][0987654321][-]?[0987654321][0987654321][0987654321]")
busca = padrao.search(endereco) # Retorna um objeto Match
if busca:
    cep = busca.group()
    print(cep)