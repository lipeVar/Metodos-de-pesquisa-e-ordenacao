/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model;

import java.io.FileReader;
import java.io.BufferedReader;
import java.util.ArrayList;

/**
 *
 * @author lfvar
 * 
 */
public class Procurador {
    /**
     * Carregar numero interio de arquivos de texto
     * 
     * @param nomeArquivo caminho e nome do arquivo
     * @param lista LIsta que recebe os inteiros
     */
     
     public static boolean carregarArquivo(String nomeArquivo, ArrayList<Integer> lista){
         try{
             FileReader procurador;
             procurador = new FileReader(nomeArquivo);
             BufferedReader leitor = new BufferedReader(procurador);
             String linha;
             
             do {                 
                 linha = leitor.readLine();
                 if(linha != null) {
                     lista.add(Integer.parseInt(linha));
                 }
             } while (linha != null);
             leitor.close();
             return true;
         } catch (Exception e) {
             return false;
         }
     }
}
