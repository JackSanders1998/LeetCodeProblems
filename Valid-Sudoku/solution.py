class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # estbalish sections (rows, cols, boxes)
        
        rows = board
        cols = [[],[],[],[],[],[],[],[],[]]
        boxes = [[],[],[],[],[],[],[],[],[]]

        # establish rows
        for row in board:
            cols[0].append(row[0])
            cols[1].append(row[1])
            cols[2].append(row[2])
            cols[3].append(row[3])
            cols[4].append(row[4])
            cols[5].append(row[5])
            cols[6].append(row[6])
            cols[7].append(row[7])
            cols[8].append(row[8])
        # establish boxes
        for row in board[0:3]:
            boxes[0] += row[0:3]
            boxes[1] += row[3:6]
            boxes[2] += row[6:9]
        for row in board[3:6]:
            boxes[3] += row[0:3]
            boxes[4] += row[3:6]
            boxes[5] += row[6:9]
        for row in board[6:9]:
            boxes[6] += row[0:3]
            boxes[7] += row[3:6]
            boxes[8] += row[6:9]
        
        no_dups = True
        for x in range(len(board)):
            row_visited = []
            col_visited = []
            box_visited = []
            for y in range(len(board[0])):
                if rows[x][y] in row_visited:
                    return False
                else:
                    if rows[x][y] != '.':
                        row_visited.append(rows[x][y])
                if cols[x][y] in col_visited:
                    return False
                else:
                    if cols[x][y] != '.':
                        col_visited.append(cols[x][y])
                if boxes[x][y] in box_visited:
                    return False
                else:
                    if boxes[x][y] != '.':
                        box_visited.append(boxes[x][y])
        return no_dups
            
