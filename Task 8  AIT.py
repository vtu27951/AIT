def solve_n_queens(n):
  def backtrack(row, cols, diag1, diag2):
    if row == n:
      return 1
    count = 0
    for col in range(n):
      if col in cols or (row - col) in diag1 or (row + col) in diag2:
        continue
      cols.add(col)
      diag1.add(row - col)
      diag2.add(row + col)
      count += backtrack(row + 1, cols, diag1, diag2)
      cols.remove(col)
      diag1.remove(row - col)
      diag2.remove(row + col)
    return count


# --- Input Explanation ---
# 'n' represents the board dimension (N x N) and number of queens.
# We test for N = 4, 8, and 12 as requested.
for n in [4, 8, 12]:
  solutions = solve_n_queens(n)
  print(f"N = {n} -> Total Solutions: {solutions}")
                               
