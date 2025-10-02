from rich.console import Console

console = Console()

def negrito(texto: str, isArquivo: bool = False):
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(f"[bold]{texto}[/bold]")

def verde(texto: str, isArquivo: bool = False):
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(f"[green]{texto}[/green]")