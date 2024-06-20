from model.model import Model

mymodel = Model()
mymodel.buildGraph("ALTICEUSA", 0.5)
print(mymodel.printGraphDetails())

for tupla in mymodel.getMaxVicini():
    for nodo in tupla[0]:
        print(f"{nodo}, numero vicini = {tupla[1]}")
