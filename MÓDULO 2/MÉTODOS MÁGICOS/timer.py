from datetime import datetime

class Evento:
    # Atributo de classe
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False

        # Incrementa o total de eventos sempre que um novo é criado
        Evento.total_eventos += 1


# Teste da Parte 1
evento1 = Evento("Reunião de TI", datetime(2025, 10, 16, 14, 0), "Reunião com a equipe de desenvolvimento.")
evento2 = Evento("Apresentação CIPA", datetime(2025, 10, 20, 9, 0), "Treinamento sobre segurança no trabalho.")

# Imprimindo os atributos
print("Evento 1:")
print("Título:", evento1.titulo)
print("Data e hora:", evento1.data_hora)
print("Descrição:", evento1.descricao)
print("Concluído:", evento1.is_concluido)
print()

print("Evento 2:")
print("Título:", evento2.titulo)
print("Data e hora:", evento2.data_hora)
print("Descrição:", evento2.descricao)
print("Concluído:", evento2.is_concluido)
print()

print("Total de eventos criados:", Evento.total_eventos)
