
from Acesso_cep import BuscaEndereco

cep = 72120070
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)

print(objeto_cep)
