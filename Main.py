from Amigo import Amigo  # Importe a classe Amigo de Amigo.py
from dvd import DVD  # Importe a classe DVD de dvd.py

class SistemaDeEmprestimoDVD:
    def init(self):
        self.amigos = []  # Lista de amigos cadastrados
        self.dvds = []  # Lista de DVDs cadastrados

    def cadastrar_amigo(self, nome, telefone, email):
        amigo = Amigo(nome, telefone, email)
        self.amigos.append(amigo)

    def cadastrar_dvd(self, titulo, sinopse, diretor, ator_principal, genero, faixa_etaria):
        dvd = DVD(titulo, sinopse, diretor, ator_principal, genero, faixa_etaria)
        self.dvds.append(dvd)

    def emprestar_dvd(self, amigo, dvd):
        if amigo in self.amigos and dvd in self.dvds and not dvd.emprestado:
            dvd.emprestado = True
            dvd.amigo_emprestado = amigo
            return f"{amigo.nome} pegou emprestado o DVD '{dvd.titulo}'"
        elif dvd.emprestado:
            return f"O DVD '{dvd.titulo}' já foi emprestado a {dvd.amigo_emprestado.nome}"
        else:
            return "Amigo ou DVD não encontrado."

    def listar_dvds_emprestados(self):
        dvds_emprestados = [dvd for dvd in self.dvds if dvd.emprestado]
        if not dvds_emprestados:
            return "Nenhum DVD foi emprestado."
        else:
            lista_emprestimos = []
            for dvd in dvds_emprestados:
                lista_emprestimos.append(f"'{dvd.titulo}' emprestado para {dvd.amigo_emprestado.nome}")
            return "\n".join(lista_emprestimos)
        
sistema = SistemaDeEmprestimoDVD()

sistema.cadastrar_amigo("Amigo1", "123456789", "amigo1@email.com")
sistema.cadastrar_amigo("Amigo2", "987654321", "amigo2@email.com")

sistema.cadastrar_dvd("Filme1", "Sinopse1", "Diretor1", "Ator1", "Aventura", "Livre")
sistema.cadastrar_dvd("Filme2", "Sinopse2", "Diretor2", "Ator2", "Comédia", "12+")

print(sistema.emprestar_dvd(sistema.amigos[0], sistema.dvds[0]))  # Amigo1 pegou emprestado o DVD 'Filme1'
print(sistema.emprestar_dvd(sistema.amigos[1], sistema.dvds[0]))  # O DVD 'Filme1' já foi emprestado a Amigo1

print(sistema.listar_dvds_emprestados())  # 'Filme1' emprestado para Amigo1