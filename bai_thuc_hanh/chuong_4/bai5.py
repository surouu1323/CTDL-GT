class HanoiTower:
    def __init__(self, n):
        self.n = n
        self.moves = []

    def move(self, n, start, end, middle):
        if n == 1:
            self.moves.append((start, end))
        else:
            self.move(n - 1, start, middle, end)
            self.moves.append((start, end))
            self.move(n - 1, middle, end, start)

    def solve(self):
        self.move(self.n, 1, 3, 2)
        return self.moves


# Tạo một đối tượng HanoiTower với 3 tầng
tower = HanoiTower(4)

# Giải quyết bài toán
solution = tower.solve()

# In các bước di chuyển
for move in solution:
    print(f"Di chuyển từ tầng {move[0]} đến tầng {move[1]}")