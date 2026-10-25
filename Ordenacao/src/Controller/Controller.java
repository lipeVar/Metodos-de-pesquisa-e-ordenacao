/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;
import Model.Util;
import Model.Ordenador;
import java.util.ArrayList;
/**
 *
 * @author lfvar
 */
public class Controller {
    ArrayList<Integer> listaNumeros = new ArrayList<>();
    
    public boolean CarregarArquivo(String nomeArquivo) {
        listaNumeros.clear();
        return Util.CarregarArquivo(nomeArquivo, listaNumeros);
    }
    
    /**
     * Executa o algorotimo de acordo com a escolha no combo da View
     * 
     * <p> Trabalha fazendo uma copia da lista original para que a mesma lista
     * possa ser usada varias vezes sem reabrir o arquivo ou ter que criar outro arquivo
     */
    public ArrayList<Float> execute(String metodo) {
        ArrayList<Integer> copiarLista = new ArrayList<>(listaNumeros);
        switch (metodo) {
            case "Bolha":
                return Model.Ordenador.bolha(copiarLista);
            case "Seleção":
                return Model.Ordenador.selecao(copiarLista);
            case "Inserção":
                return Model.Ordenador.insercao(copiarLista);
            case "Pente":
                return Model.Ordenador.pente(copiarLista);
            default:
                return new ArrayList<>();
        }
    }
    
    /**
     * Remove todos os numeros atualmente armazenados na lista.
     * 
     * Executado pelo botão limpar na view
     */
    public void limparLista() {
        listaNumeros.clear();
    }
    
    /**
     * informa qunatos numeros estão carregados na lista
     * 
     * A view usa esse valor para validar o executar
     * e para preencher o camp quantidade no painel
     * 
     */
    
    public int quantidade() {
        return listaNumeros.size();
    }
}
