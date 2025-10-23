"""
CATAPULTA - Juego de Defensa del Castillo
==========================================

Un juego donde construyes tu propia catapulta con diferentes materiales
y la usas para defender tu castillo de oleadas de enemigos.

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
    juego = Juego()
    juego.jugar()


if __name__ == "__main__":
    main()
