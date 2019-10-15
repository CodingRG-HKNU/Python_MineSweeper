import Board


class Player_Board(Board.Board):

    def __init__(self, x, y, mine):
        # 생성자 오버로딩
        super(__class__, self).__init__(x, y)
        self.__init_Array(10)
        self.__numOpened = 0
        self.__numMines = mine
        self.gameover = False

    def __init_Array(self, k):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                self.set_cell(i, j, k)

    def open(self, x, y, b):
        if x < 0 or y < 0  or x >= self.get_row() or y >= self.get_col():
            pass
        elif not(self.__is_checked(x, y)):
            copyed = b.get_cell(x, y)

            if copyed == 9:
                self.set_cell(x, y, b.get_cell(x, y))
                self.GameOver()
            elif copyed == 0:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if (i == i and j == j) or i < 0 or j < 0 or i >= self.get_row() or j >= self.get_col():
                            continue
                        # 재귀호출
                        self.set_cell(x, y, b.get_cell(x, y))
                        self.open(i, j, b)
            else:
                self.set_cell(x, y, b.get_cell(x, y))
            # 열은 칸 수 기록
            self.__numOpened +=1
            # 승리조건
            if (self.get_row() * self.get_col() - self.__numOpened) == self.__numMines:
                self.GameClear()

    def __is_checked(self, x, y):
        checked = False
        if self.get_cell(x, y) != 10:
            checked = True
        return checked

    def GameOver(self):
        self.gameover = True
        print("Game Over..")

    def GameClear(self):
        print("Game Clear !")
        # 승리

