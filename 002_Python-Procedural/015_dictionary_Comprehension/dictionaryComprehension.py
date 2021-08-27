'''
Dictionary Comprehension e Set Comprehension
    - Dictionary Comprehension
        I.  A diferença entre list e dictionary comprehension é bem sutil. A diferença se baseia
            no uso de {} ao inves de []
        II. Pode ser feito iterações ao se utilizar
    - Set Comprehension
        I.  Na ausencia de chave, valor tendo apenas um valor gera-se sets
    - Todo processo de list comprehension se aplica a dictionary e a setcomprehension

'''
print("#1")
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]
d1 = {x:y for x, y in lista}
print(d1)

print("\n#2")
d2 = {x:y*2 for x, y in lista}
print(d2)
d3 = {f'chave_{x}': x**2 for x in range(10)}
print(d3)

print("\n#3")
s1 = {x for x in range(10)}
print(s1, type(s1))