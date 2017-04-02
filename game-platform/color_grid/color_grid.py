
from collections import defaultdict


class Line(object):
    """
    Represent a line in the color grid.
    """

    def __init__(self, line_sequence=(), length=0):
        """
        :param line_sequence: number's sequence representing the black places
        """
        self.sequence = line_sequence
        self.length = length

    def set_sequence(self, sequence):
        self.sequence = sequence

    def check_line(self, sequence):
        """
        Return True if the sequence of numbers is not violated

        :param sequence: black places' sequence
        :return:
        """
        ind, n = 0, 0
        while ind < len(sequence):
            while n < len(self.sequence) and sequence[ind] > self.sequence[n]:
                n += 1
            if n == len(self.sequence) and ind < len(sequence):
                return False
            ind += 1
        return True


class ColorGrid(object):
    """
    Represent the color grid game:
      Each column and row has a sequence of numbers which describe the number of black places
    """
    WHITE = 0
    BLACK = 1
    BLOCKED = -1

    def __init__(self, length, width):
        """
        :param length: length of the grid
        :param width: width of the grid
        """
        self.grid = defaultdict()  # (i,j): boolean; True if (i,j) is black
        self.length = length
        self.width = width
        self.rows = defaultdict(Line)  # key= row's number; value= number's sequence
        self.columns = defaultdict(Line)  # key= column's number; value= number's sequence

    def set_row_sequence(self, row, sequence):
        self.rows[row].set_sequence(sequence)

    def set_column_sequence(self, col, sequence):
        self.columns[col].set_sequence(sequence)

    def is_white(self, i, j):
        return self.grid[i, j] == self.WHITE

    def is_black(self, i, j):
        return self.grid[i, j] == self.BLACK

    def is_blocked(self, i, j):
        return self.grid[i, j] == self.BLOCKED

    def set_to_white(self, i, j):
        if not 0 <= i < self.width or not 0 <= j < self.length:
            raise Exception("row %s or column %s not supported" % (i, j))
        self.grid[i, j] = self.WHITE

    def set_to_black(self, i, j):
        if not 0 <= i < self.width or not 0 <= j < self.length:
            raise Exception("row %s or column %s not supported" % (i, j))
        self.grid[i, j] = self.BLACK

    def set_to_blocked(self, i, j):
        if not 0 <= i < self.width or not 0 <= j < self.length:
            raise Exception("row %s or column %s not supported" % (i, j))
        self.grid[i, j] = self.BLOCKED

    def get_current_row_sequence(self, row):
        """
        Return the sequence of black lines on this row

        :param row: row's number
        :return:
        """
        sequence, subseq = (), 0
        for col in range(self.length):
            if self.is_black(row, col):
                subseq += 1
            else:
                if subseq > 0:
                    sequence += (subseq,)
                subseq = 0
        return sequence

    def get_current_column_sequence(self, col):
        """
        Return the sequence of black lines on this column

        :param col: column's number
        :return:
        """
        sequence, subseq = (), 0
        for row in range(self.width):
            if self.is_black(row, col):
                subseq += 1
            else:
                if subseq > 0:
                    sequence += (subseq,)
                subseq = 0
        return sequence

    def check_row(self, row):
        """
        Return True if the sequence of numbers is not violated

        :param row: row's number
        :return:
        """
        return self.rows[row].check_line(self.get_current_row_sequence(row))

    def check_column(self, col):
        """
        Return True if the sequence of numbers is not violated

        :param col: row's number
        :return:
        """
        self.columns[col].check_line(self.get_current_column_sequence(col))
