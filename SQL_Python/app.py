from my_database import MyDb

lista = [
    ('Tete','Dias','19'),
    ('Marcelo','Dias','20'),
    ('Vitor','Schnaider','19'),

]

db = MyDb("database.db")

db.show()

#db.colocar_valor("Bruno","Dias",'19')
#db.colocar_muitos(lista)

#db.show()

db.show_name("Pedro")

#db.delete("Pedro","Delavechia")

db.update("Julio","Nagaita","Jow","Estefanelli Peroni")

db.show()
