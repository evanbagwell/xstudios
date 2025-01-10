from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

# Helper function to create a full Sudoku board
def create_full_board():
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    board = [[0 for _ in range(9)] for _ in range(9)]
    solve(board)
    return board

# Remove cells to create a puzzle
def remove_cells(board, num_holes=30):
    puzzle = [row[:] for row in board]
    holes = 0
    while holes < num_holes:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            holes += 1
    return puzzle

# API to generate Sudoku puzzle
def generate_sudoku(request):
    full_board = create_full_board()
    puzzle = remove_cells(full_board, 30)
    return JsonResponse({'puzzle': puzzle})

# Helper to validate rows, columns, and 3x3 grids
def is_valid_sudoku(board):
    # Helper to check for duplicates excluding zeros
    def is_valid_group(group):
        nums = [num for num in group if num != 0]  # Ignore empty cells
        return len(nums) == len(set(nums)) and all(1 <= num <= 9 for num in nums)

    # Validate rows
    for row in board:
        if not is_valid_group(row):
            return False

    # Validate columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    # Validate 3x3 subgrids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                board[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
            ]
            if not is_valid_group(box):
                return False

    return True

# Validate Sudoku API
@csrf_exempt
def validate_sudoku(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        solution = data.get('solution')

        # Check if the board is a valid 9x9 grid
        if not solution or len(solution) != 9 or any(len(row) != 9 for row in solution):
            return JsonResponse({'valid': False, 'error': 'Invalid board size'})

        # Perform validation
        is_valid = is_valid_sudoku(solution)
        return JsonResponse({'valid': is_valid})

    return JsonResponse({'error': 'Invalid request'}, status=400)
