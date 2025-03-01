#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Información sobre los Kichwas de Ecuador
==================================================
Este programa recopila y presenta información completa sobre 
el pueblo indígena Kichwa (también conocido como Quichua) de Ecuador.

Desarrollado como parte de un proyecto de aplicación de la psicología
en problemas de ingeniería específicamente en Tecnología, con enfoque
en diseño culturalmente sensible.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
import os
import webbrowser
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk

class KichwaInfoSystem:
    """
    Sistema de información sobre la cultura Kichwa de Ecuador
    con interfaz gráfica culturalmente sensible.
    """
    
    def __init__(self, root):
        """Inicializa la aplicación con la ventana principal."""
        self.root = root
        self.root.title("Sistema de Información - Kichwas de Ecuador")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Datos sobre los Kichwas de Ecuador
        self.kichwa_data = self.load_kichwa_data()
        
        # Configuración de estilo culturalmente sensible
        self.configure_styles()
        
        # Crear la interfaz principal
        self.create_widgets()
    
    def configure_styles(self):
        """Configura los estilos de la aplicación basados en la estética Kichwa."""
        self.style = ttk.Style()
        
        # Colores inspirados en textiles Kichwas
        self.colors = {
            'primary': '#8B2323',     # Rojo oscuro (bayeta)
            'secondary': '#CD853F',   # Marrón claro (lana natural)
            'accent': '#FFD700',      # Dorado (bordados ceremoniales)
            'background': '#F5F5DC',  # Beige claro (color natural de fibras)
            'text': '#8B2323',        # Gris oscuro para texto
            'highlight': '#228B22'    # Verde para resaltar (simboliza la Pachamama)
        }
        
        # Configurar estilos personalizados
        self.style.configure('TFrame', background=self.colors['#8B2323'])
        self.style.configure('TNotebook', background=self.colors['#8B2323'])
        self.style.configure('TNotebook.Tab', background=self.colors['secondary'],
                            foreground=self.colors['red'], padding=[10, 5])
        self.style.map('TNotebook.Tab', background=[('selected', self.colors['primary'])],
                    foreground=[('selected', 'red')])
        self.style.configure('TLabel', background=self.colors['#8B2323'],
                           foreground=self.colors['text'], font=('Helvetica', 11))
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'),
                           foreground=self.colors['primary'])
        self.style.configure('Subtitle.TLabel', font=('Helvetica', 14, 'bold'),
                           foreground=self.colors['secondary'])
        self.style.configure('TButton', background=self.colors['#8B2323'],
                           foreground='red', font=('Helvetica', 11))
        
        # Configurar el aspecto general de la ventana
        self.root.configure(bg=self.colors['#8B2323'])
    
    def create_widgets(self):
        """Crea y organiza los widgets de la interfaz."""
        # Marco principal
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = ttk.Label(main_frame, text="Pueblo Kichwa del Ecuador",
                              style='Title.TLabel')
        title_label.pack(pady=(10, 20))
        
        # Crear un notebook (pestañas)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Crear pestañas
        self.create_overview_tab()
        self.create_regions_tab()
        self.create_language_tab()
        self.create_traditions_tab()
        self.create_worldview_tab()
        self.create_demographics_tab()
        self.create_cultural_design_tab()
        
        # Barra de estado
        status_frame = ttk.Frame(main_frame, style='TFrame')
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, 
                                    text=f"Desarrollado para diseño culturalmente sensible | Fecha: {datetime.now().strftime('%d-%m-%Y')}")
        self.status_label.pack(side=tk.LEFT)
        
        about_button = ttk.Button(status_frame, text="Acerca de", 
                                command=self.show_about)
        about_button.pack(side=tk.RIGHT, padx=5)
    
    def create_overview_tab(self):
        """Crea la pestaña de información general sobre los Kichwas."""
        overview_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(overview_frame, text="Información General")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(overview_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(overview_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido
        overview_data = self.kichwa_data['informacion_general']
        
        subtitle = ttk.Label(scrollable_frame, text="¿Quiénes son los Kichwas?", 
                           style='Subtitle.TLabel')
        subtitle.pack(anchor="w", pady=(10, 5), padx=10)
        
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=6, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, overview_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Historia
        history_label = ttk.Label(scrollable_frame, text="Historia", 
                                style='Subtitle.TLabel')
        history_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        history_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                               height=8, font=('Helvetica', 11))
        history_text.insert(tk.INSERT, overview_data['historia'])
        history_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        history_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Geografía y distribución
        geography_label = ttk.Label(scrollable_frame, text="Distribución Geográfica", 
                                  style='Subtitle.TLabel')
        geography_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        geography_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                                 height=6, font=('Helvetica', 11))
        geography_text.insert(tk.INSERT, overview_data['distribucion_geografica'])
        geography_text.config(state='disabled', background=self.colors['background'],
                            foreground=self.colors['text'])
        geography_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Características culturales destacadas
        cultural_label = ttk.Label(scrollable_frame, text="Características Culturales Destacadas", 
                                 style='Subtitle.TLabel')
        cultural_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for idx, caracteristica in enumerate(overview_data['caracteristicas_culturales']):
            caract_frame = ttk.Frame(scrollable_frame, style='TFrame')
            caract_frame.pack(fill=tk.X, padx=20, pady=2)
            
            bullet = ttk.Label(caract_frame, text=f"•", 
                             foreground=self.colors['primary'])
            bullet.pack(side=tk.LEFT, padx=(0, 5))
            
            caract_text = ttk.Label(caract_frame, text=caracteristica, 
                                  wraplength=700)
            caract_text.pack(side=tk.LEFT, anchor="w")
    
    def create_regions_tab(self):
        """Crea la pestaña de regiones donde habitan los Kichwas."""
        regions_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(regions_frame, text="Regiones")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(regions_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(regions_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Título
        regions_title = ttk.Label(scrollable_frame, 
                                text="Pueblos Kichwas por Regiones Geográficas", 
                                style='Subtitle.TLabel')
        regions_title.pack(anchor="w", pady=(10, 15), padx=10)
        
        # Introducción
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, self.kichwa_data['regiones']['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Regiones específicas
        for region, info in self.kichwa_data['regiones']['pueblos'].items():
            region_frame = ttk.Frame(scrollable_frame, style='TFrame')
            region_frame.pack(fill=tk.X, expand=True, padx=10, pady=10)
            
            region_title = ttk.Label(region_frame, text=region, 
                                   font=('Helvetica', 13, 'bold'),
                                   foreground=self.colors['primary'])
            region_title.pack(anchor="w", pady=(5, 10))
            
            # Descripción
            desc_text = scrolledtext.ScrolledText(region_frame, wrap=tk.WORD, 
                                                height=4, font=('Helvetica', 11))
            desc_text.insert(tk.INSERT, info['descripcion'])
            desc_text.config(state='disabled', background=self.colors['background'],
                           foreground=self.colors['text'])
            desc_text.pack(fill=tk.X, expand=False, padx=5, pady=5)
            
            # Pueblos/Comunidades
            communities_label = ttk.Label(region_frame, text="Comunidades principales:", 
                                        font=('Helvetica', 11, 'italic'))
            communities_label.pack(anchor="w", padx=5, pady=(10, 5))
            
            communities_frame = ttk.Frame(region_frame, style='TFrame')
            communities_frame.pack(fill=tk.X, padx=15)
            
            # Crear una cuadrícula de comunidades
            row = 0
            col = 0
            for community in info['comunidades']:
                comm_label = ttk.Label(communities_frame, text=f"• {community}")
                comm_label.grid(row=row, column=col, sticky="w", padx=5, pady=2)
                col += 1
                if col > 1:  # 2 columnas
                    col = 0
                    row += 1
    
    def create_language_tab(self):
        """Crea la pestaña de información lingüística sobre el Kichwa."""
        language_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(language_frame, text="Idioma")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(language_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(language_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Título y descripción general
        language_title = ttk.Label(scrollable_frame, text="Kichwa Ecuatoriano (Runa Shimi)", 
                                 style='Subtitle.TLabel')
        language_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        lang_data = self.kichwa_data['idioma']
        
        general_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                               height=5, font=('Helvetica', 11))
        general_text.insert(tk.INSERT, lang_data['descripcion_general'])
        general_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        general_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Características lingüísticas
        features_label = ttk.Label(scrollable_frame, text="Características Lingüísticas", 
                                 style='Subtitle.TLabel')
        features_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for feature, desc in lang_data['caracteristicas'].items():
            feature_frame = ttk.Frame(scrollable_frame, style='TFrame')
            feature_frame.pack(fill=tk.X, padx=20, pady=5)
            
            feature_title = ttk.Label(feature_frame, text=feature, 
                                    font=('Helvetica', 11, 'bold'),
                                    foreground=self.colors['secondary'])
            feature_title.pack(anchor="w", pady=(5, 2))
            
            feature_desc = ttk.Label(feature_frame, text=desc, 
                                   wraplength=750)
            feature_desc.pack(anchor="w", padx=10)
        
        # Diferencias dialectales
        dialects_label = ttk.Label(scrollable_frame, text="Variaciones Dialectales", 
                                 style='Subtitle.TLabel')
        dialects_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        dialects_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                                height=5, font=('Helvetica', 11))
        dialects_text.insert(tk.INSERT, lang_data['variaciones_dialectales'])
        dialects_text.config(state='disabled', background=self.colors['background'],
                           foreground=self.colors['text'])
        dialects_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Vocabulario básico
        vocab_label = ttk.Label(scrollable_frame, text="Vocabulario Básico", 
                              style='Subtitle.TLabel')
        vocab_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        # Crear tabla de vocabulario
        vocab_frame = ttk.Frame(scrollable_frame, style='TFrame')
        vocab_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Encabezados
        header_spanish = ttk.Label(vocab_frame, text="Español", 
                                 font=('Helvetica', 11, 'bold'))
        header_spanish.grid(row=0, column=0, padx=5, pady=5)
        
        header_kichwa = ttk.Label(vocab_frame, text="Kichwa", 
                                font=('Helvetica', 11, 'bold'))
        header_kichwa.grid(row=0, column=1, padx=5, pady=5)
        
        header_pronunciation = ttk.Label(vocab_frame, text="Pronunciación", 
                                       font=('Helvetica', 11, 'bold'))
        header_pronunciation.grid(row=0, column=2, padx=5, pady=5)
        
        # Palabras
        for i, (spanish, kichwa, pron) in enumerate(lang_data['vocabulario_basico']):
            spanish_label = ttk.Label(vocab_frame, text=spanish)
            spanish_label.grid(row=i+1, column=0, padx=5, pady=3, sticky="w")
            
            kichwa_label = ttk.Label(vocab_frame, text=kichwa, 
                                   foreground=self.colors['primary'])
            kichwa_label.grid(row=i+1, column=1, padx=5, pady=3, sticky="w")
            
            pron_label = ttk.Label(vocab_frame, text=pron, font=('Helvetica', 11, 'italic'))
            pron_label.grid(row=i+1, column=2, padx=5, pady=3, sticky="w")
        
        # Estado actual del idioma
        status_label = ttk.Label(scrollable_frame, text="Estado Actual e Iniciativas", 
                               style='Subtitle.TLabel')
        status_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        status_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                              height=5, font=('Helvetica', 11))
        status_text.insert(tk.INSERT, lang_data['estado_actual'])
        status_text.config(state='disabled', background=self.colors['background'],
                         foreground=self.colors['text'])
        status_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
    
    def create_traditions_tab(self):
        """Crea la pestaña de tradiciones y costumbres Kichwas."""
        traditions_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(traditions_frame, text="Tradiciones")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(traditions_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(traditions_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Tradiciones y costumbres
        trad_data = self.kichwa_data['tradiciones']
        
        # Introducción
        trad_title = ttk.Label(scrollable_frame, text="Tradiciones y Costumbres Kichwas", 
                             style='Subtitle.TLabel')
        trad_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, trad_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Festividades
        festivals_label = ttk.Label(scrollable_frame, text="Festividades Principales", 
                                  style='Subtitle.TLabel')
        festivals_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for festival, desc in trad_data['festividades'].items():
            festival_frame = ttk.Frame(scrollable_frame, style='TFrame')
            festival_frame.pack(fill=tk.X, padx=20, pady=5)
            
            festival_title = ttk.Label(festival_frame, text=festival, 
                                     font=('Helvetica', 11, 'bold'),
                                     foreground=self.colors['primary'])
            festival_title.pack(anchor="w", pady=(5, 2))
            
            festival_desc = ttk.Label(festival_frame, text=desc, 
                                    wraplength=750)
            festival_desc.pack(anchor="w", padx=10)
        
        # Vestimenta tradicional
        clothing_label = ttk.Label(scrollable_frame, text="Vestimenta Tradicional", 
                                 style='Subtitle.TLabel')
        clothing_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        clothing_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                                height=6, font=('Helvetica', 11))
        clothing_text.insert(tk.INSERT, trad_data['vestimenta'])
        clothing_text.config(state='disabled', background=self.colors['background'],
                           foreground=self.colors['text'])
        clothing_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Artesanías
        crafts_label = ttk.Label(scrollable_frame, text="Artesanías", 
                               style='Subtitle.TLabel')
        crafts_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for craft, desc in trad_data['artesanias'].items():
            craft_frame = ttk.Frame(scrollable_frame, style='TFrame')
            craft_frame.pack(fill=tk.X, padx=20, pady=5)
            
            craft_title = ttk.Label(craft_frame, text=craft, 
                                  font=('Helvetica', 11, 'bold'),
                                  foreground=self.colors['secondary'])
            craft_title.pack(anchor="w", pady=(5, 2))
            
            craft_desc = ttk.Label(craft_frame, text=desc, 
                                 wraplength=750)
            craft_desc.pack(anchor="w", padx=10)
        
        # Música y danza
        music_label = ttk.Label(scrollable_frame, text="Música y Danza", 
                              style='Subtitle.TLabel')
        music_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        music_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=5, font=('Helvetica', 11))
        music_text.insert(tk.INSERT, trad_data['musica_danza'])
        music_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        music_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Instrumentos musicales
        instruments_frame = ttk.Frame(scrollable_frame, style='TFrame')
        instruments_frame.pack(fill=tk.X, padx=20, pady=5)
        
        instruments_label = ttk.Label(instruments_frame, text="Instrumentos musicales tradicionales:", 
                                    font=('Helvetica', 11, 'italic'))
        instruments_label.pack(anchor="w", pady=(5, 5))
        
        for instrument in trad_data['instrumentos_musicales']:
            inst_label = ttk.Label(instruments_frame, text=f"• {instrument}")
            inst_label.pack(anchor="w", padx=10, pady=2)
    
    def create_worldview_tab(self):
        """Crea la pestaña sobre cosmovisión y espiritualidad Kichwa."""
        worldview_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(worldview_frame, text="Cosmovisión")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(worldview_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(worldview_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Datos de cosmovisión
        worldview_data = self.kichwa_data['cosmovision']
        
        # Título general
        worldview_title = ttk.Label(scrollable_frame, text="Cosmovisión y Espiritualidad Kichwa", 
                                  style='Subtitle.TLabel')
        worldview_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        # Introducción
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=5, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, worldview_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Principios fundamentales
        principles_label = ttk.Label(scrollable_frame, text="Principios Fundamentales", 
                                   style='Subtitle.TLabel')
        principles_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for principle, desc in worldview_data['principios_fundamentales'].items():
            principle_frame = ttk.Frame(scrollable_frame, style='TFrame')
            principle_frame.pack(fill=tk.X, padx=20, pady=5)
            
            principle_title = ttk.Label(principle_frame, text=principle, 
                                      font=('Helvetica', 11, 'bold'),
                                      foreground=self.colors['primary'])
            principle_title.pack(anchor="w", pady=(5, 2))
            
            principle_desc = ttk.Label(principle_frame, text=desc, 
                                     wraplength=750)
            principle_desc.pack(anchor="w", padx=10)
        
        # Relación con la naturaleza
        nature_label = ttk.Label(scrollable_frame, text="Relación con la Naturaleza", 
                               style='Subtitle.TLabel')
        nature_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        nature_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                              height=5, font=('Helvetica', 11))
        nature_text.insert(tk.INSERT, worldview_data['relacion_naturaleza'])
        nature_text.config(state='disabled', background=self.colors['background'],
                         foreground=self.colors['text'])
        nature_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        
"""
Sistema de Información sobre los Kichwas de Ecuador
==================================================
Este programa recopila y presenta información sobre 
el pueblo indígena Kichwa (Quichua) de Ecuador.

Desarrollado como parte de un proyecto universitario con enfoque
en diseño culturalmente sensible.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
import os
from datetime import datetime

class KichwaInfoSystem:
    """
    Sistema de información sobre la cultura Kichwa de Ecuador
    con interfaz gráfica culturalmente sensible.
    """
    
    def __init__(self, root):
        """Inicializa la aplicación con la ventana principal."""
        self.root = root
        self.root.title("Sistema de Información - Kichwas de Ecuador")
        self.root.geometry("900x600")
        self.root.minsize(800, 500)
        
        # Cargar datos sobre los Kichwas
        self.kichwa_data = self.load_kichwa_data()
        
        # Configuración de estilo culturalmente sensible
        self.configure_styles()
        
        # Crear la interfaz principal
        self.create_widgets()
    
    def load_kichwa_data(self):
        """Carga los datos desde un diccionario predefinido."""
        # Datos básicos sobre los Kichwas de Ecuador
        return {
            "informacion_general": {
                "introduccion": "Los Kichwas constituyen el grupo indígena más numeroso de Ecuador. Son herederos de una rica tradición cultural que ha evolucionado desde tiempos precolombinos, fusionando elementos andinos ancestrales con influencias posteriores. Se caracterizan por mantener viva su identidad a través de su idioma, prácticas comunitarias, vestimenta tradicional, artesanías, música y cosmovisión.",
                "historia": "Los Kichwas ecuatorianos son descendientes de los pueblos que habitaban la región andina antes de la llegada de los incas y los españoles. Durante el Imperio Inca (siglo XV), muchos grupos indígenas fueron 'kichwaizados' como parte de la política de unificación cultural. Con la colonización española, los Kichwas enfrentaron opresión y transformaciones sociales profundas, pero lograron preservar elementos fundamentales de su cultura. Durante los siglos XX y XXI, han protagonizado importantes movimientos de reivindicación política y cultural.",
                "distribucion_geografica": "Los pueblos Kichwas se distribuyen principalmente en la región andina (Sierra) y en partes de la Amazonía ecuatoriana. Cada región presenta variaciones culturales específicas que reflejan adaptaciones a diferentes entornos ecológicos y procesos históricos particulares.",
                "caracteristicas_culturales": [
                    "Organización social basada en comunidades y el ayllu (familia extendida).",
                    "Economía tradicional centrada en la agricultura, complementada con ganadería y artesanía.",
                    "Prácticas de reciprocidad y trabajo comunitario (minga).",
                    "Vestimenta distintiva que varía según la región, con elementos simbólicos.",
                    "Celebración de fiestas vinculadas al calendario agrícola y religioso."
                ]
            },
            "regiones": {
                "introduccion": "Los Kichwas ecuatorianos se distribuyen en distintas regiones geográficas, cada una con características culturales particulares que reflejan adaptaciones a diferentes entornos ecológicos.",
                "pueblos": {
                    "Kichwas de la Sierra": {
                        "descripcion": "Habitan las provincias andinas desde Imbabura hasta Loja. Se caracterizan por sus tradiciones agrícolas, textiles y cerámicas. Cada comunidad presenta variaciones en vestimenta, dialectos y prácticas culturales específicas.",
                        "comunidades": ["Otavalo", "Karanki", "Kayambi", "Kitu Kara", "Panzaleo", "Chibuleo", "Salasaka", "Kisapincha", "Tomabela", "Puruhá", "Kañari", "Saraguro"]
                    },
                    "Kichwas de la Amazonía": {
                        "descripcion": "Se encuentran principalmente en las provincias de Napo, Pastaza, Orellana y Sucumbíos. Su cultura refleja una profunda conexión con el entorno selvático, combinando prácticas ancestrales con adaptaciones más recientes.",
                        "comunidades": ["Napo Runa", "Pastaza Runa", "Canelos", "Quijos"]
                    }
                }
            },
            "idioma": {
                "descripcion_general": "El Kichwa o Quichua (Runa Shimi - 'lengua de la gente') es una variante del quechua, familia lingüística que se extiende por varios países andinos. En Ecuador, presenta características propias que lo diferencian de otras variantes regionales.",
                "caracteristicas": {
                    "Estructura gramatical": "Lengua aglutinante donde las palabras se forman agregando sufijos a las raíces. El orden básico de la oración es Sujeto-Objeto-Verbo.",
                    "Fonología": "Sistema vocálico de tres fonemas (a, i, u) y consonantes que incluyen sonidos particulares como el sonido /sh/ y consonantes glotalizadas.",
                    "Léxico": "Rico en términos relacionados con la naturaleza, agricultura y relaciones sociales. Incluye numerosos conceptos que reflejan su cosmovisión única."
                },
                "variaciones_dialectales": "Existen importantes diferencias dialectales entre el Kichwa de la Sierra y el de la Amazonía. Incluso dentro de la Sierra, hay variaciones notables entre provincias. El dialecto de Imbabura, por ejemplo, difiere del hablado en Chimborazo o Cañar.",
                "vocabulario_basico": [
                    ["Hola", "Imanalla", "Imanalla (imanalya)"],
                    ["Gracias", "Yupaychani", "Yupaychani (yupay-cha-ni)"],
                    ["Sí", "Ari", "Ari"],
                    ["No", "Mana", "Mana"],
                    ["Agua", "Yaku", "Yaku"],
                    ["Tierra", "Allpa", "Alypa"],
                    ["Sol", "Inti", "Inti"],
                    ["Luna", "Killa", "Kilya"],
                    ["Hombre", "Kari", "Kari"],
                    ["Mujer", "Warmi", "Warmi"]
                ],
                "estado_actual": "El Kichwa ecuatoriano es reconocido como idioma oficial de relación intercultural en la Constitución de 2008. Sin embargo, enfrenta desafíos para su preservación debido a factores como la discriminación histórica, la migración y la influencia dominante del español. Existen iniciativas educativas bilingües y esfuerzos para su revitalización, incluidos programas de educación intercultural bilingüe implementados por el Estado y organizaciones indígenas."
            },
            "tradiciones": {
                "introduccion": "Las tradiciones y costumbres de los pueblos Kichwas reflejan una cosmovisión única que integra elementos ancestrales con influencias posteriores. Estas prácticas culturales transmiten valores comunitarios y mantienen viva la identidad colectiva.",
                "festividades": {
                    "Inti Raymi (Fiesta del Sol)": "Celebrada en el solsticio de junio, marca el inicio del nuevo año agrícola. Incluye bailes, música, rituales de purificación y agradecimiento a la Pachamama (Madre Tierra) por las cosechas.",
                    "Pawkar Raymi": "Fiesta del florecimiento celebrada en febrero/marzo. Coincide con el carnaval y está asociada con el inicio de la floración del maíz.",
                    "Kulla Raymi": "Celebrada en septiembre, honra a la fertilidad femenina, la luna y la preparación de la tierra para nuevos cultivos.",
                    "Kapak Raymi": "Celebrada en diciembre, marca el solsticio de invierno y la renovación del poder comunal y político."
                },
                "vestimenta": "La vestimenta tradicional varía según la región pero mantiene elementos identificativos propios. Los hombres suelen usar poncho, sombrero y pantalón, mientras las mujeres visten anaco (falda), blusa bordada, fachalina (chal) y variedad de accesorios. Cada prenda tiene significados simbólicos relacionados con la identidad, estatus social y conexión comunitaria. Los colores y diseños transmiten mensajes sobre la procedencia, estado civil y posición en la comunidad.",
                "artesanias": {
                    "Textiles": "Los textiles Kichwas son reconocidos por sus técnicas, diseños y simbolismo. Destacan los tejidos de Otavalo, elaborados en telares tradicionales con motivos geométricos que representan elementos de su cosmología.",
                    "Cerámica": "La cerámica Kichwa se caracteriza por diseños que incorporan elementos de la naturaleza y símbolos ancestrales. Se utiliza tanto para fines utilitarios como ceremoniales."
                },
                "musica_danza": "La música y danza Kichwa expresan la conexión con la naturaleza, ciclos agrícolas y momentos importantes del ciclo vital. Géneros como el sanjuanito, yaraví y danzante acompañan celebraciones comunitarias y rituales. Los bailes suelen realizarse en círculos, representando la concepción cíclica del tiempo y la vida comunitaria.",
                "instrumentos_musicales": [
                    "Rondador (flauta de pan)",
                    "Pingullo (flauta vertical)",
                    "Bocina (instrumento de viento hecho de caña)",
                    "Chajchas (sonajeros)",
                    "Bombo (tambor)",
                    "Charango (instrumento de cuerda)"
                ]
            },
            "cosmovision": {
                "introduccion": "La cosmovisión Kichwa se basa en una comprensión del universo como un todo interconectado donde seres humanos, naturaleza y energías espirituales coexisten en relación recíproca. Esta visión del mundo orienta sus prácticas culturales, sociales y espirituales.",
                "principios_fundamentales": {
                    "Sumak Kawsay (Buen Vivir)": "Filosofía de vida que busca la armonía entre los seres humanos y la naturaleza. Propone un modelo de bienestar colectivo basado en la reciprocidad y respeto.",
                    "Relacionalidad": "Principio que establece que todo está conectado, nada existe aisladamente. Las personas, comunidades, naturaleza y cosmos forman una red de relaciones interdependientes.",
                    "Complementariedad": "Concepto que reconoce que los opuestos no se excluyen sino que se complementan y necesitan mutuamente. Se refleja en el par hombre-mujer, sol-luna, día-noche."
                },
                "relacion_naturaleza": "Para los Kichwas, la naturaleza (Pachamama) es un ser vivo con el que se mantiene una relación de reciprocidad y respeto. No se considera a la naturaleza como un recurso a explotar, sino como una madre que sustenta la vida y merece veneración. Antes de tomar de ella, se pide permiso mediante rituales y ofrendas específicas.",
                "medicina_tradicional": "La medicina Kichwa integra conocimientos botánicos, rituales de sanación y comprensión de las energías. Los yachaks (sabios) y parteras cumplen roles fundamentales como mediadores entre el mundo material y espiritual. Las prácticas incluyen el uso de plantas medicinales, limpias energéticas y rituales que buscan restaurar el equilibrio entre cuerpo, mente y espíritu."
            },
            "diseno_cultural": {
                "introduccion": "Los elementos estéticos de la cultura Kichwa reflejan su cosmovisión, historia y relación con el entorno. Colores, formas y motivos transmiten significados profundos relacionados con su identidad cultural.",
                "significado_colores": {
                    "Rojo (Puka)": "Representa la tierra, la sangre, la fuerza y la vitalidad. Simboliza el poder y la energía de la Pachamama.",
                    "Dorado/Amarillo (Killu)": "Asociado con el sol (Inti), la abundancia, las cosechas y la riqueza espiritual.",
                    "Azul (Ankas)": "Simboliza el agua, el cielo y el espacio. Representa la sabiduría y el universo.",
                    "Verde (Waylla)": "Representa la naturaleza, las plantas y la renovación. Símbolo de fertilidad y vida.",
                    "Negro (Yana)": "Asociado con la oscuridad primordial, el misterio y la transformación.",
                    "Blanco (Yurak)": "Simboliza la pureza, la claridad y la conexión con el mundo espiritual."
                },
                "chakana": "La chakana (cruz andina) es un símbolo central en la cosmovisión Kichwa. Representa la conexión entre los mundos superior e inferior, así como los cuatro elementos y direcciones. Su diseño encarna el principio de ordenamiento del cosmos.",
                "disenos_textiles": "Los textiles Kichwas incorporan diseños geométricos con significados específicos: espirales (ciclos de vida), zigzags (montañas y caminos), rombos (fertilidad), entre otros. Cada motivo transmite aspectos de su historia, territorio y concepción del universo."
            }
        }
    
    def configure_styles(self):
        """Configura los estilos de la aplicación basados en la estética Kichwa."""
        self.style = ttk.Style()
        
        # Colores inspirados en textiles Kichwas
        self.colors = {
            'primary': '#8B2323',     # Rojo oscuro (bayeta) - Simboliza la tierra y la fuerza
            'secondary': '#CD853F',   # Marrón claro (lana natural) - Conexión con la tradición
            'accent': '#FFD700',      # Dorado (bordados ceremoniales) - Representa al sol (Inti)
            'background': '#F5F5DC',  # Beige claro (color natural de fibras) - Pureza y tradición
            'text': '#343e40',        # Gris oscuro para texto - Sabiduría ancestral
            'highlight': '#228B22'    # Verde para resaltar - Simboliza la Pachamama (Madre Tierra)
        }
        
        # Configurar estilos personalizados
        self.style.configure('TFrame', background=self.colors['background'])
        self.style.configure('TNotebook', background=self.colors['background'])
        self.style.configure('TNotebook.Tab', background=self.colors['secondary'],
                            foreground=self.colors['text'], padding=[10, 5])
        self.style.map('TNotebook.Tab', background=[('selected', self.colors['primary'])],
                    foreground=[('selected', 'red')])
        self.style.configure('TLabel', background=self.colors['background'],
                           foreground=self.colors['text'], font=('Helvetica', 11))
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'),
                           foreground=self.colors['primary'])
        self.style.configure('Subtitle.TLabel', font=('Helvetica', 14, 'bold'),
                           foreground=self.colors['secondary'])
        self.style.configure('TButton', background=self.colors['primary'],
                           foreground='red', font=('Helvetica', 11))
        
        # Configurar el aspecto general de la ventana
        self.root.configure(bg=self.colors['background'])
    
    def create_widgets(self):
        """Crea y organiza los widgets de la interfaz."""
        # Marco principal
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = ttk.Label(main_frame, text="Pueblo Kichwa del Ecuador",
                              style='Title.TLabel')
        title_label.pack(pady=(10, 20))
        
        # Crear un notebook (pestañas)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Crear pestañas
        self.create_overview_tab()
        self.create_regions_tab()
        self.create_language_tab()
        self.create_traditions_tab()
        self.create_worldview_tab()
        self.create_design_tab()
        
        # Barra de estado
        status_frame = ttk.Frame(main_frame, style='TFrame')
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, 
                                    text=f"Desarrollado para diseño culturalmente sensible | Fecha: {datetime.now().strftime('%d-%m-%Y')}")
        self.status_label.pack(side=tk.LEFT)
        
        about_button = ttk.Button(status_frame, text="Acerca de", 
                                command=self.show_about)
        about_button.pack(side=tk.RIGHT, padx=5)
    
    def show_about(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo(
            "Acerca de",
            "Sistema de Información sobre los Kichwas de Ecuador\n\n"
            "Desarrollado como parte de un proyecto universitario\n"
            "con enfoque en diseño culturalmente sensible.\n\n"
            "Este programa busca promover el conocimiento y la\n"
            "apreciación de la cultura Kichwa ecuatoriana."
        )
    
    def create_overview_tab(self):
        """Crea la pestaña de información general sobre los Kichwas."""
        overview_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(overview_frame, text="Información General")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(overview_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(overview_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido
        overview_data = self.kichwa_data['informacion_general']
        
        subtitle = ttk.Label(scrollable_frame, text="¿Quiénes son los Kichwas?", 
                           style='Subtitle.TLabel')
        subtitle.pack(anchor="w", pady=(10, 5), padx=10)
        
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=6, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, overview_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Historia
        history_label = ttk.Label(scrollable_frame, text="Historia", 
                                style='Subtitle.TLabel')
        history_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        history_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                               height=8, font=('Helvetica', 11))
        history_text.insert(tk.INSERT, overview_data['historia'])
        history_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        history_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Geografía y distribución
        geography_label = ttk.Label(scrollable_frame, text="Distribución Geográfica", 
                                  style='Subtitle.TLabel')
        geography_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        geography_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                                 height=4, font=('Helvetica', 11))
        geography_text.insert(tk.INSERT, overview_data['distribucion_geografica'])
        geography_text.config(state='disabled', background=self.colors['background'],
                            foreground=self.colors['text'])
        geography_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Características culturales destacadas
        cultural_label = ttk.Label(scrollable_frame, text="Características Culturales Destacadas", 
                                 style='Subtitle.TLabel')
        cultural_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for idx, caracteristica in enumerate(overview_data['caracteristicas_culturales']):
            caract_frame = ttk.Frame(scrollable_frame, style='TFrame')
            caract_frame.pack(fill=tk.X, padx=20, pady=2)
            
            bullet = ttk.Label(caract_frame, text=f"•", 
                             foreground=self.colors['primary'])
            bullet.pack(side=tk.LEFT, padx=(0, 5))
            
            caract_text = ttk.Label(caract_frame, text=caracteristica, 
                                  wraplength=700)
            caract_text.pack(side=tk.LEFT, anchor="w")
    
    def create_regions_tab(self):
        """Crea la pestaña de regiones donde habitan los Kichwas."""
        regions_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(regions_frame, text="Regiones")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(regions_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(regions_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Título
        regions_title = ttk.Label(scrollable_frame, 
                                text="Pueblos Kichwas por Regiones Geográficas", 
                                style='Subtitle.TLabel')
        regions_title.pack(anchor="w", pady=(10, 15), padx=10)
        
        # Introducción
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, self.kichwa_data['regiones']['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Regiones específicas
        for region, info in self.kichwa_data['regiones']['pueblos'].items():
            region_frame = ttk.Frame(scrollable_frame, style='TFrame')
            region_frame.pack(fill=tk.X, expand=True, padx=10, pady=10)
            
            region_title = ttk.Label(region_frame, text=region, 
                                   font=('Helvetica', 13, 'bold'),
                                   foreground=self.colors['primary'])
            region_title.pack(anchor="w", pady=(5, 10))
            
            # Descripción
            desc_text = scrolledtext.ScrolledText(region_frame, wrap=tk.WORD, 
                                                height=4, font=('Helvetica', 11))
            desc_text.insert(tk.INSERT, info['descripcion'])
            desc_text.config(state='disabled', background=self.colors['background'],
                           foreground=self.colors['text'])
            desc_text.pack(fill=tk.X, expand=False, padx=5, pady=5)
            
            # Pueblos/Comunidades
            communities_label = ttk.Label(region_frame, text="Comunidades principales:", 
                                        font=('Helvetica', 11, 'italic'))
            communities_label.pack(anchor="w", padx=5, pady=(10, 5))
            
            communities_frame = ttk.Frame(region_frame, style='TFrame')
            communities_frame.pack(fill=tk.X, padx=15)
            
            # Crear una cuadrícula de comunidades
            row = 0
            col = 0
            for community in info['comunidades']:
                comm_label = ttk.Label(communities_frame, text=f"• {community}")
                comm_label.grid(row=row, column=col, sticky="w", padx=5, pady=2)
                col += 1
                if col > 1:  # 2 columnas
                    col = 0
                    row += 1
    
    def create_language_tab(self):
        """Crea la pestaña de información lingüística sobre el Kichwa."""
        language_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(language_frame, text="Idioma")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(language_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(language_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Título y descripción general
        language_title = ttk.Label(scrollable_frame, text="Kichwa Ecuatoriano (Runa Shimi)", 
                                 style='Subtitle.TLabel')
        language_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        lang_data = self.kichwa_data['idioma']
        
        general_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                               height=5, font=('Helvetica', 11))
        general_text.insert(tk.INSERT, lang_data['descripcion_general'])
        general_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        general_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Características lingüísticas
        features_label = ttk.Label(scrollable_frame, text="Características Lingüísticas", 
                                 style='Subtitle.TLabel')
        features_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for feature, desc in lang_data['caracteristicas'].items():
            feature_frame = ttk.Frame(scrollable_frame, style='TFrame')
            feature_frame.pack(fill=tk.X, padx=20, pady=5)
            
            feature_title = ttk.Label(feature_frame, text=feature, 
                                    font=('Helvetica', 11, 'bold'),
                                    foreground=self.colors['secondary'])
            feature_title.pack(anchor="w", pady=(5, 2))
            
            feature_desc = ttk.Label(feature_frame, text=desc, 
                                   wraplength=750)
            feature_desc.pack(anchor="w", padx=10)
        
        # Vocabulario básico
        vocab_label = ttk.Label(scrollable_frame, text="Vocabulario Básico", 
                              style='Subtitle.TLabel')
        vocab_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        # Crear tabla de vocabulario
        vocab_frame = ttk.Frame(scrollable_frame, style='TFrame')
        vocab_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Encabezados
        header_spanish = ttk.Label(vocab_frame, text="Español", 
                                 font=('Helvetica', 11, 'bold'))
        header_spanish.grid(row=0, column=0, padx=5, pady=5)
        
        header_kichwa = ttk.Label(vocab_frame, text="Kichwa", 
                                font=('Helvetica', 11, 'bold'))
        header_kichwa.grid(row=0, column=1, padx=5, pady=5)
        
        header_pronunciation = ttk.Label(vocab_frame, text="Pronunciación", 
                                       font=('Helvetica', 11, 'bold'))
        header_pronunciation.grid(row=0, column=2, padx=5, pady=5)
        
        # Palabras
        for i, (spanish, kichwa, pron) in enumerate(lang_data['vocabulario_basico']):
            spanish_label = ttk.Label(vocab_frame, text=spanish)
            spanish_label.grid(row=i+1, column=0, padx=5, pady=2, sticky="w")
            
            kichwa_label = ttk.Label(vocab_frame, text=kichwa)
            kichwa_label.grid(row=i+1, column=1, padx=5, pady=2, sticky="w")
            
            pron_label = ttk.Label(vocab_frame, text=pron)
            pron_label.grid(row=i+1, column=2, padx=5, pady=2, sticky="w")
        
        # Estado actual del idioma
        status_label = ttk.Label(scrollable_frame, text="Estado Actual del Idioma", 
                               style='Subtitle.TLabel')
        status_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        status_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                              height=6, font=('Helvetica', 11))
        status_text.insert(tk.INSERT, lang_data['estado_actual'])
        status_text.config(state='disabled', background=self.colors['background'],
                         foreground=self.colors['text'])
        status_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Variaciones dialectales
        dialect_label = ttk.Label(scrollable_frame, text="Variaciones Dialectales", 
                                style='Subtitle.TLabel')
        dialect_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        dialect_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                              height=4, font=('Helvetica', 11))
        dialect_text.insert(tk.INSERT, lang_data['variaciones_dialectales'])
        dialect_text.config(state='disabled', background=self.colors['background'],
                         foreground=self.colors['text'])
        dialect_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
    
    def create_traditions_tab(self):
        """Crea la pestaña de tradiciones y prácticas culturales."""
        traditions_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(traditions_frame, text="Tradiciones")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(traditions_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(traditions_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido
        trad_data = self.kichwa_data['tradiciones']
        
        # Introducción
        trad_title = ttk.Label(scrollable_frame, text="Tradiciones y Costumbres", 
                             style='Subtitle.TLabel')
        trad_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, trad_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Festividades
        fest_label = ttk.Label(scrollable_frame, text="Principales Festividades", 
                             style='Subtitle.TLabel')
        fest_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for festival, desc in trad_data['festividades'].items():
            fest_frame = ttk.Frame(scrollable_frame, style='TFrame')
            fest_frame.pack(fill=tk.X, padx=20, pady=5)
            
            fest_title = ttk.Label(fest_frame, text=festival, 
                                font=('Helvetica', 11, 'bold'),
                                foreground=self.colors['secondary'])
            fest_title.pack(anchor="w", pady=(5, 2))
            
            fest_desc = ttk.Label(fest_frame, text=desc, wraplength=750)
            fest_desc.pack(anchor="w", padx=10)
        
        # Vestimenta
        clothing_label = ttk.Label(scrollable_frame, text="Vestimenta Tradicional", 
                                 style='Subtitle.TLabel')
        clothing_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        clothing_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                               height=6, font=('Helvetica', 11))
        clothing_text.insert(tk.INSERT, trad_data['vestimenta'])
        clothing_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        clothing_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Artesanías
        craft_label = ttk.Label(scrollable_frame, text="Artesanías", 
                              style='Subtitle.TLabel')
        craft_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for craft, desc in trad_data['artesanias'].items():
            craft_frame = ttk.Frame(scrollable_frame, style='TFrame')
            craft_frame.pack(fill=tk.X, padx=20, pady=5)
            
            craft_title = ttk.Label(craft_frame, text=craft, 
                                  font=('Helvetica', 11, 'bold'),
                                  foreground=self.colors['secondary'])
            craft_title.pack(anchor="w", pady=(5, 2))
            
            craft_desc = ttk.Label(craft_frame, text=desc, wraplength=750)
            craft_desc.pack(anchor="w", padx=10)
        
        # Música y danza
        music_label = ttk.Label(scrollable_frame, text="Música y Danza", 
                              style='Subtitle.TLabel')
        music_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        music_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=5, font=('Helvetica', 11))
        music_text.insert(tk.INSERT, trad_data['musica_danza'])
        music_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        music_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Instrumentos musicales
        inst_label = ttk.Label(scrollable_frame, text="Instrumentos Musicales Tradicionales", 
                             font=('Helvetica', 11, 'bold'))
        inst_label.pack(anchor="w", padx=20, pady=(10, 5))
        
        inst_frame = ttk.Frame(scrollable_frame, style='TFrame')
        inst_frame.pack(fill=tk.X, padx=30, pady=5)
        
        # Crear dos columnas para los instrumentos
        row = 0
        col = 0
        for instrument in trad_data['instrumentos_musicales']:
            inst_item = ttk.Label(inst_frame, text=f"• {instrument}")
            inst_item.grid(row=row, column=col, sticky="w", padx=5, pady=2)
            col += 1
            if col > 1:  # 2 columnas
                col = 0
                row += 1
    
    def create_worldview_tab(self):
        """Crea la pestaña de cosmovisión Kichwa."""
        worldview_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(worldview_frame, text="Cosmovisión")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(worldview_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(worldview_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido
        cosmo_data = self.kichwa_data['cosmovision']
        
        # Título e introducción
        cosmo_title = ttk.Label(scrollable_frame, text="Cosmovisión Kichwa", 
                              style='Subtitle.TLabel')
        cosmo_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, cosmo_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Principios fundamentales
        princ_label = ttk.Label(scrollable_frame, text="Principios Fundamentales", 
                              style='Subtitle.TLabel')
        princ_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for principle, desc in cosmo_data['principios_fundamentales'].items():
            princ_frame = ttk.Frame(scrollable_frame, style='TFrame')
            princ_frame.pack(fill=tk.X, padx=20, pady=5)
            
            princ_title = ttk.Label(princ_frame, text=principle, 
                                  font=('Helvetica', 11, 'bold'),
                                  foreground=self.colors['secondary'])
            princ_title.pack(anchor="w", pady=(5, 2))
            
            princ_desc = ttk.Label(princ_frame, text=desc, wraplength=750)
            princ_desc.pack(anchor="w", padx=10)
        
        # Relación con la naturaleza
        nature_label = ttk.Label(scrollable_frame, text="Relación con la Naturaleza", 
                               style='Subtitle.TLabel')
        nature_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        nature_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                              height=6, font=('Helvetica', 11))
        nature_text.insert(tk.INSERT, cosmo_data['relacion_naturaleza'])
        nature_text.config(state='disabled', background=self.colors['background'],
                         foreground=self.colors['text'])
        nature_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Medicina tradicional
        medicine_label = ttk.Label(scrollable_frame, text="Medicina Tradicional", 
                                 style='Subtitle.TLabel')
        medicine_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        medicine_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                               height=6, font=('Helvetica', 11))
        medicine_text.insert(tk.INSERT, cosmo_data['medicina_tradicional'])
        medicine_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        medicine_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
    
    def create_design_tab(self):
        """Crea la pestaña de elementos de diseño cultural Kichwa."""
        design_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(design_frame, text="Diseño Cultural")
        
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(design_frame, bg=self.colors['background'], 
                          highlightthickness=0)
        scrollbar = ttk.Scrollbar(design_frame, orient="vertical", 
                                command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style='TFrame')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Contenido
        design_data = self.kichwa_data['diseno_cultural']
        
        # Título e introducción
        design_title = ttk.Label(scrollable_frame, text="Elementos de Diseño Cultural", 
                               style='Subtitle.TLabel')
        design_title.pack(anchor="w", pady=(10, 5), padx=10)
        
        intro_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        intro_text.insert(tk.INSERT, design_data['introduccion'])
        intro_text.config(state='disabled', background=self.colors['background'],
                        foreground=self.colors['text'])
        intro_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Significado de los colores
        colors_label = ttk.Label(scrollable_frame, text="Significado de los Colores", 
                               style='Subtitle.TLabel')
        colors_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        for color, meaning in design_data['significado_colores'].items():
            color_frame = ttk.Frame(scrollable_frame, style='TFrame')
            color_frame.pack(fill=tk.X, padx=20, pady=3)
            
            color_name = color.split(' ')[0]  # Obtener el nombre en español
            kichwa_name = color.split(' ')[1].strip('()')  # Obtener el nombre en kichwa
            
            color_title = ttk.Label(color_frame, 
                                  text=f"{color_name} - {kichwa_name}", 
                                  font=('Helvetica', 11, 'bold'),
                                  foreground=self.colors['secondary'])
            color_title.pack(anchor="w", pady=(2, 2))
            
            color_desc = ttk.Label(color_frame, text=meaning, wraplength=750)
            color_desc.pack(anchor="w", padx=10)
        
        # Chakana
        chakana_label = ttk.Label(scrollable_frame, text="La Chakana (Cruz Andina)", 
                                style='Subtitle.TLabel')
        chakana_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        chakana_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                             height=4, font=('Helvetica', 11))
        chakana_text.insert(tk.INSERT, design_data['chakana'])
        chakana_text.config(state='disabled', background=self.colors['background'],
                          foreground=self.colors['text'])
        chakana_text.pack(fill=tk.X, expand=False, padx=15, pady=5)
        
        # Diseños textiles
        textile_label = ttk.Label(scrollable_frame, text="Diseños Textiles", 
                                style='Subtitle.TLabel')
        textile_label.pack(anchor="w", pady=(15, 5), padx=10)
        
        textile_text = scrolledtext.ScrolledText(scrollable_frame, wrap=tk.WORD, 
                                              height=4, font=('Helvetica', 11))
        textile_text.insert(tk.INSERT, design_data['disenos_textiles'])
        textile_text.config(state='disabled', background=self.colors['background'],
                         foreground=self.colors['text'])
        textile_text.pack(fill=tk.X, expand=False, padx=15, pady=5)


# Función principal para iniciar la aplicación
def main():
    root = tk.Tk()
    app = KichwaInfoSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()