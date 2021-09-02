from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado'
            print(info)
            self.log_info(info)
            return 
        if self._conectado:
            info = f'{self._nome} JÀ ESTA CONECTADO.'
            print(info)
            self.log_error(info)
            return
        info = f'{self._nome} esta conectado.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado'
            print(info)
            self.log_info(info)
            return
        if not self._conectado:
            info = f'{self._nome} NÃO ESTA CONECTADO'
            print(info)
            self.log_error(info)
            return
        info = f'{self._nome} foi desligado'
        print(info)
        self.log_info(info)
        self._conectado = False    