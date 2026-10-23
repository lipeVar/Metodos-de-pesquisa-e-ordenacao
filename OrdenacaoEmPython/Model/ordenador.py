from ast import Nonlocal
import time 
from dataclasses import dataclass
from typing import List

@dataclass
class ResultadoOrdenacao:
    lista_ordenada: List[int]
    tempo_execucao: float
    total_trocas: int
    total_comparacoes: int

class Ordenador:
    # Ordenador Bolha
    def bolha(self, lista: List[int]) -> ResultadoOrdenacao:
        array = lista.copy()
        n = len(array)
        trocas = comparacoes = 0

        inicio = time.perf_counter()

        for i in range(n):
            houve_troca = False
            for j in range(0, n-i-1):
                comparacoes += 1
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    trocas += 1
                    houve_troca = True
            # se não houve nem uma troca entao o array ja esta ordenado
            if not houve_troca:
                break

        tempo_total = time.perf_counter() - inicio
        return ResultadoOrdenacao(array, tempo_total, trocas, comparacoes)

    #Ordenador Seleção
    def selecao(self, lista: List[int]) -> ResultadoOrdenacao:
        array = lista.copy()
        n = len(array)
        trocas = comparacoes = 0

        inicio = time.perf_counter()
        for i in range(n):
            minimo = 1
            for j in range(i+1, n):
                comparacoes += 1
                if array[j] < array[minimo]:
                    minimo = j

            if minimo != i:
                array[i], array[minimo] = array[minimo], array[i]
                trocas += 1
        tempo_total = time.perf_counter() - inicio
        return ResultadoOrdenacao(array, tempo_total, trocas, comparacoes)

    def insercao(self, lista: List[int]) -> ResultadoOrdenacao:
        array = lista.copy()
        n = len(array)
        trocas = comparacoes = 0

        inicio = time.perf_counter()
        for i in range(1, n):
            chave = array[i]
            j = i - 1

            while j>=0:
                comparacoes += 1
                if array[i] > chave:
                    array[j + 1] = array[j]
                    trocas += 1
                    j -= 1
                else:
                    break
            array[j + 1] = chave
        tempo_total = time.perf_counter() - inicio
        return ResultadoOrdenacao(array, tempo_total, trocas, comparacoes)

    def pente(self, lista: List[int]) -> ResultadoOrdenacao:
        array = lista.copy()
        n = len(array)
        trocas = comparacoes = 0

        gap = n
        ordenado = False

        inicio = time.perf_counter()
        while not ordenado:
            gap = int(gap / 1.3)
            if gap <= 1:
                gap = 1
                ordenador = True

            for i in range(0, n-gap):
                comparacoes += 1
                if array[i] > array[i + gap]:
                    array[i], array[i+gap] = array[i+gap], array[i]
                    trocas += 1
                    ordenado = False

        tempo_total = time.perf_counter() - inicio
        return ResultadoOrdenacao(array, tempo_total, trocas, comparacoes)

    def merge(self, lista: List[int]) -> ResultadoOrdenacao:
        array = lista.copy()
        trocas = comparacoes = 0

        def _merge_sort_recursivo(sub_array):
            nonlocal trocas, comparacoes
            
            if len(sub_array) <= 1:
                return

            meio = len(sub_array) // 2
            esquerda = sub_array[:meio]
            direita = sub_array[meio:]

            _merge_sort_recursivo(esquerda)
            _merge_sort_recursivo(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                comparacoes += 1
                if esquerda[i] <= direita[j]:
                    sub_array[k] = esquerda[i]
                    i += 1  
                else:
                    sub_array[k] = direita[j]
                    j += 1
                    trocas += 1
                k += 1

            while i < len(esquerda):
                sub_array[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                sub_array[k] = direita[j]
                j += 1
                k += 1

        inicio = time.perf_counter()
        _merge_sort_recursivo(array)
        tempo_total = time.perf_counter() - inicio

        return ResultadoOrdenacao(array, tempo_total, trocas, comparacoes)
            