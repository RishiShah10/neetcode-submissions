class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        If any of the O's in a dfs are touching the edge then they are not surronded
        go through the list, dfs on an O when you see
        1) find all its connections. if none of them are touching an edge of the board them modify
        all vals in the visited set to X
        """
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(visited, pos):
            i,j = pos
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i,j) not in visited and board[i][j] == "O":
                visited.add((i,j)) 
                
                is_border = (
                    i == 0 or 
                    i == len(board) - 1 or 
                    j == 0 or 
                    j == len(board[0]) - 1
                )
                
                connected_to_border = False
                for di, dj in directions:
                    connected_to_border = connected_to_border or dfs(visited, (i+di, j+dj))
                
                return is_border or connected_to_border

                


            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    visited = set()
                    border = dfs(visited,(i,j))
                    if border != True:
                        for (x,y) in visited:
                            board[x][y] = "X"