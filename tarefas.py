# tarefas.py - Modulo de classes de Tarefas
# GlTechSolutions2026

from datetime import datetime

class Tarefa:
      def __init__(self, titulo, descricao):
                self.titulo = titulo
                self.descricao = descricao
                self.concluida = False
        self.criada_em = datetime.now().strftime("%d/%m/%Y %H:%M")

    def __str__(self):
              status = "[X]" if self.concluida else "[ ]"
              return f"{status} {self.titulo} - {self.descricao} (Criada em: {self.criada_em})"


class GerenciadorTarefas:
      def __init__(self):
                self.tarefas = []

    def adicionar(self, tarefa):
              self.tarefas.append(tarefa)

    def listar(self):
              if not self.tarefas:
                            print("Nenhuma tarefa cadastrada.")
                            return
                        print("\n--- Lista de Tarefas ---")
        for i, tarefa in enumerate(self.tarefas, start=1):
                      print(f"{i}. {tarefa}")

    def concluir(self, idx):
              if 0 <= idx < len(self.tarefas):
                            self.tarefas[idx].concluida = True
                            print("Tarefa marcada como concluida!")
else:
            print("Indice invalido.")

    def remover(self, idx):
              if 0 <= idx < len(self.tarefas):
                            removida = self.tarefas.pop(idx)
                            print(f"Tarefa '{removida.titulo}' removida.")
else:
            print("Indice invalido.")
