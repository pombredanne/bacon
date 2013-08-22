import logging
logging.basicConfig()

import bacon
bacon.window.resizable = True

font = bacon.Font('res/DejaVuSans.ttf', 64)
font2 = bacon.Font('res/DejaVuSans.ttf', 72)

runs = [
    bacon.GlyphRun(bacon.Style(font), 'Hello, '),
    bacon.GlyphRun(bacon.Style(font2, color=(1, 0.5, 0.5, 1)), 'Bacon'),
    bacon.GlyphRun(bacon.Style(font), '!'),
]
glyph_layout = bacon.GlyphLayout(runs)

class Game(bacon.Game):
    def on_tick(self):
        bacon.clear(0, 0, 0, 1)
        bacon.draw_glyph_layout(glyph_layout, bacon.window.width / 2, bacon.window.height / 2, align=bacon.TextAlignment.center | bacon.TextAlignment.vertical_center)
bacon.run(Game())