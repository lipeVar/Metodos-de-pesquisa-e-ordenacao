class processo:
    #metodo construtor de obj
    def __init__(self, id_proc: int, descricao: str):
        self.id = id_proc  
        self.descricao = descricao

    #metodo de escrita pré programado
    def __repr__(self):
        return f"Processo [id={self.id}, descricao={self.descricao}]"

    #__lt__ metodo de ordenação
    def __lt__(self, other):
        # Verifica se o obj other percente à classe processo
        if isinstance(other, processo):
            #se o id atual for maior que o other retorna true
            return self.id < other.id
        return NotImplemented

