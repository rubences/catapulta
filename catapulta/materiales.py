"""
Módulo que define los materiales para construir la catapulta
"""

class Material:
    """Clase base para todos los materiales"""
    def __init__(self, nombre, resistencia, peso):
        self.nombre = nombre
        self.resistencia = resistencia
        self.peso = peso
    
    def __str__(self):
        return f"{self.nombre} (Resistencia: {self.resistencia}, Peso: {self.peso})"


class Palo(Material):
    """Material para la estructura de la catapulta"""
    def __init__(self, longitud):
        super().__init__("Palo", resistencia=10, peso=5)
        self.longitud = longitud
        self.potencia_base = longitud * 2
    
    def __str__(self):
        return f"{super().__str__()}, Longitud: {self.longitud}cm"


class Goma(Material):
    """Material elástico para proporcionar impulso"""
    def __init__(self, elasticidad):
        super().__init__("Goma", resistencia=5, peso=1)
        self.elasticidad = elasticidad  # 1-10
        self.impulso = elasticidad * 5
    
    def __str__(self):
        return f"{super().__str__()}, Elasticidad: {self.elasticidad}"


class Tapon(Material):
    """Material para reforzar las uniones"""
    def __init__(self):
        super().__init__("Tapón", resistencia=8, peso=2)
        self.estabilidad = 3
    
    def __str__(self):
        return f"{super().__str__()}, Estabilidad: +{self.estabilidad}"


class Corcho(Material):
    """Proyectil ligero"""
    def __init__(self):
        super().__init__("Corcho", resistencia=2, peso=1)
        self.danio = 5
    
    def __str__(self):
        return f"{super().__str__()}, Daño: {self.danio}"


class Pegamento(Material):
    """Material para unir componentes"""
    def __init__(self, calidad):
        super().__init__("Pegamento", resistencia=calidad * 2, peso=0.5)
        self.calidad = calidad  # 1-10
        self.union = calidad * 1.5
    
    def __str__(self):
        return f"{super().__str__()}, Calidad: {self.calidad}"
