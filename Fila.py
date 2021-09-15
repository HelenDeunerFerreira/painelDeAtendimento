# Simular um sistema de painel de atendimento

# Cenário

#  - Senhas sequenciais vão sendo obtidas, ao passo que são enfileiradas pelo sistema
#  - O sistema acumula essas senhas em uma fila do tipo FIFO
#  - A medida que são 'chamadas' as senhas, estas vão sendo removidas e armazenadas em uma lista auxiliar

# Implementação
# ** Usar a estrutura de Fila criada durante a aula
# - Criar um menu com as opções:
#  1) Obter nova senha
#  2) Chamar próxima senha
#  3) Mostrar senhas chamadas

# Detalhamento
# - Obter nova senha
#   - Deverá ter um contador no app que começa com o valor zero
#   - Ao chamar uma senha, deverá enfileirar o próximo valor na estrutura Fila e incrementar este contador

# - Chamar próxima senha
#   - Acrescentar numa variável (list) no app, antes de remover da Fila, qual a senha que será chamada.
#   - Remover da Fila (usar o método dequeue)

# - Mostrar senhas chamadas
#   - Apresentar o valor armazenado em uma lista (list) durante a remoção do item da Fila


# class Fila:
#     def __init__(self):
#         self.senhasCriadas = []

#     def enqueue(self, contadorSenhas):  # enfileirar
#         self.senhasCriadas.append(contadorSenhas)

#     def dequeue(self):  # desenfileirar
#         if not self.senhasCriadas.is_empty():
#             return self.senhasCriadas.pop(0)
#         return None

#     def front(self):  # mostrar o 1o da fila, sem remover!
#         if not self.is_empty():
#             return self._vet[0]
#         return None

#     def is_empty(self):  # retorna se a fila esta vazia
#         if len(self._vet) == 0:
#             return True
#         return False

#     def __len__(self):
#         return len(self._vet)

#     def __str__(self):  # representacao da fila como string
#         return str(self._vet)

class Fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)
        return None

    def front(self): # mostrar o 1o da fila, sem remover!
        if not self.is_empty():
            return self._vet[0]
        return None
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)

## TESTES ##
# if __name__ == "__main__":
#     # Criando uma Fila
#     f = Fila()
#     assert len(f) == 0, "Deve ser zero!"

#     # Enfileirando um item
#     f.enqueue(1)
#     assert len(f) == 1, "A fila deveria estar com 1 elemento"

#     f.enqueue(2)
#     assert f.front() == 1, "1o elemento da fila deve ser 1"

#     f.enqueue("imed")
#     f.enqueue(77)

#     senha_chamada = str(f.dequeue())
#     chamadas = []
#     chamadas.append(senha_chamada)
#     print("Elemento removido: " + str(f.dequeue()))

#     print(f)
