"""
CATAPULTA - Versión con Interfaz Gráfica
=========================================

Juego de defensa del castillo con interfaz gráfica usando Tkinter.
Demuestra los conceptos de POO: Estado, Comportamiento y Características.

Para jugar:
- Construye tu catapulta seleccionando materiales
- Genera oleadas de enemigos
- Dispara seleccionando enemigos
- Observa cómo cambian las características en tiempo real
"""

from catapulta.interfaz_grafica import iniciar_juego_grafico


if __name__ == "__main__":
    print("🏰 Iniciando Catapulta - Versión Gráfica...")
    iniciar_juego_grafico()
