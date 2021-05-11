# https://pypi.org/project/prettytable/
# pip install prettytable

from prettytable import PrettyTable as pt

# Inicializar com o nome das colunas
tabela = pt(["Funcionario", "Cargo", "Idade", "Genero"])

tabela.add_row(["Filipe", "Zelador", 20, "M"])
tabela.add_row(["João Pedro", "Caixa", 22, "M"])
tabela.add_row(["Lucas", "Secretário", 19, "M"])
tabela.add_row(["Moisés", "Cobrador", 22, "M"])
tabela.add_row(["Júlia", "Gerente", 25, "F"])

# print(tabela)

tabela.add_rows(
    [
        ["Amanda", "Estagiária", 20, "F"],
        ["Gustavo", "Entregador", 26, "M"]
    ]
)

# print(tabela)

# print(tabela.get_string(fields=["Funcionario", "Idade"]))

# print(tabela.get_string(start=1, end=4))

tabela.align = "c"    # right, left, center
# print(tabela)

tabela.align["Funcionario"] = "l"
tabela.align["Cargo"] = "c"
tabela.align["Idade"] = "r"
tabela.align["Genero"] = "c"
# print(tabela)

#print(tabela.get_string(sortby="Funcionario"))
# print(tabela)

tabela.sortby = "Funcionario"
# print(tabela)
# print(tabela)

tabela.reversesort = True
# print(tabela)

tabela.sortby = None
print(tabela)
