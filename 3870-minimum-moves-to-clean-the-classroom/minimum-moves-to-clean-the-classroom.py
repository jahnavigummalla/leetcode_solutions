from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find starting position and number/index of litter cells
        start = None
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        # No litter to collect
        if not litter:
            return 0

        total_litter = len(litter)
        target = (1 << total_litter) - 1

        # BFS state:
        # (row, col, collected_mask, remaining_energy, moves)
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))

        # Store visited states
        visited = set()
        visited.add((start[0], start[1], 0, energy))

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while q:
            r, c, mask, e, moves = q.popleft()

            # All litter collected
            if mask == target:
                return moves

            # If energy is 0, cannot make another move
            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                new_energy = e - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)

                # Reset energy at R
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_mask, new_energy)

                if state not in visited:
                    visited.add(state)
                    q.append(
                        (nr, nc, new_mask, new_energy, moves + 1)
                    )

        return -1