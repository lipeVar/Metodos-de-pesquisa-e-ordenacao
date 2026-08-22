package aula20_08.app.model

import java.util.List;
import java.util.Random;

public class ProcessoService {

    public void ordenarBolha(List<Processo> lista) {
        if (lista == null || lista.size() <= 1) {
            return;
        }

        Processo tmp;
        boolean houveTroca;
        do {
            houveTroca = false;
            for (int i = 0; i < lista.size() - 1; i++) {
                
                if (lista.get(i).compareTo(lista.get(i + 1)) > 0) {
                    houveTroca = true;
                    tmp = lista.get(i);
                    lista.set(i, lista.get(i + 1));
                    lista.set(i + 1, tmp);
                }
            }
        } while (houveTroca);
    }

    public void popular(List<Processo> lista, int quantidade) {
        if (lista == null) return;

        Random gerador = new Random();
        for (int i = 0; i < quantidade; i++) {
            
            int idAleatorio = 100 + gerador.nextInt(400);
            lista.add(new Processo(idAleatorio, "gerando uma string " + gerador.nextInt(quantidade)));
        }
    }
}