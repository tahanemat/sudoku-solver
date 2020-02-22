import numpy as np

class grid:
    
    def __init__(self, grid):
        self._grid = grid
        if self.check_grid_integrity() == False:
            print('Please enter valid sudoku grid')
            raise Exception

    def get_section(self,position):
        i, j = position
        if i < 0 or i >= 9 or j < 0 or j >= 9 or type(i) != int or type(j) != int:
            return None
        section = (int(i / 3) * 3) + 1
        section += int(j / 3)
        return section

    def get_digits_in_section(self,section):
        i = int((section - 1) / 3) * 3
        j = ((section - 1) % 3) * 3
        numbers = []
        for a in range(3):
            for b in range(3):
                numbers.append(self._grid[i+a][j+b])
        return numbers

    def get_digits_in_column(self, j):
        numbers = []
        for i in range(9):
            numbers.append(self._grid[i][j])
        return numbers

    def get_digits_in_row(self, i):
        numbers = []
        for j in range(9):
            numbers.append(self._grid[i][j])
        return numbers

    def check_unique_numbers(self, numbers):
        count = {}
        for number in numbers:
            if number == 0:
                pass
            elif number > 9 or number < 0:
                print('Number outside of range 0-9')
                return False
            elif str(number) not in count:
                count[str(number)] = 1
            elif count[str(number)] == 1:
                return False
        return True

    def list_possible_numbers(self, position):
        found = [False] * 9
        i, j = position
        if self._grid[i][j] != 0:
            return []
        col_nums = self.get_digits_in_column(j)
        row_nums = self.get_digits_in_row(i)
        section = self.get_section([i,j])
        sec_nums = self.get_digits_in_section(section)
        for num in col_nums + row_nums + sec_nums:
            if num == 0:
                pass
            else:
                found[num - 1] = True

        numbers = [i+1 for i, x in enumerate(found) if x == False]
        return numbers

    def check_grid_integrity(self):
        for i in range(9):
            numbers = self.get_digits_in_column(i)
            if self.check_unique_numbers(numbers) == False:
                return False

        for i in range(9):
            numbers = self.get_digits_in_row(i)
            if self.check_unique_numbers(numbers) == False:
                return False

        for i in range(9):
            numbers = self.get_digits_in_section(i+1)
            if self.check_unique_numbers(numbers) == False:
                return False
        return True

    def add_number(self,number,position):
        i, j = position
        if self._grid[i][j] != 0:
            return 'Number already in specified position'
        else:
            self._grid[i][j] = number
            if self.check_grid_integrity() == False:
                self._grid[i][j] = 0
                print('Number breaks sudoku!')
            else:
                print('Number added')

    def autofill(self):
        filled = False
        for i in range(9):
            for j in range(9):
                possibilities = self.list_possible_numbers([i,j])
                if len(possibilities) == 1:
                    self.add_number(possibilities[0],[i,j])
                    filled = True

        if filled == True:
            self.autofill()

    def __str__(self):
        result = str(self._grid).replace('],', '],\n')
        return result

    pass

test = np.array([[8,0,6,5,1,0,7,9,3],
        [3,0,0,6,0,0,0,0,8],
        [0,0,0,3,8,0,0,1,6],
        [0,0,0,8,0,6,0,0,0],
        [0,0,0,4,0,5,0,8,0],
        [0,0,8,1,3,7,9,6,0],
        [0,0,5,9,4,3,8,0,0],
        [0,0,9,7,5,8,6,3,0],
        [0,8,3,2,6,1,4,5,9]])

my_grid = grid(test)

print(my_grid)