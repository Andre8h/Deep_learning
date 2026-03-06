from manim import *

# Configuración de estilo global
config.background_color = WHITE
Mobject.set_default(color=BLACK)

class ProductoPuntoML(Scene):
    def construct(self):
        # --- ESCENA 1: Introducción ---
        titulo = Tex("El Producto Punto").scale(1.5).to_edge(UP, buff=0.5)
        subtitulo = Tex("La base matemática del Machine Learning").scale(1.1).next_to(titulo, DOWN)
        autor = Tex("Por Andres Quiñones", color=GRAY).scale(0.8).next_to(subtitulo, DOWN)
        
        grupo_intro = VGroup(titulo, subtitulo, autor)

        self.play(FadeIn(grupo_intro, shift=DOWN), run_time=1.5)
        self.wait(1)
        
        # Ejes y vectores iniciales
        ejes1 = Axes(
            x_range=[-1, 5], y_range=[-1, 4], 
            x_length=5, y_length=3,
            axis_config={"include_tip": True}
        ).shift(DOWN*1.2)
        
        vec_a1 = Vector([2, 1], color=BLUE).shift(ejes1.c2p(0, 0))
        vec_b1 = Vector([1, 3], color=YELLOW_E).shift(ejes1.c2p(0, 0)) # Cambiado color para visibilidad en blanco
        
        et_a1 = MathTex(r"\vec{a}", color=BLUE).next_to(vec_a1.get_end(), RIGHT)
        et_b1 = MathTex(r"\vec{b}", color=YELLOW_E).next_to(vec_b1.get_end(), UP)

        self.play(Create(ejes1))
        self.play(GrowArrow(vec_a1), Write(et_a1), GrowArrow(vec_b1), Write(et_b1))
        self.wait(2)

        # Transición 1: Limpiar pantalla
        self.play(FadeOut(*self.mobjects))

       # --- ESCENA 2: Interpretación y Similitud ---
        titulo2 = Tex("Interpretación: coincidencia o Similitud de vectores").to_edge(UP)
        formula = MathTex(r"\vec{a} \cdot \vec{b} = \|\vec{a}\| \|\vec{b}\| \cos(\theta)").next_to(titulo2, DOWN)
        
        ejes2 = Axes(
            x_range=[-1, 5], y_range=[-1, 4], 
            x_length=6, y_length=4,
            axis_config={"include_tip": True}
        ).shift(DOWN*0.5)

        # Definimos los vectores saliendo del origen de los ejes
        v_a = Arrow(ejes2.c2p(0,0), ejes2.c2p(3,0), color=BLUE, buff=0)
        v_b = Arrow(ejes2.c2p(0,0), ejes2.c2p(2,2), color=YELLOW_E, buff=0)
        
        # El secreto: Definir el ángulo con el vértice explícito
        angulo = Angle(v_a, v_b, radius=0.6, color=RED)
        # Posicionamos theta usando el punto medio del arco del ángulo
        theta = MathTex(r"\theta", color=RED).move_to(
            Angle(v_a, v_b, radius=0.9).point_from_proportion(0.5)
        )

        self.play(Write(titulo2), Write(formula))
        self.play(Create(ejes2), GrowArrow(v_a), GrowArrow(v_b))
        self.play(Create(angulo), Write(theta))
        
        explicacion = Tex("Mide la coincidencia entre vectores (documentos).", color=DARK_GRAY).scale(0.8).to_edge(DOWN, buff=0.7)
        self.play(Write(explicacion))
        self.wait(2)

        # TRANSICIÓN CRUCIAL: Limpieza total antes de la Escena 3
        self.play(FadeOut(*self.mobjects))
        self.wait(0.5)

        # --- ESCENA 3: Cálculo numérico ---
        titulo3 = Tex("¿Otras formas de calcular el producto punto ?").to_edge(UP)
        
        # Agrupamos para centrar mejor
        matriz_a = Matrix([[3], [2]], left_bracket="[", right_bracket="]").set_color(BLUE)
        punto = MathTex(r"\cdot").scale(2)
        matriz_b = Matrix([[4], [1]], left_bracket="[", right_bracket="]").set_color(YELLOW_E)
        igual = MathTex("=")
        operacion = MathTex(r"(3 \times 4) + (2 \times 1)").scale(0.9)
        
        ecuacion_completa = VGroup(matriz_a, punto, matriz_b, igual, operacion).arrange(RIGHT, buff=0.3).shift(UP*0.5)
        
        resultado = MathTex("= 12 + 2 = 14").set_color(GREEN_E).next_to(operacion, DOWN, aligned_edge=LEFT)

        self.play(Write(titulo3))
        self.play(FadeIn(ecuacion_completa))
        self.wait(1)
        self.play(Write(resultado))
        
        nota = Tex("Multiplicación elemento a elemento de cada vector", color=GRAY).scale(0.8).next_to(ecuacion_completa, DOWN)
        nota2= Tex("se suma los valores obtenidos de las multiplicaciones.", color=GRAY).scale(0.8).next_to(nota, DOWN)

        self.play(Write(nota))
        self.play(Write(nota2))
        self.wait(3)

        # Limpieza para la Escena 4
        self.play(FadeOut(*self.mobjects))

        # --- ESCENA 4: Aplicación en Machine Learning ---
        titulo4 = Tex("Aplicación en Machine Learning").to_edge(UP)
        
        # Red neuronal simplificada
        ent_circ = Circle(radius=0.4, color=BLUE, fill_opacity=0.1).shift(LEFT*3 + UP*1)
        peso_circ = Circle(radius=0.4, color=YELLOW_E, fill_opacity=0.1).shift(LEFT*3 + DOWN*1)
        neurona = Circle(radius=0.7, color=GREEN_E, fill_opacity=0.2).shift(RIGHT*1.5)

        txt_x = MathTex(r"\vec{x}", color=BLUE).next_to(ent_circ, LEFT)
        txt_w = MathTex(r"\vec{w}", color=YELLOW_E).next_to(peso_circ, LEFT)
        txt_z = MathTex(r"z").move_to(neurona)

        f1 = Arrow(ent_circ.get_right(), neurona.get_left(), buff=0.1)
        f2 = Arrow(peso_circ.get_right(), neurona.get_left(), buff=0.1)

        formula_ml = MathTex(r"z = \vec{w} \cdot \vec{x} + b").scale(1.2).next_to(neurona, RIGHT, buff=0.8)
        desc_ml = Tex("La neurona evalúa la coincidencia entre entrada y pesos.", color=DARK_GRAY).scale(0.7).to_edge(DOWN)

        self.play(Write(titulo4))
        self.play(FadeIn(ent_circ, txt_x), FadeIn(peso_circ, txt_w))
        self.play(GrowArrow(f1), GrowArrow(f2))
        self.play(FadeIn(neurona, txt_z))
        self.play(Write(formula_ml))
        self.play(Write(desc_ml))
        self.wait(4)
        
        # Cierre final
        self.play(FadeOut(*self.mobjects))