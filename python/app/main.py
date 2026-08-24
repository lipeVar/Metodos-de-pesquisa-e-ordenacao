from controller.processo_controller import processo_controller
from model.processo_service import processo_service
from view.processo_view import processo_view

if __name__ == '__main__':
    service = processo_service()
    view = processo_view()
    controller = processo_controller(service, view)
    controller.iniciar_sistema()