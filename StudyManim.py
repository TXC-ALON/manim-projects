from big_ol_pile_of_manim_imports import *

class Polygon(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        square = Square()

        self.play(ShowCreation(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(square))

class TextTransform(Scene):
    def construct(self):
        text = TextMobject(
            "this is a text",
            tex_to_color_map={"text": YELLOW}
        )
        trans_text = TextMobject(
            "this is another text",
            tex_to_color_map={"text": RED}
        )
        self.play(Write(text))
        self.play(Transform(text, trans_text))
        self.wait()

class TexTransform(Scene):
    def construct(self):
        tex = TexMobject(
            "\\sum_{n=1010a}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\tau^2}{6}"
        )
        trans_tex = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        self.play(Write(tex))
        self.play(Transform(tex, trans_tex))
        self.wait()

class MoveText(Scene):
    def construct(self):
        title = TextMobject(
            "Tony is trying manim",
            tex_to_color_map={"manim": RED}
        )
        trans_title = TextMobject(
            "Tony is learning manim",
            tex_to_color_map={"manim": YELLOW}
        )
        trans_title.to_corner(UP)
        transform_title = TextMobject(
            "Tony is learning manim",
            tex_to_color_map={"manim": ORANGE}
        )
        transform_title.to_corner(UP + LEFT)

        self.play(Write(title))
        self.play(Transform(title, trans_title))
        self.wait()
        self.play(Transform(title, transform_title))
        self.wait()

class TabTransform(Scene):
    def construct(self):
        tab = TextMobject(
            "\\begin{tabular}{ccc}"
            "\\toprule"
            "Name& Number& Sex\\\\"
            "\\midrule"
            "Steve Jobs& 001& Male\\\\"
            "Bill Gates& 002& Female\\\\"
            "\\bottomrule"
            "\\end{tabular}"
        )

        transform_tab = TextMobject(
            "\\begin{tabular}{ccc}"
            "\\toprule"
            "Name& Number& Sex\\\\"
            "\\midrule"
            "Steve Jobs& 001& Male\\\\"
            "Tony Wang& 002& Female\\\\"
            "\\bottomrule"
            "\\end{tabular}"
        )
        self.play(Write(tab))
        self.play(Transform(tab, transform_tab))
        self.wait()

class PrintAuthor(Scene):
    def construct(self):
        author = TextMobject(
            "@Tony鹤翔万里",
            tex_to_color_map={"@Tony鹤翔万里": [BLUE, YELLOW, ORANGE, RED]}
        )
        author.scale(1.5)
        author.to_corner(LEFT + DOWN)
        self.add(author)

class NumberPlaneTest(Scene):
    def construct(self):
        grid = NumberPlane()
        grid_title = TextMobject("空间坐标系")
        grid_title.scale(1.5)
        grid_title.to_corner(UP)

        self.play(
            Write(grid),
            FadeInFromDown(grid_title),
        )
        self.wait()
        grid_transform_title = TextMobject("放大")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        grid.prepare_for_nonlinear_transform()
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p * np.array([ 2, 2, 0, ]),
            run_time=3,
        )
        self.wait()
        grid.prepare_for_nonlinear_transform()
        grid_transform_title = TextMobject("平移")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p + np.array([2, 1, 0, ]),
            run_time=3,
        )
        self.wait()
        grid.prepare_for_nonlinear_transform()
        grid_transform_title = TextMobject("线性变换")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p + np.array([ p[1] , 0, 0,]),
            run_time=3,
        )
        self.wait()
        grid.prepare_for_nonlinear_transform()
        grid_transform_title = TextMobject("非线性变换")
        grid_transform_title.to_corner(UP)
        grid_transform_title.scale(1.5)
        self.play(
            Transform(grid_title, grid_transform_title),
            grid.apply_function,
            lambda p: p + np.array([ np.sin(p[1]) , np.sin(p[0]) , 0,]),
            run_time=3,
        )

class VideoStart(Scene):
    CONFIG = {
        "Author"        : "@鹤翔万里",
        "title_name"    : "测试",
        "svg_filename"  : "TonySVG",
        "author_colors" : [BLUE, YELLOW, ORANGE, RED],
    }
    def construct(self):
        author = TextMobject(
            self.Author,
            tex_to_color_map={self.Author : self.author_colors}
        )
        svg_file = SVGMobject(file_name = self.svg_filename)
        svg_file.to_corner(UP)

        title = TextMobject(self.title_name)
        title.to_corner((BOTTOM + ORIGIN))
        self.play(
            FadeInFromDown(svg_file),
            Write(author)
        )
        self.play(
            Write(title)
        )
        self.wait()
        self.play(
            LaggedStart(FadeOutAndShiftDown, author),
            FadeOut(title),
            run_time = 0.5,
        )

class TrySurroundingRectangle(Scene):
    def construct(self):
        text = TextMobject(
            "Here is a ", "text",
        )
        text.to_edge(TOP)
        text_rect = SurroundingRectangle(text[1])
        another_text = TextMobject(
            "That ", "text", " is created by Tony"
        )
        another_text_rect = SurroundingRectangle(another_text[1])
        text_arrow = Arrow(
            another_text[1].get_top(), text[1].get_bottom(),
            tip_length = 0.15
        )

        self.play(Write(text))
        self.play(ShowCreation(text_rect))
        self.wait()
        self.play(Write(another_text), run_time=0.5)
        self.play(ShowCreation(another_text_rect))
        self.play(ShowCreation(text_arrow))
        self.wait()