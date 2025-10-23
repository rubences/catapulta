# 🎮 Catapulta - Versión con Interfaz Gráfica

## ✨ Nueva Versión con GUI usando Tkinter

He añadido una **interfaz gráfica completa** al juego usando `tkinter`, mostrando visualmente todos los conceptos de POO.

---

## 🚀 Cómo Ejecutar

### Versión Gráfica (Recomendada):
```bash
python main_gui.py
```

### Versión Terminal (Original):
```bash
python main.py
```

---

## 🎨 Características de la Interfaz Gráfica

### 📊 Panel Izquierdo - Constructor y Estado

#### 🔨 Constructor de Catapulta:
- **Nombre**: Personaliza el nombre de tu catapulta
- **Palos**: Selector de longitud (10-50 cm)
- **Gomas**: Selector de elasticidad (1-10)
- **Tapones**: Botón para agregar estabilidad
- **Corchos**: Selector de cantidad de munición
- **Pegamento**: Selector de calidad (1-10)
- **Botón Construir**: Ensambla la catapulta
- **Inventario**: Vista en tiempo real de materiales

#### 📊 Estado de la Catapulta:
- **Barra de Durabilidad** (verde): Muestra la salud actual
- **Barra de Potencia** (azul): Capacidad de daño
- **Barra de Precisión** (morado): Probabilidad de acierto
- **Alcance**: Distancia máxima en metros
- **Munición**: Corchos disponibles
- **Estadísticas**: Disparos, desgaste, enemigos eliminados
- **Botones**:
  - 🔧 **Reparar**: Restaura durabilidad
  - ⚡ **Mejorar**: Añade refuerzos o potencia

### ⚔️ Panel Derecho - Campo de Batalla

#### 🎯 Campo de Batalla Visual:
- **Catapulta**: Dibujada en la izquierda
  - Color indica estado (marrón=bien, naranja=dañada, gris=destruida)
  - Muestra el nombre
- **Enemigos**: Dibujados según su distancia
  - Soldados (azul)
  - Caballeros (gris)
  - Arqueros (verde)
  - Gigantes (morado)
  - Barras de vida individuales
  - Distancia mostrada
- **Información**: Nivel y puntos en la parte superior
- **Botón DISPARAR**: Para atacar al enemigo seleccionado

#### 👾 Panel de Enemigos:
- **Lista de Enemigos**: Muestra todos los enemigos vivos
  - ❤️ Vivo / 💀 Muerto
  - HP actual/máximo
  - Distancia
- **Botón Generar Oleada**: Crea nuevos enemigos

---

## 🎮 Cómo Jugar

### 1️⃣ Construir la Catapulta

1. **Personaliza el nombre** de tu catapulta
2. **Agrega materiales** usando los selectores y botones:
   - Mínimo: 2 palos, 1 goma, 1 pegamento, 1 corcho
   - Recomendado: Varios de cada uno
3. **Observa el inventario** que se actualiza en tiempo real
4. **Click en "CONSTRUIR CATAPULTA"**
5. ✅ Si tiene éxito, verás la catapulta en el campo de batalla

### 2️⃣ Generar Enemigos

1. **Click en "GENERAR OLEADA DE ENEMIGOS"**
2. Aparecerán enemigos en el campo de batalla
3. Se mostrarán en la lista con sus características

### 3️⃣ Combatir

1. **Selecciona un enemigo** de la lista
2. **Click en "DISPARAR"**
3. **Observa**:
   - La precisión determina si aciertas
   - La durabilidad disminuye (-5 por disparo)
   - Las características se recalculan automáticamente
   - Los enemigos pierden vida si aciertas
4. **Repite** hasta eliminar todos los enemigos

### 4️⃣ Gestión

- **Reparar**: Cuando la durabilidad sea baja, repara usando corchos
- **Mejorar**: Añade refuerzos o potencia durante la batalla
- **Monitorear**: Observa las barras de estado en tiempo real

### 5️⃣ Victorias y Progreso

- **Oleada completada**: Ganas puntos y subes de nivel
- **Nuevas oleadas**: Más enemigos y más difíciles
- **Game Over**: Si la catapulta se destruye (puedes repararla)

---

## 📊 Visualización de Conceptos POO

### 🔸 ESTADO (State) - Visualizado en tiempo real:

- **Barra de Durabilidad**: Muestra `_durabilidad` (0-100)
- **Cambio de Color**: La catapulta cambia de color según `_estado`
  - Marrón = LISTA
  - Naranja = DANADA
  - Gris = DESTRUIDA
- **Texto de Estado**: Muestra el estado actual (enum)
- **Contadores**: Disparos, desgaste, enemigos eliminados

### ⚙️ COMPORTAMIENTO (Behavior) - Acciones interactivas:

- **Botones de construcción**: Ejecutan `agregar_*()` methods
- **Botón Construir**: Ejecuta `construir()`
- **Botón Disparar**: Ejecuta `disparar(enemigo)`
- **Botón Reparar**: Ejecuta `reparar()`
- **Botón Mejorar**: Ejecuta `mejorar(tipo)`
- **Validaciones**: Los botones se deshabilitan según el estado

### 📊 CARACTERÍSTICAS (Properties) - Calculadas dinámicamente:

- **Barra de Potencia**: Muestra `@property potencia`
- **Barra de Precisión**: Muestra `@property precision`
- **Texto de Alcance**: Muestra `@property alcance`
- **Actualización automática**: Al disparar, las barras cambian inmediatamente

---

## 🎨 Detalles Visuales

### Colores del Estado:
```
🟫 Marrón (#8B4513)  → LISTA (Funcional)
🟧 Naranja (#E67E22) → DANADA (< 30% durabilidad)
⬜ Gris (#95A5A6)    → DESTRUIDA (0% durabilidad)
```

### Tipos de Enemigos:
```
🔵 Azul (#3498DB)    → Soldado
⬜ Gris (#95A5A6)    → Caballero
🟢 Verde (#2ECC71)   → Arquero
🟣 Morado (#9B59B6)  → Gigante
```

### Barras de Estado:
```
🟢 Verde (#27AE60)   → Durabilidad
🔵 Azul (#3498DB)    → Potencia
🟣 Morado (#9B59B6)  → Precisión
🔴 Rojo (#E74C3C)    → Vida de enemigos
```

---

## 🔧 Requisitos Técnicos

- **Python 3.6+**
- **tkinter** (incluido por defecto en Python)
- **No requiere instalación adicional**

### Verificar tkinter:
```bash
python -c "import tkinter; print('✓ Tkinter disponible')"
```

---

## 📱 Ventajas de la Versión Gráfica

✅ **Visualización en tiempo real** de los conceptos POO
✅ **Feedback visual inmediato** de todas las acciones
✅ **Más intuitivo** para entender cómo cambia el estado
✅ **Interactivo**: Click en vez de escribir comandos
✅ **Educativo**: Se ven las propiedades calculándose dinámicamente
✅ **Divertido**: Gráficos y animaciones básicas

---

## 🎯 Ejemplo de Flujo de Juego Gráfico

```
1. INICIO
   └─> Ventana se abre con panel de construcción

2. CONSTRUCCIÓN
   ├─> Seleccionar materiales (spinboxes + botones)
   ├─> Inventario se actualiza en tiempo real
   └─> Click "CONSTRUIR" → Catapulta aparece en campo

3. COMBATE
   ├─> Click "GENERAR OLEADA" → Enemigos aparecen
   ├─> Seleccionar enemigo de la lista
   ├─> Click "DISPARAR"
   │   ├─> Durabilidad disminuye (barra verde baja)
   │   ├─> Potencia recalculada (barra azul baja)
   │   ├─> Precisión afectada (barra morada baja)
   │   └─> Enemigo pierde vida (barra roja del enemigo)
   └─> Repetir hasta eliminar todos

4. GESTIÓN
   ├─> Si durabilidad < 30% → Color naranja
   ├─> Click "REPARAR" → Durabilidad sube
   └─> Click "MEJORAR" → Añadir componentes

5. VICTORIA
   └─> Mensaje de victoria + opción de continuar
```

---

## 🐛 Solución de Problemas

### La ventana no se abre:
```bash
# Verificar que estás en el entorno correcto
python --version

# Verificar tkinter
python -c "import tkinter"
```

### Error de importación:
```bash
# Asegúrate de estar en el directorio correcto
cd /workspaces/catapulta
python main_gui.py
```

### La ventana se ve cortada:
- Maximiza la ventana
- Tamaño recomendado: 1200x800 (se establece automáticamente)

---

## 📚 Archivos Relacionados

- **`main_gui.py`** - Punto de entrada de la versión gráfica
- **`catapulta/interfaz_grafica.py`** - Código de la interfaz (700+ líneas)
- **`main.py`** - Versión terminal original
- **`CONCEPTOS_POO.md`** - Documentación de conceptos
- **`README_POO.md`** - Resumen de mejoras POO

---

## 🎓 Aprendizaje

La interfaz gráfica es **perfecta para aprender POO** porque:

1. **Ves el ESTADO cambiar**: Las barras se mueven en tiempo real
2. **Ejecutas COMPORTAMIENTOS**: Los botones llaman a métodos
3. **Observas CARACTERÍSTICAS**: Las propiedades se recalculan visualmente

### Experimento Sugerido:

1. Construye una catapulta
2. Observa: Potencia = 125, Precisión = 75%
3. Dispara varias veces
4. Observa cómo **automáticamente**:
   - Durabilidad baja
   - Potencia disminuye (property recalculada)
   - Precisión baja (afectada por desgaste)
5. Repara
6. Observa cómo todo se restaura

**¡Esto ES POO en acción!** 🚀

---

## 🎉 Disfruta del Juego

¡Ahora puedes ver y tocar los conceptos de Programación Orientada a Objetos de forma visual e interactiva!

```
╔═══════════════════════════════════════════════════════════╗
║  🏰 ¡Defiende tu castillo con estilo gráfico! 🎮          ║
╚═══════════════════════════════════════════════════════════╝
```
