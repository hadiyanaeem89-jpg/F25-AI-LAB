Lab 3: Uninformed Search
Student Information
- Name:  Hadiya Naeem
 
- Course: Artificial Intelligence
- Lab: 03 -- Uninformed Search
1. Introduction
This lab explains uninformed search algorithms. These algorithms search
for a goal without using heuristic information. The lab includes
Breadth-First Search (BFS), Depth-First Search (DFS), Depth-Limited
Search (DLS), Iterative Deepening Depth-First Search (IDDFS), and
Uniform Cost Search (UCS).
2. Graph for BFS and DFS
The original graph used for the BFS and DFS tasks is:
        A
       / \\
      B   C
     / \\   \\
    D   E   F
        |
        G
The graph in Python form:
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
The start node is A, and the goal node is G. The order of
neighbours affects the order in which nodes are visited.
3. Task 1: Breadth-First Search and Depth-First Search
Breadth-First Search (BFS)
BFS explores nodes level by level. It uses a queue (First In, First
Out).

Expected visit order: - A, B, C, D, E, F, G

Expected path to the goal: - A → B → E → G
Depth-First Search (DFS)
DFS explores one branch as far as possible before going back. It uses a
stack (Last In, First Out).

Expected visit order with the neighbour order shown above: - A, B, D, E,
G

Expected path to the goal: - A → B → E → G
Manual trace
Show the processed node and the queue or stack after each step.

BFS trace

  Processed node   Queue after processing
  A                B, C
B                C, D, E
C                D, E, F
D                E, F
E                F, G
F                G
G                Empty

DFS trace

  Processed node   Stack after processing (next node is at the left)
  A                B, C
B                D, E, C
D                E, C
E                G, C
G                Stop

Screenshots to add: Insert screenshots of your BFS and DFS code,
outputs, and manual trace tables.
4. Task 2: Depth-Limited Search and Iterative Deepening DFS
Depth-Limited Search (DLS)
DLS works like DFS but does not search deeper than a selected depth
limit.

The goal G is at depth 3 when A is at depth 0.

Test DLS using limits 1, 2, 3, and 4. Record the actual status and path
for each run.
Depth limit Expected result

          1 CUTOFF
          2 CUTOFF
          3 FOUND
          4 FOUND
Iterative Deepening DFS (IDDFS)
IDDFS runs DLS repeatedly, increasing the depth limit each time. It
stops when it finds the goal.

Expected result: - Limits 0, 1, and 2: CUTOFF - Limit 3: FOUND - Path: A
→ B → E → G

Use the status names consistently: FOUND, CUTOFF, and FAILURE.

Screenshots to add: Insert screenshots of your DLS and IDDFS code
and outputs. Include the results for the required depth limits.
5. Task 3: Uniform Cost Search (UCS)
UCS selects the next node with the lowest total path cost. It uses a
priority queue.

For this weighted-search experiment, use the weighted graph specified by
your lab instructions. The weighted extension may include the additional
corridor C → G. Keep the original unweighted graph unchanged for the
BFS, DFS, DLS, and IDDFS tasks.
Example weighted graph
The following is an example weight assignment used to demonstrate the
required comparison. If your instructor provided different edge weights,
replace these values with the instructor's values.
weighted_graph = {
    "A": [("B", 1), ("C", 6)],
    "B": [("D", 5), ("E", 1)],
    "C": [("F", 2), ("G", 6)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}
With these example weights: - BFS may select A → C → G because it has
fewer edges. - The cost of A → C → G is 12. - UCS selects A → B → E →
G. - The cost of A → B → E → G is 3.

This demonstrates that the path with fewer edges is not always the path
with the lowest total cost.

Important: These numerical weights are an example. Use the exact
weights from your instructor if they were supplied separately.

Screenshots to add: Insert a screenshot of your weighted graph, UCS
code, processing order, selected path, and total cost.
6. How to Run the Programs
1. Open the Lab 3 folder in VS Code.
2. Open the Python file for the task you want to run.
3. Run the file using the Run button or terminal.
4. Check the output and compare it with your manual trace.
5. Save screenshots of the code and actual output.
The heapq module used for UCS is included with Python and does not
need a separate installation.
7. Suggested Folder Structure
Lab3/
├── lab3_bfs_dfs.py
├── lab3_depth_search.py
├── lab3_ucs.py
├── README.md
├── Lab3_Report.docx
└── outputs/
    ├── bfs_output.png
    ├── dfs_output.png
    ├── dls_output.png
    ├── iddfs_output.png
    ├── weighted_graph.png
    └── ucs_output.png
Use the actual names of your files if they are different. Include all
source files used for the lab.
8. Failure or Edge-Case Analysis
Test what happens when the goal cannot be reached from the start node.
Record whether the algorithm reports that no path was found. If you
include this experiment, use a modified graph, run your code, and add
the actual output to your report.
9. Reflection
In this lab, I learned how BFS and DFS explore a graph in different
ways. I also learned how DLS uses a depth limit and how IDDFS increases
that limit step by step. Finally, I learned that UCS uses path costs to
find a lowest-cost path.
10. Responsible Practice
I kept the original graph for the uninformed search tasks and used a
separate weighted graph for the UCS experiment. I recorded the actual
processing order and path costs produced by my code. I also identified
any example edge weights that were not supplied by the instructor.
11. Conclusion
This lab helped me understand five search algorithms: BFS, DFS, DLS,
IDDFS, and UCS. BFS searches level by level, DFS explores a branch
deeply, DLS applies a depth limit, IDDFS repeats depth-limited search,
and UCS selects paths using their total cost.
