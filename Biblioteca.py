import json
import os

ARQUIVO = "livros.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar(livros):
    with open(ARQUIVO, "w") as f:
        json.dump(livros, f, indent=2)

def adicionar(livros):
    titulo = input("Título: ")
    autor = input("Autor: ")
    livros.append({"titulo": titulo, "autor": autor})
    salvar(livros)

def listar(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for i, l in enumerate(livros):
        print(f"{i} - {l['titulo']} ({l['autor']})")

def remover(livros):
    listar(livros)
    n = int(input("Número para apagar: "))
    livros.pop(n)
    salvar(livros)

def buscar(livros):
    termo = input("Buscar título: ").lower()
    for l in livros:
        if termo in l["titulo"].lower():
            print(f"- {l['titulo']} ({l['autor']})")

def main():
    livros = carregar()
    while True:
        print("\n1-Adicionar | 2-Listar | 3-Remover | 4-Buscar | 5-Sair")
        op = input("> ")
        if op == "1": adicionar(livros)
        elif op == "2": listar(livros)
        elif op == "3": remover(livros)
        elif op == "4": buscar(livros)
        elif op == "5": break

main()
