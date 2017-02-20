
try:
    import simplegui
    import simpleplot
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    import SimpleGUICS2Pygame.simpleplot as simpleplot

data = [(1, 1), (2, 3), (3, 5)]
simpleplot.plot_bars("Hello", 10, 10, "x", "y", data)
