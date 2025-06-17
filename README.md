# Grid Pathfinding Algorithms

This project implements and compares three pathfinding algorithms on an NxN grid with obstacles. The grid contains:

- `0` → walkable cell  
- `1` → blocked cell (obstacle)  

The goal is to find a path from the **top-left corner (0,0)** to the **bottom-right corner (N-1, N-1)**.

---

## Implemented Algorithms

✅ Breadth-First Search (BFS)  
✅ Depth-First Search (DFS)  
✅ Bidirectional Search  
❌ Dijkstra (not required for this grid as all moves have equal cost)

---

## How It Works

- The grid is generated with random obstacles (1s).
- The algorithms explore valid paths in the grid.
- Output is printed as the sequence of visited nodes and success/failure to reach the goal.

---
