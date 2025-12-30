class Solution:
    def get(self, board: List[List[str]], row: int, col: int) -> str:
        candidate_row = board[row]
        item = candidate_row[col]
        return item

    def get_box(self, board: List[List[str]], row: int, col: int) -> [str]:
        origin_row = row * 3
        origin_col = col * 3
        result = []
        for i in range(3):
            for j in range(3):
                result.append(self.get(board, origin_row + i, origin_col + j))

        return result

    def isValidSudoku0(self, board: List[List[str]]) -> bool:
        # rows    
        for i in range(9):
            seen_numbers = set()
            for j in range(9):
                item = self.get(board, i, j)
                if item == ".":
                    continue
                if item in seen_numbers:
                    return False
                seen_numbers.add(item)

        # columns
        for i in range(9):
            seen_numbers = set()
            for j in range(9):
                item = self.get(board, j, i)
                if item == ".":
                    continue
                if item in seen_numbers:
                    return False
                seen_numbers.add(item)

        # boxes
        for i in range(3):
            for j in range(3):
                box = self.get_box(board, i,j)
                seen_numbers = set()
                for item in box:
                    if item == ".":
                        continue
                    if item in seen_numbers:
                        return False
                    seen_numbers.add(item)
        
        return True


        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        side_length = len(board)
        sub_box = int(side_length**0.5)
        rows = [set() for _ in range(side_length)]
        cols = [set() for _ in range(side_length)]
        boxes = [set() for _ in range(side_length)]

        for r in range(side_length):
            for c in range(side_length):
                val = board[r][c]
                if val == ".": continue
            
                # The "Secret" Box Index math:
                box_idx = (r // sub_box) * sub_box + (c // sub_box)
            
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
            
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        return True
