# class Chess:

#     pieces = {1:"♚",
#                 2:"♛",
#                 3:"♜",
#                 4:"♞",
#                 5:"♝",
#                 6:"♟",
#                 7:"♔",
#                 8:"♕",
#                 9:"♖",
#                 10:"♘",
#                 11:"♗",
#                 12:"♙"}
#     BS = "▓"
#     WS = "░"

#     def initializeBoard(self):
        
#         self.board = [[0 for x in range(8)] for y in range(8)]

#         self.board[0][0]=3
#         self.board[0][1]=4
#         self.board[0][2]=5
#         self.board[0][3]=1
#         self.board[0][4]=2
#         self.board[0][5]=5
#         self.board[0][6]=4
#         self.board[0][7]=3

#         self.board[1][0]=6
#         self.board[1][1]=6
#         self.board[1][2]=6
#         self.board[1][3]=6
#         self.board[1][4]=6
#         self.board[1][5]=6
#         self.board[1][6]=6
#         self.board[1][7]=6

#         self.board[7][0]=9
#         self.board[7][1]=10
#         self.board[7][2]=11
#         self.board[7][3]=7
#         self.board[7][4]=8
#         self.board[7][5]=11
#         self.board[7][6]=10
#         self.board[7][7]=9

#         self.board[6][0]=12
#         self.board[6][1]=12
#         self.board[6][2]=12
#         self.board[6][3]=12
#         self.board[6][4]=12
#         self.board[6][5]=12
#         self.board[6][6]=12
#         self.board[6][7]=12

#     def paintBoard(self):
#         print("   a   b   c   d   e   f   g   h   ")
#         for i, row in enumerate(self.board,start=1):
#             strRow = str(i)+" "
#             for j, square in enumerate(row,start=1):

#                 c = self.BS if (i+j)%2 == 0 else self.WS

#                 if square != 0:
#                     strRow += c+self.pieces[square]+" "+c
#                 else:
#                     strRow += c*4
#             print(strRow)
#     def getIdx(self, pos):
#         x = int(pos[0]) - 1
#         y = ord(pos[1])-97
#         return (x,y)

#     def move(self, start, end):
#         xi, yi = self.getIdx(start)
#         xf, yf = self.getIdx(end)
#         self.board[xf][yf] = self.board[xi][yi]
#         self.board[xi][yi] = 0

#     def playGame(self):
#         self.paintBoard()
#         movement = input("Ingresa movimiento: ")
#         while (movement != "exit"):
#             self.move(movement[0:2],movement[3:5])
#             self.paintBoard()
#             movement = input("Ingresa movimiento: ")

#         print("G A M E   O V E R ! ")

# def run():
#     chess = Chess()
#     chess.initializeBoard()
#     input('''
# ♜ ♞ ♝ ♚ ♛ ♝ ♞ ♜  Bienvenido al juego de Ajedrez  ♖ ♘ ♗ ♔ ♕ ♗ ♘ ♖ 

# Instrucciones:
# 1. Para salir debes teclear "exit"
# 2. Las posiciones deben escribirse indicando el numero y luego la letra.
#    Ej: 2e
# 3. Para mover una ficha debes indicar la posicion inicial y la final separadas las posiciones por un espacio. 
#    Ej:
#    Ingresa movimiento: 2e 4e
#    Ingresa movimiento: 7e 5e

# Ahora solo tienes que presionar Enter para comenzar el juego!
# ''')
#     chess.playGame()

# if __name__ == "__main__":
#     run()

_CAT = ['''
                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
   ----------{_}^-'{_}----------
        ''',
        '''
      ,_     _,
      |\\___//|
      |=6   6=|
      \=._Y_.=/
       )  `  (    ,
      /       \  ((
      |       |   ))
     /| |   | |\_//
      \| |._.| |/-`
      '"'   '"'
    ''',
    '''
                        _
                       | \
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/
    ''',
    '''
    ("`-''-/").___..--''"`-._
     `6_ 6  )   `-.  (     ).`-.__.`)
     (_Y_.)'  ._   )  `._ `. ``-..-'
   _..`--'_..-_/  /--'_.' ,'
  (il).-''  (li).'  ((!.-'
    ''',
    '''
    |\      _,,,---,,_
   /,`.-'`'    -.  ;-;;,_
  |,4-  ) )-,_..;\ (  `'-'
 '---''(_/--'  `-'\_)  fL
    ''',
    '''
                 __        .-.
             .-"` .`'.    /\\|
     _(\-/)_" ,  .   ,\  /\\\/
    {(#b^d#)} .   ./,  |/\\\/
    `-.(Y).-`  ,  |  , |\.-`
         /~/,_/~~~\,__.-`
        ////~    // ~\\
      ==`==`   ==`   ==`
    ''']


Tema = '''
    B I E N V E N I D O    O R D E N A    A L    C A T
    =================================================
'''
Menu = '''
    Ordena la acción del Gatito:

    [s]entado
    [p]arado
    [c]depredador
    [d]ormido
    [a]sustado
    [x] Presione cualquier tecla para salir
'''


class Cat:
    def __init__(self, estado):
        self._estado = estado

    def sentado(self):
        self._estado = 's'
        self._display_image()

    def parado(self):
        self._estado = 'p'
        self._display_image()

    def depredador(self):
        self._estado = 'c'
        self._display_image()

    def dormido(self):
        self._estado = 'd'
        self._display_image()

    def asustado(self):
        self._estado = 'a'
        self._display_image()

    def _display_image(self):

        if self._estado == 's':
            print(_CAT[1])
        elif self._estado == 'p':
            print(_CAT[2])
        elif self._estado == 'c':
            print(_CAT[3])
        elif self._estado == 'd':
            print(_CAT[4])
        elif self._estado == 'a':
            print(_CAT[5])
        else:
            print(_CAT[0])


def run():
    print(Tema)

    cat = Cat(estado='n')
    cat._display_image()

    while True:
        print(Menu)
        estado = str(input('    Indique la acción de Gatito: ')).lower()

        if estado == 's':
            cat.sentado()
        elif estado == 'p':
            cat.parado()
        elif estado == 'c':
            cat.depredador()
        elif estado == 'd':
            cat.dormido()
        elif estado == 'a':
            cat.asustado()
        else:
            break
    

if __name__ == '__main__':
    run()