# utils.py - Funcoes utilitarias
# GlTechSolutions2026

def separador(caractere="-", tamanho=40):
      print(caractere * tamanho)

def cabecalho(titulo):
      separador("=")
      print(f"  {titulo}")
      separador("=")

def confirmar_acao(mensagem):
      resposta = input(f"{mensagem} (s/n): ").strip().lower()
      return resposta == "s"

def limpar_tela():
      import os
      os.system("cls" if os.name == "nt" else "clear")
