#Constantes
NUMERO_MAXIMO =150 # NÚMERO TOTAL DE POKEMON DA 1° GERAÇÃO
TIPOS = ('Normal', 'Fogo', 'Água', 'Planta', 'Elétrico', 'Gelo', 'Lutador', 'Venenoso', 'Terra', 'Voador', 'Psíquico', 'Inseto', 'Pedra', 'Fantasma', 'Dragão', 'Noturno', 'Metálico', 'Fada')

#Funções
def verificar_tipo_pokemon(tipo):
    """Verifica se um tipo de Pokémon é válido. """
    return tipo in  TIPOS

def verificar_numero_pokemon(numero):
    """Verifica se um número de Pokémon é válido"""
    return 1 <= numero <= NUMERO_MAXIMO