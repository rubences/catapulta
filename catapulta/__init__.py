"""
Paquete catapulta - Sistema de defensa con catapultas
"""

from .catapulta import Catapulta
from .materiales import Palo, Goma, Tapon, Corcho, Pegamento
from .enemigos import Enemigo, Soldado, Caballero, Arquero, Gigante, generar_oleada_enemigos
from .juego import Juego

__all__ = [
    'Catapulta',
    'Palo', 'Goma', 'Tapon', 'Corcho', 'Pegamento',
    'Enemigo', 'Soldado', 'Caballero', 'Arquero', 'Gigante',
    'generar_oleada_enemigos',
    'Juego'
]

__version__ = '1.0.0'
