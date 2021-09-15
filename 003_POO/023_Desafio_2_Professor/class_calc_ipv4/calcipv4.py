"""[summary]
- Será utilizado expressões regulares para validade o ip (conteudo ainda não visto)
Returns:
    [type]: [description]
"""
import re

class CalcIPv4:
    
    def __init__(self, ip, mascara=None, prefixo=None) -> None:
        self._ip = None
        self._mascara = None
        self._prefixo = None

        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()


    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('Ip invalido')
        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)
    
    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return #usuario pode não digitar mascara 
        if not self._valida_ip(valor):
            raise ValueError('Mascara Invalida')
        
        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)
        if not hasattr(self,'prefixo'):
            self.prefixo = self._mascara_bin.count('1')
         

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return #pode ser que o usuario não digite valor 
        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro')
        if valor > 32:
            raise TypeError('Prefixo precisa ser de 32bits')
        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32,'0')
        if not hasattr(self,'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)
        

    @staticmethod
    def _valida_ip(ip):
        regex = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regex.search(ip):
            return True
    
    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split(".")
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(blocos_binarios)


    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+1],2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
         host_bits = 32 - self.prefixo
         self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
         self._broadcast = self._bin_to_ip(self._broadcast_bin)
         #print(self._broadcast)

#parei em 36:53