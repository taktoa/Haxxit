import mapfuncs

class map(mapfuncs.funcs):
    layout = [[1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1],
              [1,1,0,0,1,1,0,0,1,1],
              [1,1,0,1,1,1,1,0,1,1],
              [1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1],
              [1,1,0,1,1,1,1,0,1,1],
              [1,1,0,0,1,1,0,0,1,1],
              [1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1]]
    spawns = [(0,0), (1,0), (0,1)]
    enemies = [('Spammer',(9,9)), ('Spammer',(9,8)), ('Spammer',(8,9))]
