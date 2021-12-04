with open('input4', 'r') as f:
    data = f.read().splitlines()

BOARD_SIZE = 5

class Board:

    UNMARKED = -1
    MARKED = 1

    def __init__(self, id):
        self.__id = id
        self.__num_rows = 0
        self.__numbers = dict()
        self.__rows = [BOARD_SIZE] * BOARD_SIZE
        self.__cols = [BOARD_SIZE] * BOARD_SIZE
        #self.__left_diag = BOARD_SIZE # (0,0), (1,1)
        #self.__right_diag = BOARD_SIZE # (0,4), (1,3)

    @property
    def id(self):
        return self.__id

    def add_row(self, row):
        if self.__num_rows >= BOARD_SIZE:
            return

        for i in range(len(row)):
            n = row[i]
            if n in self.__numbers:
                raise('duplicate number')
            self.__numbers[n] = [self.__num_rows, i, Board.UNMARKED]

        self.__num_rows += 1

    def mark(self, n) -> bool:
        ''' 
        Returns if a bingo was made
        '''
        if n not in self.__numbers:
            return False

        self.__numbers[n][2] = Board.MARKED
        r = self.__numbers[n][0]
        c = self.__numbers[n][1]

        self.__rows[r] -= 1
        if self.__rows[r] == 0:
            return True
        
        self.__cols[c] -= 1
        if self.__cols[c] == 0:
            return True
        '''
        if r == c:
            self.__left_diag -= 1
            if self.__left_diag == 0:
                return True

        if r + c == BOARD_SIZE - 1:
            self.__right_diag -= 1
            if self.__right_diag == 0:
                return True
        '''
        
        return False

    def score(self) -> int:
        result = 0
        for n, info in self.__numbers.items():
            if info[2] == Board.UNMARKED:
                result += n
        return result

    def get_marked(self):
        results = set()
        for n, info in self.__numbers.items():
            if info[2] == Board.MARKED:
                results.add(n)
        print(results)

rolled_numbers = [int(x) for x in data[0].split(',')]
boards = []

id = 0
board = Board(0)
ctr = 0
for row in data[2:]:
    if ctr == 5:
        boards.append(board)
        id += 1
        board = Board(id)
        ctr = 0
        continue
    
    board.add_row([int(x) for x in row.split()])
    ctr += 1

boards.append(board)

all_boards = set(range(len(boards)))
def run_bingo(rolled_numbers, boards):
    first_bingo = True

    for n in rolled_numbers:
        for b in boards:
            bingo = b.mark(n)
            if bingo and first_bingo:
                print('part a:', b.score() * n)
                first_bingo = False
            elif bingo:
                all_boards.discard(b.id)
                if len(all_boards) == 0:
                    print('part b:', b.score() * n)
                    return

run_bingo(rolled_numbers, boards)