# 🏰 Catapulta - Juego de Defensa del Castillo

Un juego interactivo en Python donde construyes tu propia catapulta usando programación orientada a objetos y la usas para defender tu castillo de oleadas de enemigos.

## 📋 Descripción

Construye tu catapulta personalizada eligiendo diferentes materiales y características. Cada decisión afecta la potencia, precisión y alcance de tu arma. Luego, enfréntate a oleadas de enemigos cada vez más difíciles para defender tu castillo.

## 🎮 Características

- **Sistema de construcción personalizable**: Elige materiales y sus características
- **Diferentes tipos de materiales**:
  - **Palos**: Estructura base (aumentan potencia según longitud)
  - **Gomas**: Impulso elástico (aumentan velocidad según elasticidad)
  - **Tapones**: Estabilidad (aumentan precisión)
  - **Corchos**: Munición para disparar
  - **Pegamento**: Une las piezas (calidad afecta construcción)

- **Variedad de enemigos**:
  - **Soldado**: Enemigo básico (20 HP, 2 armadura)
  - **Caballero**: Más protección (35 HP, 5 armadura)
  - **Arquero**: Rápido pero débil (15 HP, 1 armadura)
  - **Gigante**: Muy resistente (50 HP, 8 armadura) - Aparece desde nivel 3

- **Sistema de combate realista**:
  - Alcance basado en potencia
  - Precisión afectada por distancia
  - Daño reducido por armadura enemiga

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7 o superior

### Ejecutar el juego

```bash
python main.py
```

## 🎯 Cómo jugar

### 1. Construcción de la Catapulta

Al iniciar, deberás construir tu catapulta:

1. **Dale un nombre** a tu catapulta
2. **Agrega materiales**:
   - Al menos 2 palos (longitud: 10-50 cm)
   - Al menos 1 goma (elasticidad: 1-10)
   - Al menos 1 corcho (munición)
   - Pegamento (calidad: 1-10)
   - Tapones opcionales (mejoran precisión)

3. **Construye**: Una vez tengas los materiales mínimos, intenta construir
   - La probabilidad de éxito depende de la calidad del pegamento y número de tapones
   - Si fallas, puedes agregar más materiales e intentar de nuevo

### 2. Fase de Combate

Una vez construida tu catapulta:

1. **Aparecen enemigos**: Cada oleada tiene enemigos a diferentes distancias
2. **Selecciona objetivo**: Elige qué enemigo atacar
3. **Dispara**: El juego calcula si alcanzas y si aciertas
4. **Elimina todos los enemigos** para pasar a la siguiente oleada

### 3. Estrategia

- **Más palos largos** = Mayor potencia y alcance
- **Más gomas elásticas** = Mayor impulso
- **Más tapones** = Mayor precisión (más importante a largas distancias)
- **Mejor pegamento** = Mayor probabilidad de construcción exitosa
- **Muchos corchos** = Más intentos de disparo

## 📁 Estructura del Proyecto

```
catapulta/
├── main.py                      # Punto de entrada del juego
├── README.md                    # Este archivo
└── catapulta/                   # Paquete principal
    ├── __init__.py              # Inicialización del paquete
    ├── materiales.py            # Clases de materiales (Palo, Goma, etc.)
    ├── catapulta.py             # Clase principal Catapulta
    ├── enemigos.py              # Clases de enemigos
    └── juego.py                 # Controlador del juego
```

## 🏗️ Arquitectura (POO)

El proyecto utiliza programación orientada a objetos con las siguientes clases:

### Módulo `materiales.py`
- `Material`: Clase base abstracta
- `Palo`, `Goma`, `Tapon`, `Corcho`, `Pegamento`: Materiales específicos

### Módulo `catapulta.py`
- `Catapulta`: Clase principal que gestiona construcción y disparos

### Módulo `enemigos.py`
- `Enemigo`: Clase base
- `Soldado`, `Caballero`, `Arquero`, `Gigante`: Tipos de enemigos

### Módulo `juego.py`
- `Juego`: Controlador principal del flujo del juego

## 🎲 Mecánicas del Juego

### Cálculo de Potencia
```
Potencia = Σ(potencia_palos) + Σ(impulso_gomas) + Σ(estabilidad_tapones) + calidad_pegamento
```

### Cálculo de Precisión
```
Precisión_base = 50 + (tapones × 5) + (calidad_pegamento × 2)
Factor_distancia = (1 - distancia/alcance_máximo) × 100
Precisión_final = (Precisión_base + Factor_distancia) / 2
```

### Cálculo de Alcance
```
Alcance_máximo = Potencia × 1.5
```

### Cálculo de Daño
```
Daño_corcho = 5
Daño_total = Daño_corcho + (Potencia × 0.5)
Daño_real = max(0, Daño_total - armadura_enemigo)
```

## 📝 Ejemplo de Juego

```
🏗️  CONSTRUCTOR DE CATAPULTAS
================================

¿Cómo quieres llamar a tu catapulta? La Destructora

¿Qué material quieres agregar?
1. Palo → Agrego 2 palos de 40cm
2. Goma → Agrego 2 gomas de elasticidad 8
3. Tapón → Agrego 3 tapones
4. Corcho → Agrego 10 corchos
5. Pegamento → Agrego pegamento calidad 9
7. Construir catapulta

✅ ¡Catapulta 'La Destructora' construida con éxito!

📊 Estadísticas:
   Potencia: 113.5
   Precisión: 83%
   Alcance máximo: 170m
   Munición disponible: 10 corchos

⚔️  ¡Oleada 1 de enemigos!
   1. Soldado - Vida: 20/20, Distancia: 25m [Vivo]
   2. Arquero - Vida: 15/15, Distancia: 42m [Vivo]
   ...
```

## 🎯 Consejos

1. **No escatimes en materiales**: Más materiales = mejor catapulta
2. **Equilibrio**: Necesitas tanto potencia como precisión
3. **Gestiona tu munición**: No desperdicies corchos en objetivos lejanos si tu alcance es bajo
4. **Mejora gradual**: Cada oleada es más difícil, planifica bien tu construcción inicial

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de:
- Agregar nuevos tipos de materiales
- Crear nuevos enemigos
- Implementar power-ups
- Mejorar las mecánicas de combate
- Añadir gráficos o interfaz visual

## 📄 Licencia

Proyecto educativo de código abierto.

---

¡Diviértete construyendo y disparando tu catapulta! 🎯🏰