'''
- Diferente de outras linguagens o python não possui blocos de códigos definidos
com o abrir e fechar de de chaves

- A palavra reservada 'pass' é utilizada quando o desenvolvedor deseja deixar uma area do código
preparada para posterior implementação de uma lógica de código, caso deixado o local vazio pode
ocasionar em erro de sintaxe
- Outra forma de se obter o mesmo resultado com o mesmo contexto de uso é utilizando '...'
- Em abas situações caso haja necessário é possivel utilizar comentários 
'''
# uso de pass
teste = True

if teste:
    pass
else:
    print('falhou...')

# utilizando ...
if teste:
    print('passou...')
else:
    ...