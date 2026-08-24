class processo_view:
    def exibir_lista(self, mensagem: str, lista: list):
        print(f"\n--- {mensagem} ---")
        for item in lista:
            print(item)
