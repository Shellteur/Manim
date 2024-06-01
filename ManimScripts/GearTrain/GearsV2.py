

from manim import *
from manim.utils.unit import Percent

class Spiral(MovingCameraScene):
    def construct(self):


        squares = VGroup(Square(1 * 0.3))
        next_dir = [RIGHT,UP,LEFT,DOWN]
        FSeq = [1, 2, 3, 5, 8, 13, 21, 34, 55]

        for j, i in enumerate(FSeq):
            d = next_dir[j % 4]
            squares.add(Square(i * 0.3).next_to(squares, d, buff=0))

        squares.center()


        direction = [1, -1, -1, 1]
        corner = [[UL, -UL], [UR, -UR]]
        spiral = VGroup()

        for j, i in enumerate(squares):
            c = corner[j % 2]
            d = direction[j % 4]
            arc = ArcBetweenPoints(
                i.get_corner(c[0]),
                i.get_corner(c[1]),
                angle=PI / 2 * d,
                color=PURPLE_B,
                stroke_width=6,
            )
            if direction[j % 4] != 1:
                arc = arc.reverse_direction()
            spiral.add(arc)
        squares.scale(0.5)
        spiral.scale(0.5)

        self.play(FadeIn(squares, lag_ratio=1))
        self.play(LaggedStart(Create(spiral), run_time= 8))


        self.wait(4)



