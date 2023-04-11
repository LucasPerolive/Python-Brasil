import re

class Telefone:
    def __init__(self, numero):
        if self.valida(numero):
            self._numero = numero
        else:
            raise ValueError("Número inválido")
    
    def valida(self, numero):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,numero)
        if resposta:
            return True
        else:
            return False

    def formata(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self._numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        print(numero_formatado)
