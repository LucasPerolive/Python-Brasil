from Acesso_cep import BuscaEndereco
from TelefonesBr import Telefone
from cpf_cnpj import Documento
from DatasBr import Datas

opcao = int(input(''' 
1 - Cep
2 - Telefone
3 - CPf / CNPJ
4 - Salvar data atual
Digite o número da opção desajada: '''))

match opcao:
    case 1:
        cep = int(input("\nDigite o CEP: "))
        objeto_cep = BuscaEndereco(cep)
        uf, localidade, cep = objeto_cep.acessa_via_cep()
        print(f"\n{uf}, {localidade}, {cep}")

    case 2:
        telefone = input("\nDigite o Telefone: ")
        objeto_telefone = Telefone(telefone)
        print(f"\n{objeto_telefone.formata()}")

    case 3:
        documento = input("\nDigite o CPF/CNPJ: ")
        doc = Documento()
        print(f"\n{doc.cria_documento(documento)}")
    
    case 4:
        data = Datas()
        print(f'''\nAno: {data.ano_cadastro()},
Mês: {data.mes_cadastro()},
Dia: {data.dia_cadastro()},
Dia da semana: {data.dia_semana()},
Data: {data.formata_data()},
Tempo: {data.tempo_cadastro()}''')
