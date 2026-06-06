class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        boards = accounts
# Problem:
# You are given a list of Boards, where each board contains a Board ID and a 
# list of Pin IDs saved on that board.
# However, some boards actually represent the same user collection — 
# if two boards share at least one Pin, they should be merged into the same group 
# (i.e., they belong to the same “cluster” of related boards).
# Your task is to merge all boards that share pins and return the final 
# grouped collections, where each group contains all unique Pin IDs across 
# all boards in that group.
# The order inside each result does not matter, but the groups should be distinct

# accounts = [
#   ["board12", "p1", "p2", "p3"],
#   ["board24", "p2", "p7"],
#   ["board91", "p10"],
#   ["board33", "p7", "p8"],
# ]


# we want to first group each pin to its board and if we ever see a pin appear 
# that we have already assigned a board we know it should in the end belong to
# the board it was first assigned to

# p1 -> 0
# p2 -> 0
# p3 -> 0
# p7 -> 1

# ["board12", "p1", "p2", "p3"],
# ["board24", "p2", "p7"], i = 1
        # unioning based off of board indexes
        num_boards = len(boards)
        par = {i:i for i in range(num_boards)}
        rank = {i :0 for i in range(num_boards)}

        def find(b_idx):
            p = par[b_idx]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(b1, b2):
            p1, p2 = find(b1), find(b2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True

        pin_to_board_idx = {} # pins to board index in boards
        for i, board in enumerate(boards):
            for pin in board[1:]:
                if pin in pin_to_board_idx:
                    # group together i (which is our current board to the board
                    # our pin first belonged to)
                    # other ways that we can cluster together pins
                    # BFS/DFS ->
                        # we would instead add these boards to an adj list and
                        # therefore create a graph and then we can do a bfs
                        # or dfs on each board index and then whenever we start
                        # we can have a compinents list and just add them togethert
                    union(pin_to_board_idx[pin], i)
                else:
                    pin_to_board_idx[pin] = i

        board_idx_to_pins = defaultdict(list)

        for pin,brd_idx in pin_to_board_idx.items():
            parent = find(brd_idx)
            board_idx_to_pins[parent].append(pin)
        print(board_idx_to_pins)

        res = []
        for brd_idx, pin_list in board_idx_to_pins.items():
            temp = []
            temp.append(boards[brd_idx][0])
            temp += sorted(pin_list)
            print(temp)
            res.append(temp)
        
        return res

