"""
Módulo principal de la catapulta
"""

import random
from enum import Enum
from .materiales import Palo, Goma, Tapon, Corcho, Pegamento


class EstadoCatapulta(Enum):
    """Estados posibles de la catapulta"""
    EN_CONSTRUCCION = "En construcción"
    LISTA = "Lista para usar"
    DANADA = "Dañada"
    DESTRUIDA = "Destruida"
    EN_MANTENIMIENTO = "En mantenimiento"


class Catapulta:
    """
    Clase que representa una catapulta construida por el usuario.
    
    ESTADO (Atributos que definen el estado interno):
        - nombre: Identificador de la catapulta
        - estado: Estado actual (EN_CONSTRUCCION, LISTA, DANADA, etc.)
        - componentes: Materiales que componen la catapulta
        - durabilidad: Resistencia actual de la estructura
        - disparos_realizados: Contador de disparos
        - nivel_desgaste: Degradación por uso
    
    CARACTERÍSTICAS (Atributos calculados o propiedades):
        - potencia: Capacidad de daño
        - alcance: Distancia máxima
        - precision: Exactitud del disparo
        - estabilidad: Resistencia a fallos
    
    COMPORTAMIENTO (Métodos que definen acciones):
        - construir(): Ensambla los componentes
        - disparar(): Lanza proyectiles
        - reparar(): Restaura durabilidad
        - mejorar(): Aumenta características
    """
    
    # Constantes de clase
    DURABILIDAD_MAXIMA = 100
    DESGASTE_POR_DISPARO = 5
    
    def __init__(self, nombre="Mi Catapulta"):
        # === ESTADO DE LA CATAPULTA ===
        self.nombre = nombre
        self._estado = EstadoCatapulta.EN_CONSTRUCCION
        
        # Componentes (materiales)
        self.palos = []
        self.gomas = []
        self.tapones = []
        self.corchos = []
        self.pegamento = None
        
        # Estado interno
        self._durabilidad = 0
        self._durabilidad_maxima = self.DURABILIDAD_MAXIMA
        self.disparos_realizados = 0
        self.nivel_desgaste = 0
        self.construida = False
        
        # Historial
        self.historial_disparos = []
        self.enemigos_eliminados = 0
    
    # === PROPIEDADES (CARACTERÍSTICAS) ===
    
    @property
    def estado(self):
        """Obtiene el estado actual de la catapulta"""
        return self._estado
    
    @property
    def durabilidad(self):
        """Obtiene la durabilidad actual"""
        return self._durabilidad
    
    @property
    def durabilidad_porcentaje(self):
        """Obtiene el porcentaje de durabilidad"""
        return (self._durabilidad / self._durabilidad_maxima) * 100 if self._durabilidad_maxima > 0 else 0
    
    @property
    def potencia(self):
        """Calcula la potencia total de la catapulta"""
        if not self.construida:
            return 0
        
        potencia_base = sum(palo.potencia_base for palo in self.palos)
        impulso = sum(goma.impulso for goma in self.gomas)
        bonus_pegamento = self.pegamento.calidad * 2 if self.pegamento else 0
        
        # La durabilidad afecta la potencia
        factor_durabilidad = self.durabilidad_porcentaje / 100
        
        return int((potencia_base + impulso + bonus_pegamento) * factor_durabilidad)
    
    @property
    def alcance(self):
        """Calcula el alcance máximo en metros"""
        if not self.construida:
            return 0
        
        longitud_total = sum(palo.longitud for palo in self.palos)
        elasticidad_total = sum(goma.elasticidad for goma in self.gomas)
        
        alcance_base = (longitud_total * 0.5) + (elasticidad_total * 3)
        factor_durabilidad = self.durabilidad_porcentaje / 100
        
        return int(alcance_base * factor_durabilidad)
    
    @property
    def precision(self):
        """Calcula la precisión del disparo (0-100)"""
        if not self.construida:
            return 0
        
        estabilidad_tapones = len(self.tapones) * 10
        calidad_pegamento = self.pegamento.calidad * 5 if self.pegamento else 0
        penalizacion_desgaste = self.nivel_desgaste * 2
        
        precision_total = min(95, 50 + estabilidad_tapones + calidad_pegamento - penalizacion_desgaste)
        return max(5, precision_total)
    
    @property
    def estabilidad(self):
        """Calcula la estabilidad estructural"""
        if not self.construida:
            return 0
        
        estabilidad_base = sum(tapon.estabilidad for tapon in self.tapones)
        calidad_union = self.pegamento.union if self.pegamento else 0
        
        return estabilidad_base + calidad_union
    
    # === COMPORTAMIENTO (MÉTODOS DE CONSTRUCCIÓN) ===
    
    def agregar_palo(self, longitud):
        """Agrega un palo a la catapulta"""
        if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
            print(f"⚠ No se pueden agregar componentes. Estado: {self._estado.value}")
            return False
        
        palo = Palo(longitud)
        self.palos.append(palo)
        print(f"✓ Palo agregado: {palo}")
        return True
    
    def agregar_goma(self, elasticidad):
        """Agrega una goma elástica"""
        if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
            print(f"⚠ No se pueden agregar componentes. Estado: {self._estado.value}")
            return False
        
        if elasticidad < 1 or elasticidad > 10:
            print("⚠ La elasticidad debe estar entre 1 y 10")
            return False
        
        goma = Goma(elasticidad)
        self.gomas.append(goma)
        print(f"✓ Goma agregada: {goma}")
        return True
    
    def agregar_tapon(self):
        """Agrega un tapón para estabilidad"""
        if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
            print(f"⚠ No se pueden agregar componentes. Estado: {self._estado.value}")
            return False
        
        tapon = Tapon()
        self.tapones.append(tapon)
        print(f"✓ Tapón agregado: {tapon}")
        return True
    
    def agregar_corcho(self):
        """Agrega munición (corcho)"""
        corcho = Corcho()
        self.corchos.append(corcho)
        print(f"✓ Corcho agregado: {corcho}")
        return True
    
    def agregar_pegamento(self, calidad):
        """Agrega pegamento para unir las piezas"""
        if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
            print(f"⚠ No se pueden agregar componentes. Estado: {self._estado.value}")
            return False
        
        if calidad < 1 or calidad > 10:
            print("⚠ La calidad debe estar entre 1 y 10")
            return False
        
        self.pegamento = Pegamento(calidad)
        print(f"✓ Pegamento agregado: {self.pegamento}")
        return True
    
    # === COMPORTAMIENTO (MÉTODOS PRINCIPALES) ===
    
    def construir(self):
        """
        Intenta construir la catapulta con los materiales disponibles.
        Cambia el estado de EN_CONSTRUCCION a LISTA si tiene éxito.
        """
        print("\n🔨 Intentando construir la catapulta...")
        
        if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
            print(f"⚠ La catapulta ya está en estado: {self._estado.value}")
            return False
        
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
            self._estado = EstadoCatapulta.LISTA
            
            # Calcular durabilidad inicial
            resistencia_materiales = sum(palo.resistencia for palo in self.palos)
            resistencia_materiales += sum(goma.resistencia for goma in self.gomas)
            resistencia_materiales += self.pegamento.resistencia if self.pegamento else 0
            
            self._durabilidad = min(self.DURABILIDAD_MAXIMA, resistencia_materiales + (len(self.tapones) * 10))
            self._durabilidad_maxima = self._durabilidad
            
            print(f"✅ ¡Catapulta '{self.nombre}' construida con éxito!")
            self.mostrar_estadisticas()
            return True
        else:
            print(f"❌ La construcción falló. Probabilidad de éxito: {probabilidad}%")
            print("   Intenta agregar más tapones o mejor pegamento.")
            return False
    
    def disparar(self, enemigo):
        """
        Dispara un proyectil hacia un enemigo.
        Modifica el estado de durabilidad y desgaste.
        """
        if self._estado == EstadoCatapulta.DESTRUIDA:
            print("❌ La catapulta está destruida. Necesita reparación completa.")
            return False
        
        if self._estado == EstadoCatapulta.EN_CONSTRUCCION:
            print("❌ La catapulta aún no está construida.")
            return False
        
        if len(self.corchos) == 0:
            print("❌ No hay munición disponible.")
            return False
        
        print(f"\n🎯 Preparando disparo contra {enemigo.nombre}...")
        
        # Verificar si la catapulta puede alcanzar al enemigo
        if enemigo.distancia > self.alcance:
            print(f"❌ Enemigo fuera de alcance. Distancia: {enemigo.distancia}m, Alcance: {self.alcance}m")
            self._aplicar_desgaste()
            return False
        
        # Calcular si el disparo acierta
        acierto = random.randint(1, 100) <= self.precision
        
        if acierto:
            # Usar un corcho como munición
            corcho = self.corchos.pop(0)
            danio = corcho.danio + (self.potencia // 10)
            
            print(f"✅ ¡Disparo acertado! Daño: {danio}")
            eliminado = enemigo.recibir_danio(danio)
            
            if eliminado:
                self.enemigos_eliminados += 1
                print(f"💀 ¡{enemigo.nombre} eliminado!")
            
            self.historial_disparos.append({
                'enemigo': enemigo.nombre,
                'acierto': True,
                'danio': danio,
                'eliminado': eliminado
            })
        else:
            print(f"❌ ¡Disparo fallado! Precisión: {self.precision}%")
            self.historial_disparos.append({
                'enemigo': enemigo.nombre,
                'acierto': False,
                'danio': 0,
                'eliminado': False
            })
        
        self.disparos_realizados += 1
        self._aplicar_desgaste()
        
        return acierto
    
    def _aplicar_desgaste(self):
        """Aplica desgaste a la catapulta después de cada disparo"""
        self._durabilidad -= self.DESGASTE_POR_DISPARO
        self.nivel_desgaste += 1
        
        # Actualizar estado según durabilidad
        if self._durabilidad <= 0:
            self._durabilidad = 0
            self._estado = EstadoCatapulta.DESTRUIDA
            print("💔 ¡La catapulta se ha destruido!")
        elif self._durabilidad < self._durabilidad_maxima * 0.3:
            self._estado = EstadoCatapulta.DANADA
            print("⚠️  La catapulta está muy dañada. Considera repararla.")
        
        print(f"   Durabilidad: {self._durabilidad}/{self._durabilidad_maxima} ({self.durabilidad_porcentaje:.1f}%)")
    
    def reparar(self):
        """Repara la catapulta restaurando su durabilidad"""
        if self._estado == EstadoCatapulta.EN_CONSTRUCCION:
            print("⚠ La catapulta no está construida aún.")
            return False
        
        if self._estado == EstadoCatapulta.DESTRUIDA:
            print("🔧 Reparación completa necesaria...")
            costo = 3
        else:
            print("🔧 Reparando catapulta...")
            costo = 1
        
        if len(self.corchos) < costo:
            print(f"❌ Se necesitan {costo} corchos para la reparación.")
            return False
        
        # Usar corchos como material de reparación
        for _ in range(costo):
            self.corchos.pop()
        
        restauracion = self._durabilidad_maxima * 0.5
        self._durabilidad = min(self._durabilidad_maxima, self._durabilidad + restauracion)
        self.nivel_desgaste = max(0, self.nivel_desgaste - 5)
        
        if self._estado == EstadoCatapulta.DESTRUIDA:
            self._estado = EstadoCatapulta.LISTA
        elif self._estado == EstadoCatapulta.DANADA:
            if self.durabilidad_porcentaje > 50:
                self._estado = EstadoCatapulta.LISTA
        
        print(f"✅ Reparación completada. Durabilidad: {self._durabilidad}/{self._durabilidad_maxima}")
        return True
    
    def mejorar(self, tipo_mejora):
        """
        Mejora la catapulta agregando más componentes.
        Requiere que la catapulta esté en mantenimiento.
        """
        if self._estado == EstadoCatapulta.DESTRUIDA:
            print("❌ No se puede mejorar una catapulta destruida. Repárala primero.")
            return False
        
        print(f"⚡ Mejorando catapulta: {tipo_mejora}...")
        
        if tipo_mejora == "refuerzo":
            self.agregar_tapon()
            self._durabilidad_maxima += 10
            print("✅ Catapulta reforzada. Durabilidad máxima aumentada.")
        elif tipo_mejora == "potencia":
            if not self.agregar_goma(random.randint(7, 10)):
                return False
            print("✅ Potencia mejorada.")
        else:
            print("⚠ Tipo de mejora no reconocido.")
            return False
        
        return True
    
    def calcular_potencia(self):
        """Método legacy - usa la propiedad potencia"""
        return self.potencia
    
    def calcular_precision(self):
        """Método legacy - usa la propiedad precision"""
        return self.precision
    
    def calcular_alcance_maximo(self):
        """Método legacy - usa la propiedad alcance"""
        return self.alcance
    
    # === MÉTODOS DE VISUALIZACIÓN ===
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas completas de la catapulta"""
        print(f"\n{'='*60}")
        print(f"📊 ESTADÍSTICAS DE '{self.nombre}'")
        print(f"{'='*60}")
        
        # Estado
        print(f"\n🔸 ESTADO: {self._estado.value}")
        print(f"   Durabilidad: {self._durabilidad}/{self._durabilidad_maxima} ({self.durabilidad_porcentaje:.1f}%)")
        print(f"   Disparos realizados: {self.disparos_realizados}")
        print(f"   Nivel de desgaste: {self.nivel_desgaste}")
        print(f"   Enemigos eliminados: {self.enemigos_eliminados}")
        
        # Características
        print(f"\n🔸 CARACTERÍSTICAS:")
        print(f"   Potencia: {self.potencia}")
        print(f"   Alcance: {self.alcance}m")
        print(f"   Precisión: {self.precision}%")
        print(f"   Estabilidad: {self.estabilidad:.1f}")
        
        # Componentes
        print(f"\n� COMPONENTES:")
        print(f"   Palos: {len(self.palos)}")
        print(f"   Gomas: {len(self.gomas)}")
        print(f"   Tapones: {len(self.tapones)}")
        print(f"   Pegamento: {'Calidad ' + str(self.pegamento.calidad) if self.pegamento else 'No'}")
        
        # Munición
        print(f"\n🔸 MUNICIÓN:")
        print(f"   Corchos disponibles: {len(self.corchos)}")
        
        print(f"{'='*60}\n")
    
    def mostrar_inventario(self):
        """Muestra el inventario de materiales"""
        print(f"\n� Inventario de '{self.nombre}':")
        print(f"   Palos: {len(self.palos)}")
        print(f"   Gomas: {len(self.gomas)}")
        print(f"   Tapones: {len(self.tapones)}")
        print(f"   Corchos: {len(self.corchos)}")
        print(f"   Pegamento: {'Sí' if self.pegamento else 'No'}")
        print(f"   Estado: {self._estado.value}")
    
    def mostrar_historial(self):
        """Muestra el historial de disparos"""
        if not self.historial_disparos:
            print("\n📜 No hay historial de disparos.")
            return
        
        print(f"\n📜 Historial de disparos ({len(self.historial_disparos)} disparos):")
        for i, disparo in enumerate(self.historial_disparos[-10:], 1):  # Últimos 10
            estado = "✅ ACERTÓ" if disparo['acierto'] else "❌ FALLÓ"
            eliminado = " - ☠️ ELIMINADO" if disparo.get('eliminado') else ""
            print(f"   {i}. vs {disparo['enemigo']}: {estado} (Daño: {disparo['danio']}){eliminado}")
    
    def __str__(self):
        """Representación en string de la catapulta"""
        return (f"Catapulta '{self.nombre}' - Estado: {self._estado.value} - "
                f"Potencia: {self.potencia} - Alcance: {self.alcance}m - "
                f"Disparos: {self.disparos_realizados}")
