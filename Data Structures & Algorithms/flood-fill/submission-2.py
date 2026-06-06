class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        old_color = image[sr][sc]
        q = deque()
        if old_color == color:
            return image
        q.append((sr,sc))
        image[sr][sc] = color
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS
                        or image[nr][nc] != old_color):
                        continue
                    image[nr][nc] = color
                    q.append((nr,nc))
        return image