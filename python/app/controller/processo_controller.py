from model.processo_service import processo_service
from model.processo import processo
from view.processo_view import processo_view

class processo_controller:
    def __init__(self, service: processo_service, view: processo_view):
        self.service = service
        self.view = view
        self.lista_processo = []

    def iniciar_sistema(self):
        self.service.popular(self.lista_processo, 4)
        self.view.exibir_lista("Mostrando a lista com IDs gerados", self.lista_processo)
        self.service.ordenar_bolha(self.lista_processo)
        self.view.exibir_lista("Lista com IDs em ordem", self.lista_processo)