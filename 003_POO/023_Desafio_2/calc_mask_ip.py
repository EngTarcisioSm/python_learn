from math import log


class CalcMask():

    def __init__(self, qtdIP:int, ip:str) -> None:
        self.__qtdIP = qtdIP
        self.__ip = ip.split('.')
        
    @property
    def qtdIP(self):
        return self.__qtdIP
    
    @property
    def ip(self):
        return self.__ip

    def __calc_bit(self):
        return int(abs(log(self.qtdIP+2, 2)))

    @staticmethod
    def conv_dec_bin(valor:int):
        val_int = int(valor)
        answer = ''
        if val_int >= 128:
            answer += '1'
            val_int -= 128
        else:
            answer += '0'
        
        if val_int >= 64:
            answer += '1'
            val_int -= 64
        else:
            answer += '0'

        if val_int >= 32:
            answer += '1'
            val_int -= 32
        else:
            answer += '0'

        if val_int >= 16:
            answer += '1'
            val_int -= 16
        else:
            answer += '0'

        if val_int >= 8:
            answer += '1'
            val_int -= 8
        else:
            answer += '0'

        if val_int >= 4:
            answer += '1'
            val_int -= 4
        else:
            answer += '0'
        
        if val_int >= 2:
            answer += '1'
            val_int -= 2
        else:
            answer += '0'

        if val_int >= 1: 
            answer += '1'
            val_int -= 1
        else:
            answer += '0'

        return answer    

    def logic_and(num1:str, num2:str):
        if num1 == '1' and num2 == '1':
            return '1'
        else: 
            return '0'

    def generate_mask(self):
        mask = '11111111111111111111111111111111'
        
        aux = self.__calc_bit()
        a = list(mask)
        for x in range(len(mask)-1, len(mask)- (aux+1),-1):
            a[x] = '0'

        mask = "".join(a)

        answer = []
        answer.append(mask[0:8])
        answer.append(mask[8:16])
        answer.append(mask[16:24])
        answer.append(mask[24:33])

        return answer
    
    def number_ips(self):
        return pow(2,self.__calc_bit()) -2

    @staticmethod
    def bin_to_dec(valor:str):
        answer = 0
        for x, y in enumerate(valor):
            if y == '1':
                if x == 0:
                    answer += 128
                if x == 1:
                    answer += 64
                if x == 2:
                    answer += 32
                if x == 3:
                    answer += 16
                if x == 4:
                    answer += 8
                if x == 5:
                    answer += 4
                if x == 6:
                    answer += 2
                if x == 7:
                    answer += 1
        return str(answer)

    @staticmethod
    def invert(valor):
        answer = ""
        for x in valor:
            if x == '1':
                answer += '0'
            else:
                answer += '1'
        return answer


    def ip_broadcast(self):
        mask = self.generate_mask()
        answer = []
        for a, x in enumerate(mask):
            if x != '11111111':
                answer.append(self.bin_to_dec(self.invert(x)))
            else:
                answer.append(self.ip[a])
        a = answer[0] + '.' + answer[1] + '.' + answer[2] + '.' + answer[3]
        return a
    
    def ip_rede(self):
        a = self.ip_broadcast().split('.')
        answer = []
        for x in range(4):
            if self.ip[x] != a[x]:
                answer.append('0')
            else:
                answer.append(self.ip[x])
        
        b = answer[0] + '.' + answer[1] + '.' + answer[2] + '.' + answer[3]
        return b 

    def __str__(self):
        return f'Broadcast: {self.ip_broadcast()} | IP_Rede:{self.ip_rede()} | Numero IPs:{self.number_ips()}'


