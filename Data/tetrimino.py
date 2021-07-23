class Tetrimino:
    def __init__(self, color, grid):
        self.color = color
        self.grid = grid
        self.grid_id = 0

    def __copy__(self):
        return Tetrimino(self.color, self.grid)


cyan_i = Tetrimino((0, 255, 255), ((
    (0,0,0,0),
    (1,1,1,1),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,0,1,0),
    (0,0,1,0),
    (0,0,1,0),
    (0,0,1,0)), (

    (0,0,0,0),
    (0,0,0,0),
    (1,1,1,1),
    (0,0,0,0)), (

    (0,1,0,0),
    (0,1,0,0),
    (0,1,0,0),
    (0,1,0,0))
))

blue_j = Tetrimino((0, 0, 128), ((
    (1,0,0,0),
    (1,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,1,0),
    (0,1,0,0),
    (0,1,0,0),
    (0,0,0,0)), (

    (0,0,0,0),
    (1,1,1,0),
    (0,0,1,0),
    (0,0,0,0)), (

    (0,1,0,0),
    (0,1,0,0),
    (1,1,0,0),
    (0,0,0,0))
))

orange_l = Tetrimino((255, 128, 0), ((
    (0,0,1,0),
    (1,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,0,0),
    (0,1,0,0),
    (0,1,1,0),
    (0,0,0,0)), (

    (0,0,0,0),
    (1,1,1,0),
    (1,0,0,0),
    (0,0,0,0)), (

    (1,1,0,0),
    (0,1,0,0),
    (0,1,0,0),
    (0,0,0,0))
))

yellow_o = Tetrimino((255, 255, 0), ((
    (0,1,1,0),
    (0,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,1,0),
    (0,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,1,0),
    (0,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,1,0),
    (0,1,1,0),
    (0,0,0,0),
    (0,0,0,0))
))

green_s = Tetrimino((0, 255, 0), ((
    (0,1,1,0),
    (1,1,0,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,0,0),
    (0,1,1,0),
    (0,0,1,0),
    (0,0,0,0)), (

    (0,0,0,0),
    (0,1,1,0),
    (1,1,0,0),
    (0,0,0,0)), (

    (1,0,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,0,0,0))
))


red_z = Tetrimino((255, 0, 0), ((
    (1,1,0,0),
    (0,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,0,1,0),
    (0,1,1,0),
    (0,1,0,0),
    (0,0,0,0)), (

    (0,0,0,0),
    (1,1,0,0),
    (0,1,1,0),
    (0,0,0,0)), (

    (0,1,0,0),
    (1,1,0,0),
    (1,0,0,0),
    (0,0,0,0))
))

purple_t = Tetrimino((128, 0, 128), ((
    (0,1,0,0),
    (1,1,1,0),
    (0,0,0,0),
    (0,0,0,0)), (

    (0,1,0,0),
    (0,1,1,0),
    (0,1,0,0),
    (0,0,0,0)), (

    (0,0,0,0),
    (1,1,1,0),
    (0,1,0,0),
    (0,0,0,0)), (

    (0,1,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,0,0,0))
))
