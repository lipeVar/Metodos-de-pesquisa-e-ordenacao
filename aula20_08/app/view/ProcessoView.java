package aula20_08.app.view;

import java.util.List;
import aula20_08.app.model.*;

public class ProcessoView {
    public void exibirLista(String mensagem, List<Processo> lista) {
        System.out.println("\n--- " + mensagem + " ---");
        for (aula20_08.app.model.Processo item : lista) {
            System.out.println(item);
        }
    }
}
