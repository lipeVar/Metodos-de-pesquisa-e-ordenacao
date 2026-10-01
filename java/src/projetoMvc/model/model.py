"""
package projeto.model;

import java.util.List;
import java.util.Random;

public class Utilidades {
    /**
     * método de classe que popula lista ou com números aleatorios e de forma sequencial dentro de uma faixa
     * @param lista
     * @param quantidadeNumeros
     * @param inicio
     * @param fim
     * @param aleatorio - se true os números devem ser aleatórios
     */
    public static void popularLista(List<Integer> lista, long quantidadeNumeros, int inicio, int fim, boolean aleatorio) {
        Random gerador = new Random();
        
        if (aleatorio) {
            for (long i = 0; i < quantidadeNumeros; i++) {
                lista.add(gerador.nextInt(inicio, fim));
            }
        } else {
            for (long i = 0; i < quantidadeNumeros; i++) {
                lista.add((int) (inicio + i));
            }
        }
    }
}
"""
import random

class ModelList:
    def __init__(self):
        self.lista_aleatoria = []
        self.lista_ordenada = []

    """def popular_lista_sequencial(self, quantidade: int, inicio: int, fim: int) -> None:
        EXEMPLO DE BOA PRATICA """
    def popular_lista_aleatoria(self, quantidade, inicio, fim):
        """Gera numeros aleatorios dentro da faixa"""
        self.lista_aleatoria = [random.randint(inicio, fim - 1) for _ in range(quantidade)]

    """def popular_lista_sequencial(self, quantidade: int, inicio: int) -> None:
            EXEMPLO DE BOA PRATICA """
    def popular_lista_ordenada(self, quantidade, inicio, fim):
        """Gera numeros ordenados dentro de uma faixa"""
        self.lista_ordenada = list(range(inicio, quantidade))

    """Criação de metodos getters para retornar as listas como uma boa pratica de encapsulamento"""
    def get_lista_aleatorios(self) -> list:
        return self.lista_aleatoria
    def get_lista_ordenados(self) -> list:
        return self.lista_ordenada