# Versao: 1.1 - Adicionado controle de versao
# main.py - Sistema de Gestao de Tarefas
# GlTechSolutions2026

from tarefas import Tarefa, GerenciadorTarefas

def menu():
      print("\n=== Sistema de Gestao de Tarefas ===")
      print("1. Adicionar tarefa")
      print("2. Listar tarefas")
      print("3. Concluir tarefa")
      print("4. Remover tarefa")
      print("0. Sair")
      return input("Escolha uma opcao: ")

def main():
      gerenciador = GerenciadorTarefas()

    while True:
              opcao = menu()

        if opcao == "1":
                      titulo = input("Titulo da tarefa: ")
                      descricao = input("Descricao: ")
                      tarefa = Tarefa(titulo, descricao)
                      gerenciador.adicionar(tarefa)
                      print("Tarefa adicionada com sucesso!")

elif opcao == "2":
              gerenciador.listar()

elif opcao == "3":
              idx = int(input("Numero da tarefa a concluir: ")) - 1
              gerenciador.concluir(idx)

elif opcao == "4":
              idx = int(input("Numero da tarefa a remover: ")) - 1
              gerenciador.remover(idx)

elif opcao == "0":
              print("Encerrando o sistema. Ate logo!")
              break

else:
              print("Opcao invalida!")

if __name__ == "__main__":
      main()
