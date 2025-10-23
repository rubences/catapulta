"""
Interfaz Web para el juego de la Catapulta usando Flask
"""

from flask import Flask, render_template, jsonify, request, session
import secrets
import json
from .catapulta import Catapulta, EstadoCatapulta
from .enemigos import generar_oleada_enemigos


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Almacenamiento temporal de juegos (en memoria)
juegos = {}


def obtener_juego():
    """Obtiene o crea el juego de la sesión actual"""
    if 'game_id' not in session:
        session['game_id'] = secrets.token_hex(8)
    
    game_id = session['game_id']
    
    if game_id not in juegos:
        juegos[game_id] = {
            'catapulta': None,
            'enemigos': [],
            'nivel': 1,
            'puntos': 0
        }
    
    return juegos[game_id]


@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')


@app.route('/api/crear_catapulta', methods=['POST'])
def crear_catapulta():
    """Crea una nueva catapulta"""
    data = request.json
    nombre = data.get('nombre', 'Mi Catapulta')
    
    juego = obtener_juego()
    juego['catapulta'] = Catapulta(nombre)
    
    return jsonify({'success': True, 'mensaje': f"Catapulta '{nombre}' creada"})


@app.route('/api/agregar_material', methods=['POST'])
def agregar_material():
    """Agrega un material a la catapulta"""
    data = request.json
    tipo = data.get('tipo')
    valor = data.get('valor')
    
    juego = obtener_juego()
    catapulta = juego['catapulta']
    
    if not catapulta:
        return jsonify({'success': False, 'error': 'Catapulta no creada'})
    
    if catapulta.construida:
        return jsonify({'success': False, 'error': 'Catapulta ya construida'})
    
    try:
        if tipo == 'palo':
            catapulta.agregar_palo(int(valor))
        elif tipo == 'goma':
            catapulta.agregar_goma(int(valor))
        elif tipo == 'tapon':
            catapulta.agregar_tapon()
        elif tipo == 'corcho':
            for _ in range(int(valor)):
                catapulta.agregar_corcho()
        elif tipo == 'pegamento':
            catapulta.agregar_pegamento(int(valor))
        
        return jsonify({
            'success': True,
            'inventario': obtener_inventario(catapulta)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/construir', methods=['POST'])
def construir():
    """Construye la catapulta"""
    juego = obtener_juego()
    catapulta = juego['catapulta']
    
    if not catapulta:
        return jsonify({'success': False, 'error': 'Catapulta no creada'})
    
    if catapulta.construir():
        return jsonify({
            'success': True,
            'mensaje': f"¡Catapulta '{catapulta.nombre}' construida con éxito!",
            'estado': obtener_estado_catapulta(catapulta)
        })
    else:
        return jsonify({
            'success': False,
            'error': 'No se pudo construir. Verifica los materiales mínimos.'
        })


@app.route('/api/generar_oleada', methods=['POST'])
def generar_oleada():
    """Genera una nueva oleada de enemigos"""
    juego = obtener_juego()
    
    if not juego['catapulta'] or not juego['catapulta'].construida:
        return jsonify({'success': False, 'error': 'Construye la catapulta primero'})
    
    juego['enemigos'] = generar_oleada_enemigos(juego['nivel'])
    
    return jsonify({
        'success': True,
        'nivel': juego['nivel'],
        'enemigos': obtener_enemigos(juego['enemigos'])
    })


@app.route('/api/disparar', methods=['POST'])
def disparar():
    """Dispara a un enemigo"""
    data = request.json
    indice_enemigo = data.get('enemigo')
    
    juego = obtener_juego()
    catapulta = juego['catapulta']
    
    if not catapulta or not catapulta.construida:
        return jsonify({'success': False, 'error': 'Catapulta no lista'})
    
    enemigos_vivos = [e for e in juego['enemigos'] if e.vivo]
    
    if indice_enemigo >= len(enemigos_vivos):
        return jsonify({'success': False, 'error': 'Enemigo inválido'})
    
    enemigo = enemigos_vivos[indice_enemigo]
    acierto = catapulta.disparar(enemigo)
    
    eliminado = not enemigo.vivo
    if eliminado:
        juego['puntos'] += 50
    
    # Verificar victoria
    enemigos_vivos = [e for e in juego['enemigos'] if e.vivo]
    victoria = len(enemigos_vivos) == 0
    
    if victoria:
        juego['puntos'] += juego['nivel'] * 100
        juego['nivel'] += 1
    
    return jsonify({
        'success': True,
        'acierto': acierto,
        'eliminado': eliminado,
        'victoria': victoria,
        'estado': obtener_estado_catapulta(catapulta),
        'enemigos': obtener_enemigos(juego['enemigos']),
        'puntos': juego['puntos'],
        'nivel': juego['nivel'],
        'game_over': catapulta.estado == EstadoCatapulta.DESTRUIDA
    })


@app.route('/api/reparar', methods=['POST'])
def reparar():
    """Repara la catapulta"""
    juego = obtener_juego()
    catapulta = juego['catapulta']
    
    if not catapulta:
        return jsonify({'success': False, 'error': 'Catapulta no creada'})
    
    if catapulta.reparar():
        return jsonify({
            'success': True,
            'mensaje': 'Catapulta reparada',
            'estado': obtener_estado_catapulta(catapulta)
        })
    else:
        return jsonify({
            'success': False,
            'error': 'No se pudo reparar (¿sin recursos?)'
        })


@app.route('/api/mejorar', methods=['POST'])
def mejorar():
    """Mejora la catapulta"""
    data = request.json
    tipo = data.get('tipo')
    
    juego = obtener_juego()
    catapulta = juego['catapulta']
    
    if not catapulta:
        return jsonify({'success': False, 'error': 'Catapulta no creada'})
    
    if catapulta.mejorar(tipo):
        return jsonify({
            'success': True,
            'mensaje': f'Mejora {tipo} aplicada',
            'estado': obtener_estado_catapulta(catapulta)
        })
    else:
        return jsonify({
            'success': False,
            'error': 'No se pudo mejorar'
        })


@app.route('/api/estado', methods=['GET'])
def estado():
    """Obtiene el estado completo del juego"""
    juego = obtener_juego()
    catapulta = juego['catapulta']
    
    return jsonify({
        'catapulta': obtener_estado_catapulta(catapulta) if catapulta else None,
        'enemigos': obtener_enemigos(juego['enemigos']),
        'nivel': juego['nivel'],
        'puntos': juego['puntos']
    })


# === FUNCIONES AUXILIARES ===

def obtener_inventario(catapulta):
    """Retorna el inventario de la catapulta"""
    return {
        'palos': len(catapulta.palos),
        'gomas': len(catapulta.gomas),
        'tapones': len(catapulta.tapones),
        'corchos': len(catapulta.corchos),
        'pegamento': catapulta.pegamento is not None
    }


def obtener_estado_catapulta(catapulta):
    """Retorna el estado completo de la catapulta"""
    if not catapulta:
        return None
    
    return {
        'nombre': catapulta.nombre,
        'construida': catapulta.construida,
        'estado': catapulta.estado.value if catapulta.construida else 'No construida',
        'durabilidad': catapulta.durabilidad if catapulta.construida else 0,
        'durabilidad_max': catapulta._durabilidad_maxima if catapulta.construida else 0,
        'durabilidad_pct': catapulta.durabilidad_porcentaje if catapulta.construida else 0,
        'potencia': catapulta.potencia,
        'alcance': catapulta.alcance,
        'precision': catapulta.precision,
        'estabilidad': catapulta.estabilidad,
        'disparos': catapulta.disparos_realizados,
        'desgaste': catapulta.nivel_desgaste,
        'enemigos_eliminados': catapulta.enemigos_eliminados,
        'inventario': obtener_inventario(catapulta),
        'historial': catapulta.historial_disparos[-10:] if hasattr(catapulta, 'historial_disparos') else []
    }


def obtener_enemigos(enemigos):
    """Retorna la lista de enemigos"""
    return [{
        'nombre': e.nombre,
        'vida': e.vida,
        'vida_max': e.vida_maxima,
        'distancia': e.distancia,
        'armadura': e.armadura,
        'vivo': e.vivo
    } for e in enemigos]


def iniciar_servidor(host='0.0.0.0', port=5000, debug=True):
    """Inicia el servidor Flask"""
    app.run(host=host, port=port, debug=debug)
