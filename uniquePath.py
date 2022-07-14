class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        firstRow = []
        sol = []
        for i in range(n):
            firstRow.append(1)
        for i in range(m):
            if i == 0:
                sol.append(firstRow)
                continue
            else:
                row = []
                for j in range(n):
                    if j == 0:
                        row.append(1)
                    else:
                        row.append(row[j-1] + sol[i-1][j])
                sol.append(row)
        return sol[m-1][n-1]