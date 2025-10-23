# 🏰 Catapulta POO - Sistema Mejorado

## 🎯 Mejoras Implementadas

He mejorado completamente el sistema de la catapulta para demostrar claramente los **tres pilares de POO**:

### 1. 🔸 ESTADO (State)

La catapulta ahora tiene un **sistema de estados robusto**:

#### Estados Posibles (usando Enum):
```python
class EstadoCatapulta(Enum):
    EN_CONSTRUCCION = "En construcción"
    LISTA = "Lista para usar"
    DANADA = "Dañada"
    DESTRUIDA = "Destruida"
    EN_MANTENIMIENTO = "En mantenimiento"
```

#### Atributos de Estado:
```python
self._estado = EstadoCatapulta.EN_CONSTRUCCION  # Estado actual
self._durabilidad = 0                           # Salud actual
self.disparos_realizados = 0                    # Contador de uso
self.nivel_desgaste = 0                         # Degradación
self.enemigos_eliminados = 0                    # Estadística
self.historial_disparos = []                    # Registro de acciones
```

**Flujo de estados:**
```
EN_CONSTRUCCION → LISTA → DANADA → DESTRUIDA
                     ↓
                  REPARAR
                     ↑
```

### 2. ⚙️ COMPORTAMIENTO (Behavior)

Métodos que definen **acciones** y modifican el estado:

#### Construcción:
- `agregar_palo(longitud)` - Añade componentes (solo en EN_CONSTRUCCION)
- `agregar_goma(elasticidad)` - Añade gomas (solo en EN_CONSTRUCCION)
- `agregar_tapon()` - Añade refuerzos (solo en EN_CONSTRUCCION)
- `agregar_pegamento(calidad)` - Material de unión (solo en EN_CONSTRUCCION)

#### Acciones Principales:
- `construir()` - Ensambla la catapulta y cambia estado a LISTA
- `disparar(enemigo)` - Lanza proyectil y aplica desgaste
- `reparar()` - Restaura durabilidad usando recursos
- `mejorar(tipo)` - Añade mejoras post-construcción

#### Ejemplo de Comportamiento con Validación de Estado:
```python
def disparar(self, enemigo):
    # 1. Verificar estado
    if self._estado == EstadoCatapulta.DESTRUIDA:
        print("❌ La catapulta está destruida")
        return False
    
    # 2. Ejecutar acción
    acierto = self._calcular_acierto()
    
    # 3. Modificar estado
    self._durabilidad -= 5
    self.disparos_realizados += 1
    
    # 4. Actualizar estado si es necesario
    if self._durabilidad <= 0:
        self._estado = EstadoCatapulta.DESTRUIDA
```

### 3. 📊 CARACTERÍSTICAS (Properties)

Propiedades **calculadas dinámicamente** usando `@property`:

#### `potencia` - Se recalcula según durabilidad:
```python
@property
def potencia(self):
    potencia_base = sum(palo.potencia_base for palo in self.palos)
    impulso = sum(goma.impulso for goma in self.gomas)
    
    # La durabilidad afecta la potencia
    factor_durabilidad = self.durabilidad_porcentaje / 100
    
    return int((potencia_base + impulso) * factor_durabilidad)
```

#### `alcance` - Distancia máxima:
```python
@property
def alcance(self):
    longitud_total = sum(palo.longitud for palo in self.palos)
    elasticidad_total = sum(goma.elasticidad for goma in self.gomas)
    
    alcance_base = (longitud_total * 0.5) + (elasticidad_total * 3)
    factor_durabilidad = self.durabilidad_porcentaje / 100
    
    return int(alcance_base * factor_durabilidad)
```

#### `precision` - Afectada por desgaste:
```python
@property
def precision(self):
    estabilidad_tapones = len(self.tapones) * 10
    calidad_pegamento = self.pegamento.calidad * 5
    penalizacion_desgaste = self.nivel_desgaste * 2  # ¡El desgaste afecta!
    
    return max(5, min(95, 50 + estabilidad_tapones + calidad_pegamento - penalizacion_desgaste))
```

## 🔄 Ejemplo Completo de Interacción

```python
# ESTADO INICIAL
catapulta = Catapulta("Mi Catapulta")
print(catapulta.estado)  # → EN_CONSTRUCCION

# COMPORTAMIENTO: Construcción
catapulta.agregar_palo(30)
catapulta.agregar_goma(8)
catapulta.agregar_pegamento(7)
catapulta.construir()

# ESTADO CAMBIADO
print(catapulta.estado)           # → LISTA
print(catapulta.durabilidad)      # → 100

# CARACTERÍSTICAS (calculadas dinámicamente)
print(catapulta.potencia)         # → 125
print(catapulta.alcance)          # → 45m
print(catapulta.precision)        # → 75%

# COMPORTAMIENTO: Disparo
catapulta.disparar(enemigo)

# ESTADO MODIFICADO
print(catapulta.durabilidad)      # → 95
print(catapulta.disparos_realizados)  # → 1

# CARACTERÍSTICAS RECALCULADAS AUTOMÁTICAMENTE
print(catapulta.potencia)         # → 119 (¡ha bajado!)
print(catapulta.alcance)          # → 43m (¡reducido!)
print(catapulta.precision)        # → 73% (¡afectado por desgaste!)

# Múltiples disparos...
for _ in range(19):
    catapulta.disparar(enemigo)

# ESTADO CRÍTICO
print(catapulta.estado)           # → DESTRUIDA
print(catapulta.durabilidad)      # → 0

# COMPORTAMIENTO: Reparación
catapulta.reparar()

# ESTADO RESTAURADO
print(catapulta.estado)           # → LISTA
print(catapulta.durabilidad)      # → 50
```

## 📈 Nuevas Funcionalidades

### 1. Sistema de Durabilidad
- Cada disparo reduce durabilidad en 5 puntos
- Cuando durabilidad < 30%, estado cambia a DANADA
- Cuando durabilidad = 0, estado cambia a DESTRUIDA
- La durabilidad afecta directamente potencia, alcance y precisión

### 2. Sistema de Desgaste
- Contador de desgaste que aumenta con cada uso
- Afecta negativamente la precisión
- Se puede reducir con reparaciones

### 3. Historial de Disparos
```python
catapulta.mostrar_historial()
# Muestra:
# 1. vs Caballero: ✅ ACERTÓ (Daño: 62) - ☠️ ELIMINADO
# 2. vs Soldado: ✅ ACERTÓ (Daño: 59) - ☠️ ELIMINADO
# 3. vs Arquero: ❌ FALLÓ (Daño: 0)
```

### 4. Sistema de Reparación
- Usa corchos como material de reparación
- Restaura 50% de la durabilidad máxima
- Reduce el nivel de desgaste
- Cambia el estado de DESTRUIDA a LISTA

### 5. Sistema de Mejoras
```python
catapulta.mejorar("refuerzo")   # Añade tapón, aumenta durabilidad máxima
catapulta.mejorar("potencia")   # Añade goma de alta elasticidad
```

### 6. Estadísticas Completas
```python
catapulta.mostrar_estadisticas()
```
Muestra:
- Estado actual
- Durabilidad (valor y porcentaje)
- Disparos realizados
- Nivel de desgaste
- Enemigos eliminados
- Características (potencia, alcance, precisión, estabilidad)
- Componentes instalados
- Munición disponible

## 🎮 Nuevas Opciones en el Juego

Durante el combate ahora puedes:
1. **Disparar** - Ataca a un enemigo
2. **Ver enemigos** - Lista de objetivos disponibles
3. **Reparar catapulta** - Restaura durabilidad (cuesta 1 corcho)
4. **Ver historial** - Muestra todos los disparos realizados
5. **Mejorar catapulta** - Añade componentes adicionales
6. **Abandonar** - Termina la partida

## 📊 Visualización del Estado

El juego ahora muestra constantemente:
```
============================================================
📊 ESTADÍSTICAS DE 'Mi Catapulta'
============================================================

🔸 ESTADO: Lista para usar
   Durabilidad: 85/100 (85.0%)
   Disparos realizados: 3
   Nivel de desgaste: 3
   Enemigos eliminados: 2

🔸 CARACTERÍSTICAS:
   Potencia: 484
   Alcance: 176m
   Precisión: 95%
   Estabilidad: 21.0

🔸 COMPONENTES:
   Palos: 7
   Gomas: 4
   Tapones: 2
   Pegamento: Calidad 10

🔸 MUNICIÓN:
   Corchos disponibles: 2
============================================================
```

## 🎓 Conceptos POO Demostrados

### Encapsulación
```python
self._durabilidad      # Atributo privado
self._estado           # Atributo privado

@property
def durabilidad(self): # Acceso controlado
    return self._durabilidad
```

### Validación de Estado
```python
if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
    print("⚠ No se pueden agregar componentes")
    return False
```

### Properties Calculadas
```python
@property
def potencia(self):
    # Se calcula dinámicamente cada vez que se accede
    return self._calcular_potencia_actual()
```

### Flujo de Estado Consistente
- Los métodos verifican el estado antes de actuar
- Las acciones modifican el estado de forma controlada
- El estado determina qué acciones son posibles

## 📚 Documentación Completa

Ver [`CONCEPTOS_POO.md`](CONCEPTOS_POO.md) para:
- Explicación detallada de cada concepto
- Ejemplos de código comentados
- Diagramas de flujo de estados
- Ejercicios propuestos

## 🚀 Próximas Mejoras Posibles

1. Estado `EN_MANTENIMIENTO` funcional
2. Diferentes tipos de munición (piedras, bolas de fuego, etc.)
3. Sistema de experiencia y niveles para la catapulta
4. Guardar/cargar partidas
5. Modo multijugador

---

**¡Ahora la catapulta es un objeto vivo que cambia y evoluciona durante el juego!** 🎯🏰
