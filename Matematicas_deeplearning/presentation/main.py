from manim import *

class Escena1_Definicion(Scene):
    def construct(self):
        # Título
        titulo = Tex("El Producto Punto").scale(1.5).to_edge(UP, buff=0.3)
        subtitulo = Tex("La base matemática del Machine Learning").scale(1.2).next_to(titulo, DOWN)
        autor = Tex("Por Andres Quiñones", color=GRAY).scale(1).next_to(subtitulo,DOWN)
        
        grupo_info = VGroup(titulo, subtitulo, autor)

        self.play(FadeIn(grupo_info, shift=DOWN, scale=0.5), run_time=2)
        self.wait(1)

        # Ejes y vectores
        ejes = Axes(
                    x_range=[-1, 5], 
                    y_range=[-1, 4], 
                    x_length=6, 
                    y_length=4,
                    axis_config={"include_tip": True}
                ).shift(DOWN*1.2)
        origen = ejes.c2p(0, 0)
        vec_a = Vector([2, 1], color=BLUE).shift(origen)
        vec_b = Vector([2, 3], color=YELLOW).shift(origen)
        
        et_a = MathTex(r"\vec{a}").next_to(vec_a.get_end(), RIGHT, buff=0.1)
        et_b = MathTex(r"\vec{b}").next_to(vec_b.get_end(), UP, buff=0.1)

        self.play(Create(ejes))
        self.play(
            GrowArrow(vec_a), Write(et_a),
            GrowArrow(vec_b), Write(et_b),
            run_time=2
        )
        self.wait(2)

class Escena2_Geometria(Scene):
    def construct(self):
        titulo = Tex("Interpretación: Similitud").to_edge(UP)
        self.play(Write(titulo))

        ejes = Axes(
                    x_range=[-1, 5], 
                    y_range=[-1, 4], 
                    x_length=6, 
                    y_length=4,
                    axis_config={"include_tip": True}
                ).shift(DOWN*0.5)
        origen = ejes.c2p(0, 0)

        vec_a = Vector([3, 0], color=BLUE).shift(origen)
        vec_b = Vector([3, 3], color=YELLOW).shift(origen)
        
        # Proyección (Línea punteada)
        proyeccion = DashedLine(vec_b.get_end(), [1, -1.8, 0], color=WHITE)
        
        angulo = Angle(vec_a, vec_b, radius=0.8, color=RED)
        theta = MathTex(r"\theta").next_to(angulo, UR, buff=0.1).shift(origen, UP*1.3 + RIGHT*2)

        self.play(Create(ejes), GrowArrow(vec_a), GrowArrow(vec_b))
        self.play(Create(angulo), Write(theta))
        self.wait(1)

        self.play(Create(proyeccion))
        
        explicacion = Tex("Mide qué tan ``similares'' son dos vectores.").scale(0.5).to_edge(DOWN).shift(UP*0.6)
        explicacion2 = Tex("Usando el angulo que existe entre estos dos como valor de similaridad").scale(0.5).next_to(explicacion,DOWN).shift(UP*0.2)

        formula = MathTex(r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos(\theta)").next_to(titulo, DOWN)
        
        self.play(Write(explicacion),Write(explicacion2), Write(formula))
        self.wait(2)


class Escena3_Calculo(Scene):
    def construct(self):
        titulo = Tex("¿Cómo se calcula?").to_edge(UP)
        self.play(Write(titulo))

        # Matrices / Arrays
        matriz_a = Matrix([[3], [2]], left_bracket="[", right_bracket="]").set_color(BLUE)
        punto = MathTex(r"\cdot").scale(2)
        matriz_b = Matrix([[4], [1]], left_bracket="[", right_bracket="]").set_color(YELLOW)
        
        igual = MathTex("=")
        
        operacion = MathTex(r"(3 \times 4) + (2 \times 1)")
        resultado = MathTex("= 12 + 2 = 14").set_color(GREEN)

        ecuacion = VGroup(matriz_a, punto, matriz_b, igual, operacion).arrange(RIGHT)
        ecuacion.shift(UP)
        resultado.next_to(operacion, DOWN, aligned_edge=LEFT)

        self.play(Write(matriz_a), Write(punto), Write(matriz_b))
        self.wait(1)
        self.play(Write(igual), Write(operacion))
        self.wait(1)
        self.play(Write(resultado))
        
        nota = Tex("Multiplicación elemento a elemento y suma.").scale(0.8).to_edge(DOWN)
        self.play(Write(nota))
        self.wait(2)


class Escena4_MachineLearning(Scene):
    def construct(self):
        titulo = Tex("Aplicación en Machine Learning").to_edge(UP)
        self.play(Write(titulo))

        # Dibujo de una neurona simple
        entrada_circ = Circle(radius=0.5, color=BLUE, fill_opacity=0.2).shift(LEFT*3 + UP*1.5)
        peso_circ = Circle(radius=0.5, color=YELLOW, fill_opacity=0.2).shift(LEFT*3 + DOWN*1.5)
        neurona = Circle(radius=1, color=GREEN, fill_opacity=0.2).shift(RIGHT*1)

        txt_x = MathTex(r"\vec{x} \text{ (Entradas)}").next_to(entrada_circ, LEFT)
        txt_w = MathTex(r"\vec{w} \text{ (Pesos)}").next_to(peso_circ, LEFT)
        txt_z = MathTex(r"z").move_to(neurona)

        flecha1 = Arrow(entrada_circ.get_right(), neurona.get_left(), buff=0.1)
        flecha2 = Arrow(peso_circ.get_right(), neurona.get_left(), buff=0.1)

        self.play(FadeIn(entrada_circ, txt_x), FadeIn(peso_circ, txt_w))
        self.play(GrowArrow(flecha1), GrowArrow(flecha2))
        self.play(FadeIn(neurona, txt_z))

        # Formula final de ML
        formula_ml = MathTex(r"z = \vec{w} \cdot \vec{x} + b").scale(1.5).next_to(neurona, RIGHT, buff=1)
        explicacion = Tex("La neurona evalúa la similitud entre los pesos y la entrada.").scale(0.8).to_edge(DOWN)

        self.play(Write(formula_ml))
        self.play(Write(explicacion))
        self.wait(3)