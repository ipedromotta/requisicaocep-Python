import requests

class Consulta:

    def consultar(self):
        self.resultado = ''
        cep = self.tela_buscador.input_cep.text()
        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        try:
            endereco = url.json()
            if "erro" in endereco:
                self.tela_buscador.resultado.setText("CEP INVÁLIDO")
            else:
                for k, v in endereco.items():
                    self.resultado += f'{k.upper()} : {v}\n'
                self.tela_buscador.resultado.setText(self.resultado)
        except:
            self.tela_buscador.resultado.setText("CEP INVÁLIDO")
