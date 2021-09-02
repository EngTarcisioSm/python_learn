
# feita unicamente para adicionar funcionalidades em outras classes 
class LogMixin:
    #como em nenhum momento é solicitado dados da classe é possivel torna-la statica, removendo self e colocando a palavra reservada @staticmethod antes do nome do métod
    @staticmethod
    def write(msg):
        # sempre vai adicionar uma nova linha ao arquivo por conta de 'a+'
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')
    
    def log_info(self, msg):
        self.write(f'INFO : {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')