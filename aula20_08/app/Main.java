package aula20_08.app;

import aula20_08.app.controller.ProcessoController;
import aula20_08.app.model.ProcessoService;
import aula20_08.app.view.ProcessoView;


public class Main {
    public static void main(String[] args) {
        // 1. instancia o processo model e view
        ProcessoService service = new ProcessoService();
        ProcessoView view = new ProcessoView();

        //2. instancia o controller utilizando service e view
        ProcessoController controller = new ProcessoController(service, view);

        //3. iniciando o fluxo da aplicação atraves do metodo controller
        controller.iniciarSistema();
    }
}
