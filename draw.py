from svgwrite import cm, mm
import svgwrite as s
from svgwrite.shapes import Circle

def basic_shapes():
    dwg = s.Drawing(filename="text.svg", debug=True, profile='tiny')
    maxi_pawns = dwg.add(dwg.g(id='maxi_pawns', fill='white', stroke='black', stroke_width=1))
    mini_pawns = dwg.add(dwg.g(id='mini_pawns', fill='black', stroke='white', stroke_width=1))
    spaces = dwg.add(dwg.g(id='spaces', fill='white', stroke='black', stroke_width=1))
    borders = spaces = dwg.add(dwg.g(id='borders', fill='white', stroke='black', stroke_width=1))

    circle1 = dwg.circle(center=(1*cm, 1*cm), r='2mm')
    circle2 = dwg.circle(center=(3*cm, 3*cm), r='2mm')
    circle3 = dwg.circle(center=(2*cm, 3*cm), r='2mm')
    
    maxi_pawns.add(circle1)
    maxi_pawns.add(circle2)
    maxi_pawns.add(circle3)

    circle4 = dwg.circle(center=(1*cm, 2*cm), r='2mm')
    circle5 = dwg.circle(center=(3*cm, 2*cm), r='2mm')
    circle6 = dwg.circle(center=(1*cm, 3*cm), r='2mm')

    mini_pawns.add(circle4)
    mini_pawns.add(circle5)
    mini_pawns.add(circle6)

    circle7 = dwg.circle(center=(2*cm, 1*cm), r='0.7mm')
    circle8 = dwg.circle(center=(3*cm, 1*cm), r='0.7mm')
    circle9 = dwg.circle(center=(2*cm, 2*cm), r='0.7mm')

    spaces.add(circle7)
    spaces.add(circle8)
    spaces.add(circle9)

    #paragraph = dwg.add(dwg.g(font_size=14))
    #paragraph.add(dwg.text("This is a Test!", (1*cm, 2*cm)))

    dwg.save()


if __name__ == '__main__':
    basic_shapes()