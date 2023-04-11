import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_val(cep):
            self._cep = cep
        else:
            raise ValueError("Cep Inválido")

    def cep_e_val(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formata_cep(self):
        return "{}.{}-{}".format(
            self._cep[:2], self._cep[2:5], self._cep[5:] 
        )
    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self._cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['uf'],
            dados['localidade'],
            dados['cep']
        )



