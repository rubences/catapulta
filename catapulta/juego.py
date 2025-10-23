"""
Módulo del juego principal
"""

from .catapulta import Catapulta
from .enemigos import generar_oleada_enemigos


class Juego:
    """Controlador principal del juego"""
    
    def __init__(self):
        self.catapulta = None
        self.enemigos = []
        self.nivel = 1
        self.puntos = 0
    
    def crear_catapulta(self):
        """Permite al usuario crear su catapulta"""
        print("\n" + "="*60)
        print("🏗️  CONSTRUCTOR DE CATAPULTAS")
        print("="*60)
        
        nombre = input("\n¿Cómo quieres llamar a tu catapulta? (Enter para 'Mi Catapulta'): ").strip()
        if not nombre:
            nombre = "Mi Catapulta"
        
        self.catapulta = Catapulta(nombre)
        
        print("\n📋 MATERIALES DISPONIBLES:")
        print("1. Palos (estructura) - Aumentan potencia")
        print("2. Gomas (impulso) - Aumentan potencia y velocidad")
        print("3. Tapones (estabilidad) - Aumentan precisión")
        print("4. Corchos (munición) - Proyectiles para disparar")
        print("5. Pegamento (unión) - Necesario para construir")
        
        print("\n💡 RECOMENDACIONES:")
        print("   - Mínimo 2 palos, 1 goma, 1 pegamento y 1 corcho")
        print("   - Más tapones = mayor precisión y estabilidad")
        print("   - Mejor pegamento = mayor probabilidad de construcción exitosa")
        print("   - Más corchos = más disparos disponibles")
        
        while True:
            print("\n" + "-"*60)
            print("¿Qué material quieres agregar?")
            print("1. Palo")
            print("2. Goma")
            print("3. Tapón")
            print("4. Corcho")
            print("5. Pegamento")
            print("6. Ver inventario")
            print("7. Construir catapulta")
            print("0. Salir")
            
            opcion = input("\nOpción: ").strip()
            
            if opcion == "1":
                try:
                    longitud = int(input("Longitud del palo (10-50 cm): "))
                    if 10 <= longitud <= 50:
                        self.catapulta.agregar_palo(longitud)
                    else:
                        print("⚠ La longitud debe estar entre 10 y 50 cm")
                except ValueError:
                    print("⚠ Valor inválido")
            
            elif opcion == "2":
                try:
                    elasticidad = int(input("Elasticidad de la goma (1-10): "))
                    self.catapulta.agregar_goma(elasticidad)
                except ValueError:
                    print("⚠ Valor inválido")
            
            elif opcion == "3":
                self.catapulta.agregar_tapon()
            
            elif opcion == "4":
                cantidad = input("¿Cuántos corchos? (Enter para 1): ").strip()
                try:
                    cantidad = int(cantidad) if cantidad else 1
                    for _ in range(cantidad):
                        self.catapulta.agregar_corcho()
                except ValueError:
                    print("⚠ Valor inválido")
            
            elif opcion == "5":
                try:
                    calidad = int(input("Calidad del pegamento (1-10): "))
                    self.catapulta.agregar_pegamento(calidad)
                except ValueError:
                    print("⚠ Valor inválido")
            
            elif opcion == "6":
                self.catapulta.mostrar_inventario()
            
            elif opcion == "7":
                if self.catapulta.construir():
                    return True
                else:
                    continuar = input("\n¿Quieres seguir agregando materiales? (s/n): ").lower()
                    if continuar != 's':
                        return False
            
            elif opcion == "0":
                return False
    
    def generar_enemigos(self):
        """Genera una nueva oleada de enemigos"""
        self.enemigos = generar_oleada_enemigos(self.nivel)
        print(f"\n⚔️  ¡Oleada {self.nivel} de enemigos!")
        print(f"   {len(self.enemigos)} enemigos se aproximan:\n")
        for i, enemigo in enumerate(self.enemigos, 1):
            print(f"   {i}. {enemigo}")
    
    def seleccionar_objetivo(self):
        """Permite al jugador seleccionar un objetivo"""
        enemigos_vivos = [e for e in self.enemigos if e.vivo]
        
        if not enemigos_vivos:
            return None
        
        print("\n🎯 SELECCIONAR OBJETIVO:")
        for i, enemigo in enumerate(enemigos_vivos, 1):
            print(f"   {i}. {enemigo}")
        
        while True:
            try:
                opcion = input(f"\nElige objetivo (1-{len(enemigos_vivos)}): ").strip()
                indice = int(opcion) - 1
                if 0 <= indice < len(enemigos_vivos):
                    return enemigos_vivos[indice]
                else:
                    print("⚠ Opción inválida")
            except ValueError:
                print("⚠ Valor inválido")
    
    def fase_combate(self):
        """Fase de combate contra los enemigos"""
        print("\n" + "="*60)
        print("⚔️  FASE DE COMBATE")
        print("="*60)
        
        while True:
            enemigos_vivos = [e for e in self.enemigos if e.vivo]
            
            if not enemigos_vivos:
                print("\n🎉 ¡Has eliminado a todos los enemigos!")
                self.puntos += self.nivel * 100
                self.nivel += 1
                return True
            
            if len(self.catapulta.corchos) == 0:
                print("\n😢 Te has quedado sin munición...")
                print(f"   Enemigos restantes: {len(enemigos_vivos)}")
                return False
            
            # Verificar estado de la catapulta
            from .catapulta import EstadoCatapulta
            if self.catapulta.estado == EstadoCatapulta.DESTRUIDA:
                print("\n💔 ¡Tu catapulta ha sido destruida!")
                return False
            
            self.catapulta.mostrar_estadisticas()
            print(f"\n   Enemigos vivos: {len(enemigos_vivos)}/{len(self.enemigos)}")
            print(f"   Puntos: {self.puntos}")
            
            print("\n¿Qué quieres hacer?")
            print("1. Disparar")
            print("2. Ver enemigos")
            print("3. Reparar catapulta (cuesta 1 corcho)")
            print("4. Ver historial de disparos")
            print("5. Mejorar catapulta")
            print("6. Abandonar")
            
            opcion = input("\nOpción: ").strip()
            
            if opcion == "1":
                objetivo = self.seleccionar_objetivo()
                if objetivo:
                    self.catapulta.disparar(objetivo)
                    if not objetivo.vivo:
                        self.puntos += 50
            
            elif opcion == "2":
                print("\n📋 ESTADO DE LOS ENEMIGOS:")
                for i, enemigo in enumerate(self.enemigos, 1):
                    print(f"   {i}. {enemigo}")
            
            elif opcion == "3":
                self.catapulta.reparar()
            
            elif opcion == "4":
                self.catapulta.mostrar_historial()
            
            elif opcion == "5":
                print("\n⚡ MEJORAS DISPONIBLES:")
                print("1. Refuerzo estructural (agrega tapón)")
                print("2. Aumento de potencia (agrega goma)")
                mejora = input("Elige mejora (1-2): ").strip()
                
                if mejora == "1":
                    self.catapulta.mejorar("refuerzo")
                elif mejora == "2":
                    self.catapulta.mejorar("potencia")
            
            elif opcion == "6":
                return False
    
    def jugar(self):
        """Bucle principal del juego"""
        print("\n" + "="*60)
        print("🏰  CATAPULTA - DEFENSA DEL CASTILLO")
        print("="*60)
        print("\n¡Bienvenido! Construye tu catapulta y defiende el castillo.")
        
        if not self.crear_catapulta():
            print("\n👋 Gracias por jugar!")
            return
        
        while True:
            self.generar_enemigos()
            
            if not self.fase_combate():
                print("\n" + "="*60)
                print("💀 GAME OVER")
                print("="*60)
                print(f"   Nivel alcanzado: {self.nivel}")
                print(f"   Puntuación final: {self.puntos}")
                break
            
            if len(self.catapulta.corchos) == 0:
                print("\n⚠️  Sin munición para continuar...")
                break
            
            continuar = input("\n¿Continuar a la siguiente oleada? (s/n): ").lower()
            if continuar != 's':
                print("\n" + "="*60)
                print("🏆 ¡VICTORIA!")
                print("="*60)
                print(f"   Nivel alcanzado: {self.nivel}")
                print(f"   Puntuación final: {self.puntos}")
                break
        
        print("\n👋 ¡Gracias por jugar!")
