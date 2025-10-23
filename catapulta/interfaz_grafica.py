"""
Interfaz gráfica para el juego de la Catapulta
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from catapulta.catapulta import Catapulta, EstadoCatapulta
from catapulta.enemigos import generar_oleada_enemigos


class VentanaJuego:
    """Ventana principal del juego con interfaz gráfica"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🏰 Catapulta - Defensa del Castillo")
        self.root.geometry("1200x800")
        self.root.configure(bg="#2C3E50")
        
        self.catapulta = None
        self.enemigos = []
        self.nivel = 1
        self.puntos = 0
        self.en_construccion = True
        
        self.crear_widgets()
        
    def crear_widgets(self):
        """Crea todos los widgets de la interfaz"""
        
        # Frame superior - Título
        frame_titulo = tk.Frame(self.root, bg="#34495E", height=80)
        frame_titulo.pack(fill="x", padx=10, pady=10)
        
        titulo = tk.Label(
            frame_titulo,
            text="🏰 CATAPULTA - DEFENSA DEL CASTILLO 🏰",
            font=("Arial", 24, "bold"),
            bg="#34495E",
            fg="#ECF0F1"
        )
        titulo.pack(pady=20)
        
        # Frame principal - dividido en 2 columnas
        frame_principal = tk.Frame(self.root, bg="#2C3E50")
        frame_principal.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Columna izquierda - Construcción y Estado
        self.frame_izquierda = tk.Frame(frame_principal, bg="#34495E", width=400)
        self.frame_izquierda.pack(side="left", fill="both", padx=5)
        
        # Columna derecha - Campo de batalla
        self.frame_derecha = tk.Frame(frame_principal, bg="#34495E")
        self.frame_derecha.pack(side="right", fill="both", expand=True, padx=5)
        
        self.crear_panel_construccion()
        self.crear_panel_estado()
        self.crear_campo_batalla()
        self.crear_panel_enemigos()
        
    def crear_panel_construccion(self):
        """Panel para construir la catapulta"""
        frame = tk.LabelFrame(
            self.frame_izquierda,
            text="🔨 Constructor de Catapulta",
            font=("Arial", 12, "bold"),
            bg="#34495E",
            fg="#ECF0F1",
            relief="ridge",
            bd=2
        )
        frame.pack(fill="x", pady=10, padx=10)
        
        # Nombre
        tk.Label(frame, text="Nombre:", bg="#34495E", fg="#ECF0F1").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame, width=25)
        self.entry_nombre.insert(0, "Mi Catapulta")
        self.entry_nombre.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        
        # Palos
        tk.Label(frame, text="Palos (longitud 10-50):", bg="#34495E", fg="#ECF0F1").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.spin_palo = tk.Spinbox(frame, from_=10, to=50, width=10)
        self.spin_palo.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(frame, text="➕ Agregar Palo", command=self.agregar_palo, bg="#3498DB", fg="white").grid(row=1, column=2, padx=5, pady=5)
        
        # Gomas
        tk.Label(frame, text="Gomas (elasticidad 1-10):", bg="#34495E", fg="#ECF0F1").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.spin_goma = tk.Spinbox(frame, from_=1, to=10, width=10)
        self.spin_goma.grid(row=2, column=1, padx=5, pady=5)
        tk.Button(frame, text="➕ Agregar Goma", command=self.agregar_goma, bg="#3498DB", fg="white").grid(row=2, column=2, padx=5, pady=5)
        
        # Tapones
        tk.Label(frame, text="Tapones:", bg="#34495E", fg="#ECF0F1").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Button(frame, text="➕ Agregar Tapón", command=self.agregar_tapon, bg="#3498DB", fg="white", width=20).grid(row=3, column=1, columnspan=2, padx=5, pady=5)
        
        # Corchos
        tk.Label(frame, text="Corchos (cantidad):", bg="#34495E", fg="#ECF0F1").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.spin_corcho = tk.Spinbox(frame, from_=1, to=20, width=10)
        self.spin_corcho.grid(row=4, column=1, padx=5, pady=5)
        tk.Button(frame, text="➕ Agregar Corchos", command=self.agregar_corchos, bg="#3498DB", fg="white").grid(row=4, column=2, padx=5, pady=5)
        
        # Pegamento
        tk.Label(frame, text="Pegamento (calidad 1-10):", bg="#34495E", fg="#ECF0F1").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.spin_pegamento = tk.Spinbox(frame, from_=1, to=10, width=10)
        self.spin_pegamento.grid(row=5, column=1, padx=5, pady=5)
        tk.Button(frame, text="➕ Agregar Pegamento", command=self.agregar_pegamento, bg="#3498DB", fg="white").grid(row=5, column=2, padx=5, pady=5)
        
        # Botón Construir
        self.btn_construir = tk.Button(
            frame,
            text="🔨 CONSTRUIR CATAPULTA",
            command=self.construir_catapulta,
            bg="#27AE60",
            fg="white",
            font=("Arial", 12, "bold"),
            height=2
        )
        self.btn_construir.grid(row=6, column=0, columnspan=3, pady=15, padx=5, sticky="ew")
        
        # Inventario
        self.text_inventario = tk.Text(frame, height=6, width=40, bg="#ECF0F1", font=("Courier", 9))
        self.text_inventario.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
        
        # Inicializar catapulta vacía
        self.catapulta = Catapulta("Mi Catapulta")
        self.actualizar_inventario()
        
    def crear_panel_estado(self):
        """Panel que muestra el estado de la catapulta"""
        frame = tk.LabelFrame(
            self.frame_izquierda,
            text="📊 Estado de la Catapulta",
            font=("Arial", 12, "bold"),
            bg="#34495E",
            fg="#ECF0F1",
            relief="ridge",
            bd=2
        )
        frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        # Canvas para las barras de estado
        self.canvas_estado = tk.Canvas(frame, bg="#2C3E50", height=300)
        self.canvas_estado.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Texto de estadísticas
        self.text_stats = tk.Text(frame, height=8, width=40, bg="#ECF0F1", font=("Courier", 9))
        self.text_stats.pack(padx=10, pady=10)
        
        # Botones de acción
        frame_botones = tk.Frame(frame, bg="#34495E")
        frame_botones.pack(fill="x", padx=10, pady=10)
        
        self.btn_reparar = tk.Button(
            frame_botones,
            text="🔧 Reparar",
            command=self.reparar_catapulta,
            bg="#E67E22",
            fg="white",
            state="disabled"
        )
        self.btn_reparar.pack(side="left", padx=5)
        
        self.btn_mejorar = tk.Button(
            frame_botones,
            text="⚡ Mejorar",
            command=self.mejorar_catapulta,
            bg="#9B59B6",
            fg="white",
            state="disabled"
        )
        self.btn_mejorar.pack(side="left", padx=5)
        
        self.actualizar_estado()
        
    def crear_campo_batalla(self):
        """Crea el campo de batalla visual"""
        frame = tk.LabelFrame(
            self.frame_derecha,
            text="⚔️ Campo de Batalla",
            font=("Arial", 12, "bold"),
            bg="#34495E",
            fg="#ECF0F1",
            relief="ridge",
            bd=2
        )
        frame.pack(fill="both", expand=True, pady=10, padx=10)
        
        # Info superior
        frame_info = tk.Frame(frame, bg="#34495E")
        frame_info.pack(fill="x", padx=10, pady=5)
        
        self.label_nivel = tk.Label(
            frame_info,
            text="Nivel: 1",
            font=("Arial", 14, "bold"),
            bg="#34495E",
            fg="#F39C12"
        )
        self.label_nivel.pack(side="left", padx=10)
        
        self.label_puntos = tk.Label(
            frame_info,
            text="Puntos: 0",
            font=("Arial", 14, "bold"),
            bg="#34495E",
            fg="#2ECC71"
        )
        self.label_puntos.pack(side="right", padx=10)
        
        # Canvas para dibujar
        self.canvas_batalla = tk.Canvas(frame, bg="#95A5A6", height=400)
        self.canvas_batalla.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Botón disparar
        self.btn_disparar = tk.Button(
            frame,
            text="🎯 DISPARAR",
            command=self.disparar,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 14, "bold"),
            height=2,
            state="disabled"
        )
        self.btn_disparar.pack(pady=10, fill="x", padx=10)
        
        self.dibujar_campo_batalla()
        
    def crear_panel_enemigos(self):
        """Panel de lista de enemigos"""
        frame = tk.LabelFrame(
            self.frame_derecha,
            text="👾 Enemigos",
            font=("Arial", 12, "bold"),
            bg="#34495E",
            fg="#ECF0F1",
            relief="ridge",
            bd=2
        )
        frame.pack(fill="x", pady=10, padx=10)
        
        # Listbox de enemigos
        self.listbox_enemigos = tk.Listbox(
            frame,
            height=6,
            bg="#ECF0F1",
            font=("Courier", 10),
            selectmode="single"
        )
        self.listbox_enemigos.pack(fill="x", padx=10, pady=10)
        
        # Botón generar oleada
        self.btn_oleada = tk.Button(
            frame,
            text="⚔️ GENERAR OLEADA DE ENEMIGOS",
            command=self.generar_oleada,
            bg="#C0392B",
            fg="white",
            font=("Arial", 12, "bold"),
            state="disabled"
        )
        self.btn_oleada.pack(pady=10, fill="x", padx=10)
        
    # === MÉTODOS DE CONSTRUCCIÓN ===
    
    def agregar_palo(self):
        if self.catapulta and not self.catapulta.construida:
            longitud = int(self.spin_palo.get())
            self.catapulta.agregar_palo(longitud)
            self.actualizar_inventario()
            self.log(f"✓ Palo de {longitud}cm agregado")
    
    def agregar_goma(self):
        if self.catapulta and not self.catapulta.construida:
            elasticidad = int(self.spin_goma.get())
            self.catapulta.agregar_goma(elasticidad)
            self.actualizar_inventario()
            self.log(f"✓ Goma elasticidad {elasticidad} agregada")
    
    def agregar_tapon(self):
        if self.catapulta and not self.catapulta.construida:
            self.catapulta.agregar_tapon()
            self.actualizar_inventario()
            self.log("✓ Tapón agregado")
    
    def agregar_corchos(self):
        if self.catapulta:
            cantidad = int(self.spin_corcho.get())
            for _ in range(cantidad):
                self.catapulta.agregar_corcho()
            self.actualizar_inventario()
            self.log(f"✓ {cantidad} corchos agregados")
    
    def agregar_pegamento(self):
        if self.catapulta and not self.catapulta.construida:
            calidad = int(self.spin_pegamento.get())
            self.catapulta.agregar_pegamento(calidad)
            self.actualizar_inventario()
            self.log(f"✓ Pegamento calidad {calidad} agregado")
    
    def construir_catapulta(self):
        if not self.catapulta:
            return
        
        nombre = self.entry_nombre.get()
        self.catapulta.nombre = nombre
        
        if self.catapulta.construir():
            self.log(f"✅ ¡Catapulta '{nombre}' construida con éxito!")
            self.en_construccion = False
            self.btn_construir.config(state="disabled")
            self.btn_oleada.config(state="normal")
            self.btn_reparar.config(state="normal")
            self.btn_mejorar.config(state="normal")
            self.actualizar_estado()
            self.dibujar_campo_batalla()
            messagebox.showinfo("¡Éxito!", f"Catapulta '{nombre}' construida correctamente.\n\n¡Ahora genera una oleada de enemigos!")
        else:
            self.log("❌ Construcción fallida. Revisa los materiales.")
            messagebox.showerror("Error", "No se pudo construir la catapulta.\nVerifica que tienes los materiales mínimos.")
    
    # === MÉTODOS DE COMBATE ===
    
    def generar_oleada(self):
        self.enemigos = generar_oleada_enemigos(self.nivel)
        self.actualizar_lista_enemigos()
        self.dibujar_campo_batalla()
        self.btn_disparar.config(state="normal")
        self.btn_oleada.config(state="disabled")
        self.log(f"⚔️ Oleada {self.nivel}: {len(self.enemigos)} enemigos generados")
    
    def disparar(self):
        if not self.catapulta or not self.catapulta.construida:
            return
        
        if not self.enemigos:
            messagebox.showwarning("Sin enemigos", "No hay enemigos. Genera una nueva oleada.")
            return
        
        # Obtener enemigo seleccionado
        seleccion = self.listbox_enemigos.curselection()
        if not seleccion:
            messagebox.showwarning("Selección", "Selecciona un enemigo para disparar")
            return
        
        enemigos_vivos = [e for e in self.enemigos if e.vivo]
        if not enemigos_vivos:
            messagebox.showinfo("Victoria", "¡Todos los enemigos eliminados!")
            self.victoria_oleada()
            return
        
        indice = seleccion[0]
        if indice >= len(enemigos_vivos):
            return
        
        enemigo = enemigos_vivos[indice]
        
        # Disparar
        acierto = self.catapulta.disparar(enemigo)
        
        if acierto and
            self.puntos += 50
            self.label_puntos.config(text=f"Puntos: {self.puntos}")
        
        self.actualizar_lista_enemigos()
        self.actualizar_estado()
        self.dibujar_campo_batalla()
        
        # Verificar si quedan enemigos vivos
        enemigos_vivos = [e for e in self.enemigos if e.vivo]
        if not enemigos_vivos:
            self.victoria_oleada()
        
        # Verificar estado de la catapulta
        if self.catapulta.estado == EstadoCatapulta.DESTRUIDA:
            self.game_over()
    
    def victoria_oleada(self):
        self.puntos += self.nivel * 100
        self.nivel += 1
        self.label_nivel.config(text=f"Nivel: {self.nivel}")
        self.label_puntos.config(text=f"Puntos: {self.puntos}")
        
        resultado = messagebox.askyesno(
            "¡Victoria!",
            f"¡Oleada {self.nivel - 1} completada!\n\nPuntos: {self.puntos}\n\n¿Continuar al nivel {self.nivel}?"
        )
        
        if resultado:
            self.btn_oleada.config(state="normal")
            self.btn_disparar.config(state="disabled")
            self.log(f"🎉 ¡Oleada {self.nivel - 1} completada!")
        else:
            messagebox.showinfo("Fin del Juego", f"¡Juego terminado!\n\nNivel alcanzado: {self.nivel}\nPuntuación final: {self.puntos}")
            self.root.quit()
    
    def game_over(self):
        self.btn_disparar.config(state="disabled")
        messagebox.showinfo(
            "Game Over",
            f"💀 La catapulta ha sido destruida\n\nNivel alcanzado: {self.nivel}\nPuntuación final: {self.puntos}\n\nPuedes repararla para continuar."
        )
    
    def reparar_catapulta(self):
        if self.catapulta:
            if self.catapulta.reparar():
                self.actualizar_estado()
                self.dibujar_campo_batalla()
                self.log("🔧 Catapulta reparada")
                if self.catapulta.estado != EstadoCatapulta.DESTRUIDA:
                    self.btn_disparar.config(state="normal")
    
    def mejorar_catapulta(self):
        opciones = ["refuerzo", "potencia"]
        ventana = tk.Toplevel(self.root)
        ventana.title("Mejorar Catapulta")
        ventana.geometry("300x150")
        ventana.configure(bg="#34495E")
        
        tk.Label(ventana, text="Selecciona mejora:", bg="#34495E", fg="white", font=("Arial", 12)).pack(pady=10)
        
        def aplicar_refuerzo():
            self.catapulta.mejorar("refuerzo")
            self.actualizar_estado()
            self.log("⚡ Refuerzo aplicado")
            ventana.destroy()
        
        def aplicar_potencia():
            self.catapulta.mejorar("potencia")
            self.actualizar_estado()
            self.log("⚡ Potencia mejorada")
            ventana.destroy()
        
        tk.Button(ventana, text="🛡️ Refuerzo Estructural", command=aplicar_refuerzo, bg="#3498DB", fg="white", width=20).pack(pady=5)
        tk.Button(ventana, text="💪 Aumento de Potencia", command=aplicar_potencia, bg="#E67E22", fg="white", width=20).pack(pady=5)
    
    # === MÉTODOS DE ACTUALIZACIÓN VISUAL ===
    
    def actualizar_inventario(self):
        if not self.catapulta:
            return
        
        self.text_inventario.delete(1.0, tk.END)
        texto = f"INVENTARIO:\n"
        texto += f"Palos: {len(self.catapulta.palos)}\n"
        texto += f"Gomas: {len(self.catapulta.gomas)}\n"
        texto += f"Tapones: {len(self.catapulta.tapones)}\n"
        texto += f"Corchos: {len(self.catapulta.corchos)}\n"
        texto += f"Pegamento: {'Sí' if self.catapulta.pegamento else 'No'}\n"
        self.text_inventario.insert(1.0, texto)
    
    def actualizar_estado(self):
        if not self.catapulta or not self.catapulta.construida:
            return
        
        # Actualizar canvas de barras
        self.canvas_estado.delete("all")
        
        # Barra de durabilidad
        self.dibujar_barra(10, 20, self.catapulta.durabilidad_porcentaje, "Durabilidad", "#27AE60")
        
        # Barra de potencia (relativa)
        potencia_max = 600
        potencia_pct = min(100, (self.catapulta.potencia / potencia_max) * 100)
        self.dibujar_barra(10, 80, potencia_pct, "Potencia", "#3498DB")
        
        # Barra de precisión
        self.dibujar_barra(10, 140, self.catapulta.precision, "Precisión", "#9B59B6")
        
        # Alcance
        self.canvas_estado.create_text(
            10, 200,
            text=f"🎯 Alcance: {self.catapulta.alcance}m",
            anchor="w",
            font=("Arial", 12, "bold"),
            fill="#ECF0F1"
        )
        
        # Munición
        self.canvas_estado.create_text(
            10, 230,
            text=f"🔫 Munición: {len(self.catapulta.corchos)} corchos",
            anchor="w",
            font=("Arial", 12, "bold"),
            fill="#ECF0F1"
        )
        
        # Actualizar texto de estadísticas
        self.text_stats.delete(1.0, tk.END)
        texto = f"ESTADO: {self.catapulta.estado.value}\n"
        texto += f"Disparos: {self.catapulta.disparos_realizados}\n"
        texto += f"Desgaste: {self.catapulta.nivel_desgaste}\n"
        texto += f"Enemigos eliminados: {self.catapulta.enemigos_eliminados}\n"
        texto += f"\nCARACTERÍSTICAS:\n"
        texto += f"Potencia: {self.catapulta.potencia}\n"
        texto += f"Estabilidad: {self.catapulta.estabilidad:.1f}\n"
        self.text_stats.insert(1.0, texto)
    
    def dibujar_barra(self, x, y, porcentaje, nombre, color):
        """Dibuja una barra de progreso"""
        ancho = 350
        alto = 30
        
        # Fondo
        self.canvas_estado.create_rectangle(
            x, y, x + ancho, y + alto,
            fill="#7F8C8D",
            outline="#ECF0F1"
        )
        
        # Barra de progreso
        ancho_barra = int((ancho * porcentaje) / 100)
        self.canvas_estado.create_rectangle(
            x, y, x + ancho_barra, y + alto,
            fill=color,
            outline=""
        )
        
        # Texto
        self.canvas_estado.create_text(
            x + ancho / 2, y + alto / 2,
            text=f"{nombre}: {porcentaje:.0f}%",
            font=("Arial", 10, "bold"),
            fill="white"
        )
    
    def actualizar_lista_enemigos(self):
        self.listbox_enemigos.delete(0, tk.END)
        enemigos_vivos = [e for e in self.enemigos if e.vivo]
        
        for enemigo in enemigos_vivos:
            estado = "💀" if not enemigo.vivo else "❤️"
            texto = f"{estado} {enemigo.nombre} - HP:{enemigo.vida}/{enemigo.vida_maxima} - {enemigo.distancia}m"
            self.listbox_enemigos.insert(tk.END, texto)
    
    def dibujar_campo_batalla(self):
        """Dibuja la catapulta y los enemigos en el campo de batalla"""
        self.canvas_batalla.delete("all")
        
        ancho = self.canvas_batalla.winfo_width()
        if ancho <= 1:
            ancho = 700
        alto = self.canvas_batalla.winfo_height()
        if alto <= 1:
            alto = 400
        
        # Dibujar suelo
        self.canvas_batalla.create_rectangle(0, alto - 50, ancho, alto, fill="#7F8C8D", outline="")
        
        # Dibujar catapulta (izquierda)
        if self.catapulta and self.catapulta.construida:
            x_catapulta = 80
            y_catapulta = alto - 100
            
            # Color según estado
            if self.catapulta.estado == EstadoCatapulta.DESTRUIDA:
                color = "#95A5A6"
            elif self.catapulta.estado == EstadoCatapulta.DANADA:
                color = "#E67E22"
            else:
                color = "#8B4513"
            
            # Base
            self.canvas_batalla.create_rectangle(
                x_catapulta - 30, y_catapulta + 30,
                x_catapulta + 30, y_catapulta + 50,
                fill=color, outline="black", width=2
            )
            
            # Brazo
            self.canvas_batalla.create_line(
                x_catapulta, y_catapulta + 30,
                x_catapulta + 40, y_catapulta - 30,
                fill=color, width=8
            )
            
            # Cesta
            self.canvas_batalla.create_oval(
                x_catapulta + 30, y_catapulta - 40,
                x_catapulta + 50, y_catapulta - 20,
                fill="#C0392B", outline="black"
            )
            
            # Nombre
            self.canvas_batalla.create_text(
                x_catapulta, y_catapulta + 70,
                text=self.catapulta.nombre,
                font=("Arial", 10, "bold"),
                fill="white"
            )
        
        # Dibujar enemigos
        if self.enemigos:
            for i, enemigo in enumerate(self.enemigos):
                if not enemigo.vivo:
                    continue
                
                # Posición basada en distancia
                x_enemigo = 150 + (enemigo.distancia * 7)
                y_enemigo = alto - 100
                
                # Color según tipo
                if "Soldado" in enemigo.nombre:
                    color = "#3498DB"
                elif "Caballero" in enemigo.nombre:
                    color = "#95A5A6"
                elif "Arquero" in enemigo.nombre:
                    color = "#2ECC71"
                elif "Gigante" in enemigo.nombre:
                    color = "#9B59B6"
                else:
                    color = "#E74C3C"
                
                # Cuerpo
                tamaño = 20 if "Gigante" not in enemigo.nombre else 30
                self.canvas_batalla.create_oval(
                    x_enemigo - tamaño/2, y_enemigo - tamaño,
                    x_enemigo + tamaño/2, y_enemigo + tamaño,
                    fill=color, outline="black", width=2
                )
                
                # Barra de vida
                barra_ancho = 40
                barra_alto = 5
                vida_pct = enemigo.vida / enemigo.vida_maxima
                
                self.canvas_batalla.create_rectangle(
                    x_enemigo - barra_ancho/2, y_enemigo - tamaño - 15,
                    x_enemigo + barra_ancho/2, y_enemigo - tamaño - 10,
                    fill="#7F8C8D", outline="black"
                )
                
                self.canvas_batalla.create_rectangle(
                    x_enemigo - barra_ancho/2, y_enemigo - tamaño - 15,
                    x_enemigo - barra_ancho/2 + (barra_ancho * vida_pct), y_enemigo - tamaño - 10,
                    fill="#E74C3C", outline=""
                )
                
                # Distancia
                self.canvas_batalla.create_text(
                    x_enemigo, y_enemigo + tamaño + 10,
                    text=f"{enemigo.distancia}m",
                    font=("Arial", 8),
                    fill="white"
                )
    
    def log(self, mensaje):
        """Muestra un mensaje en la consola (para debug)"""
        print(mensaje)
    
    def iniciar(self):
        """Inicia el loop principal de la interfaz"""
        self.root.mainloop()


def iniciar_juego_grafico():
    """Función para iniciar el juego con interfaz gráfica"""
    juego = VentanaJuego()
    juego.iniciar()
