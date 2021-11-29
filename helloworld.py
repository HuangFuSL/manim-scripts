from manim import Scene, Create, Transform, Uncreate
from manim.mobject import geometry
from manim.utils import color


class CircleToSquare(Scene):
    """ Draw a circle - transform it to square """


    def construct(self):
        square = geometry.Square()
        square.set_fill(color.GREEN_A, opacity=0.5)
        square.set_stroke(color.GREEN_A, width=2)
        
        circle = geometry.Circle()
        circle.set_fill(color.GREEN_A, opacity=0.5)
        circle.set_stroke(color.GREEN_A, width=2)

        self.play(Create(square))
        self.wait()
        self.play(Transform(square, circle))
        self.wait()
        self.play(Uncreate(square))
