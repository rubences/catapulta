"""
Paquete catapulta - Sistema de defensa con catapultas
"""

from catapulta.catapulta import Catapulta, EstadoCatapulta
from catapulta.materiales import Palo, Goma, Tapon, Corcho, Pegamento
from catapulta.enemigos import Enemigo, Soldado, Caballero, Arquero, Gigante, generar_oleada_enemigos
from catapulta.juego import Juego

__all__ = [
    'Catapulta',
    'EstadoCatapulta',
    'Palo', 'Goma', 'Tapon', 'Corcho', 'Pegamento',
    'Enemigo', 'Soldado', 'Caballero', 'Arquero', 'Gigante',
    'generar_oleada_enemigos',
    'Juego'
]

__version__ = '2.0.0'  # Versión con interfaz gráfica
