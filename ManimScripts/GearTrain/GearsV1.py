from manim import *


class Hundred(Scene):

    def construct(self):

        # This Scene renders 120 files exceeding
        # the default limit of max_files_cached
        config.max_files_cached = -1
        # -1 sets max_files_cached to unlimited

        NP = NumberPlane(x_range=(-3.01, 3.01, 1), y_range=(-3.01,
                         3.01, 1), axis_config={'stroke_width': 5},
                         background_line_style={'stroke_color': TEAL,
                         'stroke_width': 3, 'stroke_opacity': 0.6})

        (RedGear, BlueGear) = SVGMobject('Gears.svg')
        BlueGear.scale(2).center()

        fps = 60
        dt = 1 / fps
        run_time = 2

        self.add(NP, BlueGear)

        for i in range(fps * run_time):
            BlueGear.rotate(dt * 180 * DEGREES)
            self.wait(dt)
            self.wait(3)