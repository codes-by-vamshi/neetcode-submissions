class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            j = board[i]
            count_dot = j.count(".")
            if count_dot > 0 and (len(set(j))-1 != 9-count_dot):
                print(j)
                return False
            if count_dot == 0 and (len(set(j)) != 9):
                print(j)
                return False
        for i in range(9):
            j = [l[i]for l in board[:]]
            count_dot = j.count(".")
            if count_dot > 0 and (len(set(j))-1 != 9-count_dot):
                print(j)
                return False
            if count_dot == 0 and (len(set(j)) != 9):
                print(j)
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                k = [l[j:j+3] for l in board[i:i+3]]
                k = [item for row in k for item in row]
                count_dot = k.count(".")
                if count_dot > 0 and (len(set(k))-1 != 9-count_dot):
                    print(k)
                    return False
                if count_dot == 0 and (len(set(k)) != 9):
                    print(k)
                    return False
        return True