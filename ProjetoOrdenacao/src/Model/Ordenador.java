/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model;

import java.util.ArrayList;
/**
 *
 * @author lfvar
 */
public class Ordenador {
    public static ArrayList bolha(ArrayList<Integer> lista){
        ArrayList<Float> estatisticas = new ArrayList<>();
        long qtdComparacoes = 0;
        long qtdTrocas = 0;
        int aux;
        boolean houveTroca;
        int i;
        do {            
            houveTroca = false;
            for(i=0; i < lista.size() - 1; i++) {
                qtdComparacoes++;
                if(lista.get(i) > lista.get(i + 1)) {
                    houveTroca = true;
                    aux = lista.get(i);
                    lista.set(i, lista.get(i + 1));
                    lista.set(i + 1, aux);
                    qtdTrocas++;
                }
            }
        } while (houveTroca);
        estatisticas.add((float) qtdComparacoes);
        estatisticas.add((float) qtdTrocas);
        return estatisticas;
    }
    
    public static ArrayList selection(ArrayList<Integer> lista) {
        ArrayList<Float> estatisticas = new ArrayList<>();
        long qtdComparacoes = 0;
        long qtdTrocas = 0;
        int i, j, posiMenor, aux;
        posiMenor = 0;
        
        for(i=0; i< lista.size(); i++) {
            posiMenor = i;
            for(j = i +1; j<lista.size(); j++) {
                qtdComparacoes++;
                if(lista.get(j) < lista.get(posiMenor)){
                    posiMenor = j;
                }
            }
            if(posiMenor != i) {
                aux = lista.get(i);
                lista.set(i, lista.get(posiMenor));
                lista.set(posiMenor, aux);
                qtdTrocas++;
            }
        }
        
        estatisticas.add((float) qtdComparacoes);
        estatisticas.add((float) qtdTrocas);
        return estatisticas;
    }
    
    public static ArrayList insercao(ArrayList<Integer> lista){
        ArrayList<Float> estatisticas = new ArrayList<>();
        long qtdComparacoes = 0;
        long qtdTrocas = 0;
        int i, j, aux;
        
        for(i=0; i<lista.size(); i++){
            aux = lista.get(i);
            for(j=i; j<lista.size(); j++) {
                qtdTrocas++;
                lista.set(j+1, lista.get(j));
            }
            lista.set(j+1, aux);
        }
        estatisticas.add((float) qtdComparacoes);
        estatisticas.add((float) qtdTrocas);
        return estatisticas;
    }
    
    public static ArrayList combSort(ArrayList<Integer> lista){
        ArrayList<Float> estatisticas = new ArrayList<>();
        long qtdComparacoes = 0;
        long qtdTrocas = 0;
        int aux, i;
        boolean houveTroca;
        int distancia = lista.size();
        
        do {            
            distancia = (int) (distancia/1.3);
            if(distancia <= 0) {
                distancia = 1;
            }
            houveTroca = false;
            for(i=0; i + distancia < lista.size(); i++){
                qtdComparacoes++;
                if(lista.get(i) < lista.get(i + distancia)){
                    houveTroca = true;
                    aux = lista.get(i);
                    lista.set(i, lista.get(i + distancia));
                    lista.set(i + distancia, aux);
                    qtdTrocas++;
                }
            }
        } while (distancia > 1 || houveTroca);
        estatisticas.add((float) qtdComparacoes);
        estatisticas.add((float) qtdTrocas);
        return estatisticas;  
    }
}
