"""
Servidor Web para la Catapulta
================================

Ejecuta el juego con interfaz web usando Flask.

Para jugar:
1. Ejecuta este archivo: python main_web.py
2. Abre tu navegador en: http://localhost:5000
3. ¡Disfruta del juego con interfaz gráfica!
"""

from catapulta.servidor_web import iniciar_servidor

if __name__ == "__main__":
    print("="*60)
    print("🏰 CATAPULTA - Versión Web 🏰".center(60))
    print("="*60)
    print("\n📱 Servidor iniciando...")
    print("\n🌐 Abre tu navegador en: http://localhost:5000")
    print("\n💡 Presiona Ctrl+C para detener el servidor\n")
    print("="*60)
    
    iniciar_servidor(host='0.0.0.0', port=5000, debug=False)
