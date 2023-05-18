dicci={'azul':'blue',
        'amarillo':'yelow',
        'rosado':'pink',
        'negro':'black',
        'rojo':'red',
        'naranga':'orange',
        'verde':'green',
        'dorado':'golden',
        'blanco': 'white',
        'morado': 'purple',
        'lila':'lilac',}
colores=['amarillo','azul','lila' ]

for color in colores:
    if color in dicci:
        print(color,"->", dicci[color])
    else:
        print(color, "no esta el color ") 