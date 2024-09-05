class Lista(list):
   def prepend(self, value):
      self.insert(0, value)

lista = Lista([1, 2, 3])
lista.append(4)
lista.prepend(0)
print(lista)