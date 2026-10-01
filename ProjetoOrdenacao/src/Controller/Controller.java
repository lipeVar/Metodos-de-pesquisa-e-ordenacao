/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import java.util.ArrayList;
import Model.Ordenador;
import Model.Procurador;

/**
 *
 * @author lfvar
 */
public class Controller {
    /*
    * Lista de numeros carregada do arquivo informado na view
    */
    ArrayList<Integer> listaNumero = new ArrayList();
    
    public boolean carregarArquivo(String nomeArquivo) {
        listaNumero.clear();
        return Procurador.carregarArquivo(nomeArquivo, listaNumero);
    }
    
    /*
        Executa o algoritmo de ordenação de acordo com a escolha do usuario
        
        Faz a copia de da lista original para que novas execuções possam ser iniciadas 
        usando os mesmos numeros sem reabrir o arquivo.
    
        "metodo" é o nome do metodo de ordenacao selecionado na interface.
        @return Lista de metricas que a posicao 0 é a quantidade de comparações 
              e a posicao 1 é a quantidade de trocas
    */
    public ArrayList<Float> execute(String metodo) {
        ArrayList<Integer> copiarLista = new ArrayList<>(listaNumero);
        switch (metodo) {
            case "Bolha":
                return Ordenador.bolha(copiarLista);
            case "Seleção":
                return Ordenador.selection(copiarLista);
            case "Inserção":
                return Ordenador.insercao(copiarLista);
            case "Pente":
                    return Ordenador.combSort(copiarLista);
            default:
                return new ArrayList<>();
        }
    }
    
    /*
        Metodo para limpar o armazenamento
    
        Acionado pelo botão BtnLimpar da view para recomeçar
    */
    public void limparLista() {
        listaNumero.clear();
    }
    
    /*
        informa a quantidade de numeros carregados na lista
    */
    
    public int quantidade() {
        return listaNumero.size();
    }
}
