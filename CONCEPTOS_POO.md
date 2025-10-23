# 📚 Conceptos de Programación Orientada a Objetos en Catapulta

Este proyecto demuestra los tres pilares fundamentales de la POO aplicados a una catapulta de juego.

---

## 🎯 1. ESTADO (State)

El **estado** representa los datos internos de un objeto que pueden cambiar durante su vida útil.

### En la Catapulta:

#### Atributos de Estado Principal:
```python
self._estado = EstadoCatapulta.EN_CONSTRUCCION  # Estado actual
self._durabilidad = 0                           # Resistencia actual
self.disparos_realizados = 0                    # Contador de uso
self.nivel_desgaste = 0                         # Degradación acumulada
```

#### Estados Posibles (Enum):
- `EN_CONSTRUCCION`: La catapulta está siendo ensamblada
- `LISTA`: Funcional y lista para usar
- `DANADA`: Funciona pero con eficiencia reducida
- `DESTRUIDA`: No puede usarse sin reparación
- `EN_MANTENIMIENTO`: Está siendo reparada

#### Componentes (Estado de Composición):
```python
self.palos = []      # Lista de palos agregados
self.gomas = []      # Lista de gomas elásticas
self.tapones = []    # Lista de tapones de refuerzo
self.corchos = []    # Munición disponible
self.pegamento = None # Material de unión
```

#### ¿Por qué es importante?
El estado determina **qué puede hacer** la catapulta:
- Si está `EN_CONSTRUCCION`, no puede disparar
- Si está `DESTRUIDA`, necesita reparación
- La durabilidad afecta la potencia y precisión

---

## ⚙️ 2. COMPORTAMIENTO (Behavior)

El **comportamiento** son las acciones que un objeto puede realizar, implementadas como métodos.

### Comportamientos de Construcción:

#### `agregar_palo(longitud)` - Agregar componentes
```python
def agregar_palo(self, longitud):
    """Agrega un palo verificando el estado"""
    if self._estado != EstadoCatapulta.EN_CONSTRUCCION:
        print("⚠ No se pueden agregar componentes")
        return False
    
    palo = Palo(longitud)
    self.palos.append(palo)
    return True
```

### Comportamientos Principales:

#### `construir()` - Ensambla la catapulta
```python
def construir(self):
    """Cambia el estado de EN_CONSTRUCCION a LISTA"""
    # 1. Validar materiales mínimos
    # 2. Calcular probabilidad de éxito
    # 3. Cambiar estado si exitoso
    # 4. Calcular durabilidad inicial
```

#### `disparar(enemigo)` - Lanza proyectiles
```python
def disparar(self, enemigo):
    """Ataca a un enemigo y aplica desgaste"""
    # 1. Verificar estado (¿puede disparar?)
    # 2. Calcular si alcanza al enemigo
    # 3. Calcular precisión del disparo
    # 4. Aplicar daño si acierta
    # 5. Reducir durabilidad (desgaste)
    # 6. Actualizar historial
```

#### `reparar()` - Restaura durabilidad
```python
def reparar(self):
    """Restaura durabilidad usando recursos"""
    # 1. Verificar recursos disponibles
    # 2. Restaurar durabilidad
    # 3. Cambiar estado si es necesario
```

#### `mejorar(tipo)` - Añade mejoras
```python
def mejorar(self, tipo_mejora):
    """Mejora características de la catapulta"""
    # Permite agregar componentes después de construir
```

### ¿Por qué es importante?
- Los métodos **encapsulan** la lógica compleja
- Cada acción puede **modificar el estado** interno
- Se valida que la acción sea válida según el estado actual
- Se mantiene la **coherencia** del objeto

---

## 📊 3. CARACTERÍSTICAS (Properties)

Las **características** son valores calculados dinámicamente basándose en el estado actual.

### Usando `@property` - Propiedades Calculadas:

#### `potencia` - Capacidad de daño
```python
@property
def potencia(self):
    """Calcula potencia basándose en componentes y durabilidad"""
    if not self.construida:
        return 0
    
    # Suma de componentes
    potencia_base = sum(palo.potencia_base for palo in self.palos)
    impulso = sum(goma.impulso for goma in self.gomas)
    bonus_pegamento = self.pegamento.calidad * 2
    
    # Factor de durabilidad afecta la potencia
    factor_durabilidad = self.durabilidad_porcentaje / 100
    
    return int((potencia_base + impulso + bonus_pegamento) * factor_durabilidad)
```

#### `alcance` - Distancia máxima
```python
@property
def alcance(self):
    """Calcula alcance dinámicamente"""
    longitud_total = sum(palo.longitud for palo in self.palos)
    elasticidad_total = sum(goma.elasticidad for goma in self.gomas)
    
    alcance_base = (longitud_total * 0.5) + (elasticidad_total * 3)
    factor_durabilidad = self.durabilidad_porcentaje / 100
    
    return int(alcance_base * factor_durabilidad)
```

#### `precision` - Exactitud de los disparos
```python
@property
def precision(self):
    """Calcula precisión considerando varios factores"""
    estabilidad_tapones = len(self.tapones) * 10
    calidad_pegamento = self.pegamento.calidad * 5
    penalizacion_desgaste = self.nivel_desgaste * 2  # ¡El desgaste afecta!
    
    precision_total = 50 + estabilidad_tapones + calidad_pegamento - penalizacion_desgaste
    return max(5, min(95, precision_total))
```

#### `durabilidad_porcentaje` - Estado de salud
```python
@property
def durabilidad_porcentaje(self):
    """Porcentaje de durabilidad actual"""
    return (self._durabilidad / self._durabilidad_maxima) * 100
```

### ¿Por qué usar Properties?

1. **Se calculan en tiempo real**: Siempre reflejan el estado actual
2. **Sintaxis limpia**: Se usan como atributos (`catapulta.potencia`)
3. **No almacenan datos redundantes**: Se calculan cuando se necesitan
4. **Encapsulación**: Pueden cambiar internamente sin afectar el código externo

---

## 🔄 Interacción entre Estado, Comportamiento y Características

### Ejemplo Completo: Secuencia de Disparo

```python
# ESTADO INICIAL
catapulta._durabilidad = 100
catapulta._estado = EstadoCatapulta.LISTA
catapulta.disparos_realizados = 0

# CARACTERÍSTICA (antes del disparo)
print(catapulta.potencia)  # → 85 (100% durabilidad)
print(catapulta.precision) # → 75%

# COMPORTAMIENTO (disparar)
catapulta.disparar(enemigo)
# Internamente:
# 1. Verifica estado (¿puede disparar?)
# 2. Calcula si acierta usando `precision`
# 3. Usa `potencia` para calcular daño
# 4. Aplica desgaste: durabilidad -= 5
# 5. Actualiza disparos_realizados += 1

# ESTADO MODIFICADO
catapulta._durabilidad = 95
catapulta.disparos_realizados = 1

# CARACTERÍSTICAS (después del disparo)
print(catapulta.potencia)  # → 81 (95% durabilidad - ¡ha bajado!)
print(catapulta.precision) # → 73% (desgaste afecta)
```

### Flujo de Vida de una Catapulta

```
┌─────────────────────┐
│  EN_CONSTRUCCION    │ ← Estado inicial
└──────────┬──────────┘
           │ agregar_palo()    ← Comportamiento
           │ agregar_goma()
           │ agregar_pegamento()
           ▼
    ┌──────────────┐
    │  construir() │ ← Comportamiento
    └──────┬───────┘
           ▼
┌─────────────────────┐
│       LISTA         │ ← Estado: lista para usar
└──────────┬──────────┘
           │ disparar()        ← Comportamiento
           │ (durabilidad ↓)   ← Estado cambia
           ▼
┌─────────────────────┐
│      DANADA         │ ← Estado: durabilidad < 30%
└──────────┬──────────┘
           │ reparar()         ← Comportamiento
           ▼
┌─────────────────────┐
│       LISTA         │ ← Estado restaurado
└─────────────────────┘
```

---

## 🎓 Conceptos Adicionales POO Implementados

### 1. Encapsulación
```python
self._durabilidad      # Atributo privado (convención _)
@property
def durabilidad(self): # Acceso controlado
    return self._durabilidad
```

### 2. Herencia
```python
class Material:                    # Clase base
    def __init__(self, nombre, resistencia, peso):
        self.nombre = nombre
        # ...

class Palo(Material):              # Hereda de Material
    def __init__(self, longitud):
        super().__init__("Palo", resistencia=10, peso=5)
        self.longitud = longitud
```

### 3. Polimorfismo
```python
# Todos los enemigos tienen recibir_danio()
soldado.recibir_danio(10)
gigante.recibir_danio(10)  # Mismo método, diferente resultado
```

### 4. Composición
```python
# La catapulta está COMPUESTA por materiales
self.palos = []     # Tiene palos
self.gomas = []     # Tiene gomas
self.pegamento = None  # Tiene pegamento
```

---

## 🚀 Ejercicios Propuestos

1. **Agregar nuevo estado**: `EN_REPARACION` que bloquee disparos
2. **Nueva característica**: `eficiencia` que compare disparos exitosos vs totales
3. **Nuevo comportamiento**: `desmontar()` que devuelva materiales
4. **Nueva property**: `vida_util` que calcule disparos restantes estimados

---

## 📖 Resumen

| Concepto | ¿Qué es? | Ejemplo en Catapulta |
|----------|----------|----------------------|
| **Estado** | Datos que cambian | `_durabilidad`, `_estado`, `disparos_realizados` |
| **Comportamiento** | Acciones/métodos | `construir()`, `disparar()`, `reparar()` |
| **Características** | Valores calculados | `potencia`, `alcance`, `precision` (properties) |

### La clave está en entender:
- El **ESTADO** define "cómo está" el objeto ahora
- El **COMPORTAMIENTO** define "qué puede hacer" el objeto
- Las **CARACTERÍSTICAS** definen "qué tan capaz es" el objeto (calculado dinámicamente)

¡Estos tres conceptos trabajando juntos crean objetos robustos y realistas! 🎯
