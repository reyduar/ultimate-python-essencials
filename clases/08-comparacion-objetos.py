class Cordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    # Metodo mágico __eq__ se ejecuta cuando se compara un objeto con ==
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
    
    # Metodo mágico __ne__ se ejecuta cuando se compara un objeto con !=
    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon
    
    # Metodo mágico __str__ se ejecuta cuando se imprime un objeto
    def __str__(self):
        return f'Latitud: {self.lat}, Longitud: {self.lon}'
    
    # Metodo mágico __lt__ se ejecuta cuando se compara un objeto con <
    def __lt__(self, other):
        return self.lat < other.lat and self.lon < other.lon
    
    # Metodo mágico __le__ se ejecuta cuando se compara un objeto con <=
    def __le__(self, other):
        return self.lat <= other.lat and self.lon <= other.lon


coords1 = Cordenadas(10, 20);
coords2 = Cordenadas(10, 20);


print(coords1 == coords2) # True
print(coords1 != coords2) # False
print(coords1 < coords2) # False
print(coords1 <= coords2) # True

