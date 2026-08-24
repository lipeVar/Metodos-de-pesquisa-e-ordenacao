import random
from model.processo import processo

class processo_service:
    #classe para criar id aleatorio
    def popular(self, lista: list, quantidade: int):
        #se a lista n existe ele return a lista
        if lista is None:
            return
        for _ in range(quantidade):
            contador: int = quantidade
            id_aleatorio = random.randint(100, 499)
            desc = f"Gerando uma string {random.randint(0, quantidade -1)}"
            lista.append(processo(id_aleatorio, desc))

    #class para ordenar os IDs recebidos e deixar em ordem
    def ordenar_bolha(self, lista: list):
        if not lista or len(lista) <= 1:
            return

        n = len(lista)
        for i in range(n):
            houve_troca = False
            for j in range(0, n - i - 1):
                if lista[j+1] < lista[j]: #chama o __lt__
                    lista[j], lista [j+1] = lista[j+1], lista[j]
                    houve_troca = True
            if not houve_troca:
                break