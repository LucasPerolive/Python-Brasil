from datetime import datetime, timedelta

class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()



    def ano_cadastro(self):
        ano_cadastro = self.momento_cadastro.year
        return ano_cadastro

    def mes_cadastro(self):
        meses_do_ano = (
            "MesesDoAno","Janeiro", "Fervereiro", "Março", "Abril", 
            "Maio", "Junho", "Julho", "Agosto", "Setembro", 
            "Outubro", "Novembro", "Dezembro"
        ) 
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro]

    def dia_cadastro(self):
        dia_cadastro = self.momento_cadastro.day
        return dia_cadastro



    def dia_semana(self):
        dia_semana = (
            "Segunda-feira", "Terça-feira", "Quarta-feira", 
            "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"
        )
        dia_semana_cadastro = self.momento_cadastro.weekday()
        return dia_semana[dia_semana_cadastro]
    


    def formata_data(self):
        hoje_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return hoje_formatada
    


    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro