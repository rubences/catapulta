"""
Módulo principal de la catapulta
"""

import random
from .materiales import Palo, Goma, Tapon, Corcho, Pegamento


class Catapulta:
    """Clase que representa una catapulta construida por el usuario"""
    
    def __init__(self, nombre="Mi Catapulta"):
        self.nombre = nombre
        self.palos = []
        self.gomas = []
        self.tapones = []
        self.corchos = []
        self.pegamento = None
        self.construida = False
    
    def agregar_palo(self, longitud):
        """Agrega un palo a la catapulta"""
        palo = Palo(longitud)
        self.palos.append(palo)
        print(f"✓ Palo agregado: {palo}")
    
    def agregar_goma(self, elasticidad):
        """Agrega una goma elástica"""
        if elasticidad < 1 or elasticidad > 10:
            print("⚠ La elasticidad debe estar entre 1 y 10")
            return
        goma = Goma(elasticidad)
        self.gomas.append(goma)
        print(f"✓ Goma agregada: {goma}")
    
    def agregar_tapon(self):
        """Agrega un tapón para estabilidad"""
        tapon = Tapon()
        self.tapones.append(tapon)
        print(f"✓ Tapón agregado: {tapon}")
    
    def agregar_corcho(self):
        """Agrega munición (corcho)"""
        corcho = Corcho()
        self.corchos.append(corcho)
        print(f"✓ Corcho agregado: {corcho}")
    
    def agregar_pegamento(self, calidad):
        """Agrega pegamento para unir las piezas"""
        if calidad < 1 or calidad > 10:
            print("⚠ La calidad debe estar entre 1 y 10")
            return
        self.pegamento = Pegamento(calidad)
        print(f"✓ Pegamento agregado: {self.pegamento}")
    
    def construir(self):
        """Intenta construir la catapulta con los materiales disponibles"""
        print("\n🔨 Intentando construir la catapulta...")
        
        # Validar requisitos mínimos
        errores = []
        if len(self.palos) < 2:
            errores.append("Se necesitan al menos 2 palos")
        if len(self.gomas) < 1:
            errores.append("Se necesita al menos 1 goma")
        if self.pegamento is None:
            errores.append("Se necesita pegamento para unir las piezas")
        if len(self.corchos) < 1:
            errores.append("Se necesita al menos 1 corcho como munición")
        
        if errores:
            print("❌ No se puede construir la catapulta:")
            for error in errores:
                print(f"   - {error}")
            return False
        
        # Calcular probabilidad de éxito basada en materiales
        probabilidad = 50  # Base
        probabilidad += len(self.tapones) * 10  # Cada tapón aumenta estabilidad
        probabilidad += self.pegamento.calidad * 3  # Pegamento de calidad ayuda
        probabilidad = min(95, probabilidad)  # Máximo 95%
        
        if random.randint(1, 100) <= probabilidad:
            self.construida = True
            print(f"✅ ¡Catapulta '{self.nombre}' construida con éxito!")
            self.mostrar_estadisticas()
            return True
        else:
            print(f"❌ La construcción falló. Probabilidad de éxito: {probabilidad}%")
            print("   Intenta agregar más tapones o mejor pegamento.")
            return False
    
    def calcular_potencia(self):
        """Calcula la potencia total de la catapulta"""
        if not self.construida:
            return 0
        
        potencia = sum(palo.potencia_base for palo in self.palos)
        impulso = sum(goma.impulso for goma in self.gomas)
        estabilidad = sum(tapon.estabilidad for tapon in self.tapones)
        
        potencia_total = potencia + impulso + estabilidad + self.pegamento.union
        return potencia_total
    
    def calcular_precision(self):
        """Calcula la precisión de la catapulta"""
        if not self.construida:
            return 0
        
        precision_base = 50
        precision_base += len(self.tapones) * 5  # Tapones mejoran precisión
        precision_base += self.pegamento.calidad * 2
        precision_base = min(95, precision_base)
        return precision_base
    
    def calcular_alcance_maximo(self):
        """Calcula el alcance máximo de la catapulta"""
        if not self.construida:
            return 0
        
        potencia = self.calcular_potencia()
        return int(potencia * 1.5)
    
    def disparar(self, objetivo):
        """Dispara la catapulta a un objetivo"""
        if not self.construida:
            print("❌ La catapulta no está construida")
            return False
        
        if len(self.corchos) == 0:
            print("❌ No hay munición disponible")
            return False
        
        if not objetivo.vivo:
            print(f"❌ {objetivo.nombre} ya está eliminado")
            return False
        
        print(f"\n🎯 Disparando a {objetivo.nombre} (Distancia: {objetivo.distancia}m)...")
        
        # Calcular si el disparo alcanza
        alcance_maximo = self.calcular_alcance_maximo()
        if objetivo.distancia > alcance_maximo:
            print(f"❌ ¡El disparo no llegó! Alcance máximo: {alcance_maximo}m")
            self.corchos.pop()
            return False
        
        # Calcular precisión
        precision = self.calcular_precision()
        distancia_factor = (1 - objetivo.distancia / alcance_maximo) * 100
        precision_final = (precision + distancia_factor) / 2
        
        if random.randint(1, 100) <= precision_final:
            # Impacto exitoso
            corcho = self.corchos.pop()
            potencia = self.calcular_potencia()
            danio = corcho.danio + int(potencia * 0.5)
            
            print(f"💥 ¡IMPACTO! Daño causado: {danio}")
            eliminado = objetivo.recibir_danio(danio)
            
            if eliminado:
                print(f"☠️  {objetivo.nombre} ha sido eliminado!")
            else:
                print(f"❤️  {objetivo.nombre} sobrevivió con {objetivo.vida} puntos de vida")
            
            return True
        else:
            print(f"❌ ¡Disparo fallido! Precisión: {precision_final:.1f}%")
            self.corchos.pop()
            return False
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas de la catapulta"""
        print(f"\n📊 Estadísticas de '{self.nombre}':")
        print(f"   Potencia: {self.calcular_potencia()}")
        print(f"   Precisión: {self.calcular_precision()}%")
        print(f"   Alcance máximo: {self.calcular_alcance_maximo()}m")
        print(f"   Munición disponible: {len(self.corchos)} corchos")
    
    def mostrar_inventario(self):
        """Muestra el inventario de materiales"""
        print(f"\n📦 Inventario de '{self.nombre}':")
        print(f"   Palos: {len(self.palos)}")
        print(f"   Gomas: {len(self.gomas)}")
        print(f"   Tapones: {len(self.tapones)}")
        print(f"   Corchos: {len(self.corchos)}")
        print(f"   Pegamento: {'Sí' if self.pegamento else 'No'}")
        print(f"   Estado: {'✅ Construida' if self.construida else '⚠️  No construida'}")
