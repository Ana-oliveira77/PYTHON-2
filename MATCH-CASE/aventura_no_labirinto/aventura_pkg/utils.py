"""
Funções utilitárias: instruções, menu e animação recursiva.
"""

from rich.console import Console
console = Console()

def imprime_instrucoes():
    """
    Exibe instruções do jogo formatadas com Rich.
    """
    console.print("[bold cyan]Instruções:[/bold cyan]")
    console.print("Use W, A, S, D para se mover.")
    console.print("Chegue até a saída (E) para vencer!")

def menu_principal():
    """
    Exibe o menu e retorna a opção escolhida.
    """
    console.print("\n[bold green]=== AVENTURA NO LABIRINTO ===[/bold green]")
    console.print("1 - Jogar")
    console.print("2 - Instruções")
    console.print("3 - Sair")
    return input("Escolha uma opção: ")

def animacao_vitoria(n=5):
    """
    Função recursiva simples de celebração.
    """
    if n == 0:
        return
    console.print(f"[yellow]🎉 Parabéns! Vitória em {n}...[/yellow]")
    animacao_vitoria(n - 1)
