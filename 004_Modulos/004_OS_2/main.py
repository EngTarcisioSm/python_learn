'''
OS + SHUTIL
    - Mover
    - Copiar
    - Apagar arquivos

    - Em caminhos utilizando windows é comum de se utilizar barra invertida, existe duas saidas 
        - usar r 'conteudo com barra invertida'
        - usar duas barras em cada uma das barras unitarias 
            c:\\windows\\...

    - É possivel remover arquivos entretanto deve se ter cuidado por se tratar de um processo irrevercivel 

    - em shutil existe o método de copiar um arquivo 
'''
import os 
import shutil

caminho_original = r'C:\esp\esp-idf\esp-course2'
caminho_novo = r'F:\projetos\esp32\esp-course'

#criando pasta nova
try:
    os.mkdir(caminho_novo)
    print(f'Pasta {caminho_novo} criado com sucesso!\n')
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe!\n')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        #junto o caminho + nome do arquivo em uma string 
        old_file_path = os.path.join(root, file)
        #print(old_file_path)
        
        #criando o novo caminho 
        new_file_path = os.path.join(caminho_novo, file)
        print(new_file_path)

        #move arquivos não mantem a estrutura de subpastas
        #é possivel alterar o nome do arquivo ao move-lo bastando dar um novo nome para o mesmo em new_file_path
        '''
        try:
            shutil.move(old_file_path, new_file_path)
        except Exception as e:
            print("Falha ao mover o arquivo", e)
        '''
        #Remover Arquivos

        #selecionando o tipo de arquivo a ser excluido
        if '.obj' in file:
            os.remove(new_file_path)

        
        
        