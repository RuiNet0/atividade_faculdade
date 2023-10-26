class DVD:
    def init(self, titulo, sinopse, diretor, ator_principal, genero, faixa_etaria):
        self.titulo = titulo
        self.sinopse = sinopse
        self.diretor = diretor
        self.ator_principal = ator_principal
        self.genero = genero
        self.faixa_etaria = faixa_etaria

        def str(self):
            return f"Título: {self.titulo}, Sinopse: {self.sinopse}, Diretor: {self.diretor}, Ator Principal: {self.ator_principal}, Gênero: {self.genero}, Faixa Etária: {self.faixa_etaria}"