"""
Módulo painel - usa painel do rich
"""
from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto: str, isArquivo: bool = False):
    """Mostra texto em um painel"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto))

def painel_alerta(texto: str, isArquivo: bool = False):
    """Mostra texto em um painel vermelho"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto, style="bold red"))
