class Amigo:
    def init(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def str(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"