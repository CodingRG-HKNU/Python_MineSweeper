import Board
import random


class Mine_Board(Board.Board):

    def __init__(self, x, y, mine):
        # 생성자 오버로딩
        super(__class__, self).__init__(x, y)
        #Board.Board.__init__(x, y)
        self.__numMines = mine
        self.__set_Mine()
        self.__set_Num()

    def __set_Mine(self):
        for i in range(self.get_numMines()):
            x = self.__get_RandNum(0, self.get_row()-1)
            y = self.__get_RandNum(0, self.get_col()-1)
            if self.get_cell(x, y) == 0:
                self.set_cell(x, y, 9)
            else:
                i -= 1  # i--

    def __set_Num(self):
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                if self.get_cell(i, j) != 9:
                    n = 0
                    for i2 in range(i-1, i+2):
                        for j2 in range(j-1, j+2):
                            if (i2 == i and j2 == j) or i2 < 0 or j2 < 0 or i2 >= self.get_row() or j2 >= self.get_col():
                                continue
                            elif self.get_cell(i2, j2) == 9:
                                n += 1
                    self.set_cell(i, j, n)

    def __get_RandNum(self, r_min, r_max):
        return random.randint(r_min, r_max)

    def get_numMines(self):
        return self.__numMines



