"""
Módulo que define los enemigos
"""

import random


class Enemigo:
    """Clase base para enemigos"""
    def __init__(self, nombre, vida, distancia, armadura=0):
        self.nombre = nombre
        self.vida_maxima = vida
        self.vida = vida
        self.distancia = distancia
        self.armadura = armadura
        self.vivo = True
    
    def recibir_danio(self, danio):
        """Recibe daño reducido por la armadura"""
        danio_real = max(0, danio - self.armadura)
        self.vida -= danio_real
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False
            return True  # Enemigo eliminado
        return False
    
    def __str__(self):
        estado = "Vivo" if self.vivo else "Eliminado"
        return f"{self.nombre} - Vida: {self.vida}/{self.vida_maxima}, Distancia: {self.distancia}m, Armadura: {self.armadura} [{estado}]"


class Soldado(Enemigo):
    """Enemigo básico"""
    def __init__(self, distancia):
        super().__init__("Soldado", vida=20, distancia=distancia, armadura=2)


class Caballero(Enemigo):
    """Enemigo con más armadura"""
    def __init__(self, distancia):
        super().__init__("Caballero", vida=35, distancia=distancia, armadura=5)


class Arquero(Enemigo):
    """Enemigo rápido pero débil"""
    def __init__(self, distancia):
        super().__init__("Arquero", vida=15, distancia=distancia, armadura=1)


class Gigante(Enemigo):
    """Enemigo muy resistente"""
    def __init__(self, distancia):
        super().__init__("Gigante", vida=50, distancia=distancia, armadura=8)


def generar_oleada_enemigos(nivel=1):
    """Genera una oleada de enemigos según el nivel"""
    enemigos = []
    num_enemigos = 3 + nivel
    
    tipos = [Soldado, Caballero, Arquero]
    if nivel >= 3:
        tipos.append(Gigante)
    
    for i in range(num_enemigos):
        tipo = random.choice(tipos)
        distancia = random.randint(10, 50)
        enemigos.append(tipo(distancia))
    
    return enemigos
