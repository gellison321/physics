from manim import *

class EllipticalOrbitAnimation(Scene):
    def construct(self):
        # Axes configuration
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": GREEN},
            x_axis_config={"numbers_to_include": range(-2, 3)},
            y_axis_config={"numbers_to_include": range(-2, 3)}
        )

        # Add axes to the scene
        self.add(axes)

        # Constants
        alpha = 1  # Semi-major axis
        beta = 1   # Semi-minor axis
        w = 3      # Angular frequency

        # Parametric function for the ellipse
        def ellipse(t):
            x = alpha * np.cos(w * t)
            y = beta * np.sin(w * t)
            return axes.c2p(x, y)  # Convert coordinates to axes points

        # Create the ellipse path
        ellipse_path = ParametricFunction(ellipse, t_range=[0, 2*PI], color=BLUE)
        self.add(ellipse_path)

        # Create a dot to move along the path
        moving_dot = Dot(color=RED).move_to(ellipse_path.get_start())
        self.add(moving_dot)

        # Animate the dot moving along the ellipse
        self.play(MoveAlongPath(moving_dot, ellipse_path, rate_func=linear), run_time=4)
        self.wait()
