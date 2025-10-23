"""
CATAPULTA - Juego de Defensa del Castillo
==========================================

Un juego de Programación Orientada a Objetos donde construyes tu propia 
catapulta con diferentes materiales y la usas para defender tu castillo 
de oleadas de enemigos.

CONCEPTOS POO DEMOSTRADOS:
--------------------------
1. ESTADO (State):
   - La catapulta tiene estados: EN_CONSTRUCCION, LISTA, DANADA, DESTRUIDA
   - Atributos que cambian: durabilidad, desgaste, munición
   
2. COMPORTAMIENTO (Behavior):
   - Métodos: construir(), disparar(), reparar(), mejorar()
   - La catapulta responde a acciones y modifica su estado
   
3. CARACTERÍSTICAS (Properties):
   - Propiedades calculadas: potencia, alcance, precision, estabilidad
   - Se calculan dinámicamente basándose en el estado actual

Materiales disponibles:
- Palos: Estructura base (aumentan potencia)
- Gomas: Proporcionan impulso (aumentan potencia y velocidad)
- Tapones: Dan estabilidad (aumentan precisión)
- Corchos: Munición para disparar
- Pegamento: Une las piezas (necesario para construir)

Enemigos:
- Soldado: Enemigo básico
- Caballero: Más armadura
- Arquero: Rápido pero débil
- Gigante: Muy resistente (aparece en nivel 3+)
"""

from catapulta import Juego


def main():
    """Función principal del juego"""
    print("\n" + "="*70)
    print(" 🏰 BIENVENIDO AL JUEGO DE LA CATAPULTA - POO Edition 🏰")
    print("="*70)
    print("\nEste juego demuestra los principios de POO:")
    print("  • ESTADO: La catapulta cambia de estado según su uso")
    print("  • COMPORTAMIENTO: Métodos que realizan acciones")
    print("  • CARACTERÍSTICAS: Propiedades calculadas dinámicamente")
    print("\n" + "="*70 + "\n")
    
    juego = Juego()
    juego.jugar()


if __name__ == "__main__":
    main()
