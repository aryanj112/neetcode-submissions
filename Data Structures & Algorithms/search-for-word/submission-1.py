class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # go character by character and say
        # does this match the first letter of word, we want to run the 
        # dfs on all 4 edges of the part in the graph
        # base case is if the word is empty, or if we are out of bounds
        ROWS, COLS = len(board), len(board[0]) 
        path = set()
        def backtrack(r,c,curr):
            if not curr:
                return True
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] != curr[0:1] or
                (r,c) in path):
                return False
            path.add((r,c))
            new_curr = curr[1:]
            res = (backtrack(r,c+1,new_curr) or 
            backtrack(r,c-1,new_curr) or 
            backtrack(r+1,c,new_curr) or 
            backtrack(r-1,c,new_curr))

            path.remove((r,c))
            return res    
    
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = res or backtrack(i,j,word)
                if res:
                    return True

        return False

