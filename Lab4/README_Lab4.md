Lab 4: Informed Search -- Heuristics and A*
Student Information
- Name: \(Write your name\)
- Registration Number: \(Write your registration number\)
- Course: Artificial Intelligence
- Lab: 04 -- Informed Search: Heuristics and A*
1. Introduction
This lab explains informed search using heuristics and the A* search
algorithm. It also compares A* with Uniform Cost Search (UCS). The main
purpose is to find a path from the start node to the goal node with the
lowest cost.
2. Graph Used in This Lab
The graph contains five nodes: S, A, B, C, and G.
S --1--> A --2--> C --3--> G
 \                         
  \--4--> B --5----------> G
The edge costs are: - S to A = 1 - S to B = 4 - A to C = 2 - B to G =
5 - C to G = 3

The start node is S, and the goal node is G.

The heuristic values are:

  Node     Heuristic h(n)
  S                     5
A                     4
B                     4
C                     2
G                     0
3. Task 1: Manual A* Calculations
A* uses the following formula:

f(n) = g(n) + h(n)
- g(n): Actual cost from the start node to the current node.
- h(n): Estimated cost from the current node to the goal.
- f(n): Total estimated cost.
The first three nodes selected for processing are S, A, and C.

  Node     g(n)   h(n)   f(n)
  S           0      5      5
A           1      4      5
C           3      2      5
Frontier after each expansion
  After processing   Frontier entries (node, g, h, f)
  S                  A (1, 4, 5), B (4, 4, 8)
A                  C (3, 2, 5), B (4, 4, 8)
C                  G (6, 0, 6), B (4, 4, 8)

The next selected node is G because its f-value is 6, which is smaller
than B's f-value of 8.

Screenshot to add: Insert a screenshot of your manual calculation
and frontier tables here.
4. Task 2: A* Search and UCS Comparison
The program runs A* and UCS on the same graph.
A* Search
A* calculates priority using:

f(n) = g(n) + h(n)

Expected result: - Path: S → A → C → G - Total cost: 6 - Processed
order: S, A, C, G - Expanded nodes: 3 (S, A, C; the goal is not counted
as expanded)
Uniform Cost Search (UCS)
UCS uses a heuristic value of zero for every node. Therefore, its
priority is based only on the actual path cost.

Expected result: - Path: S → A → C → G - Total cost: 6 - Processed
order: S, A, C, B, G - Expanded nodes: 4 (S, A, C, B; the goal is not
counted as expanded)
Comparison
  Measure           A*             UCS
  Path              S → A → C → G   S → A → C → G
Total cost        6               6
Processed order   S, A, C, G      S, A, C, B, G
Expanded nodes    3               4

Screenshot to add: Insert screenshots of your A* and UCS code and
their outputs here.
5. Task 3: Heuristic Audit and Overestimation
A heuristic is admissible when it does not overestimate the actual
minimum remaining cost to the goal.

The actual remaining costs are:

  Node     Actual remaining cost   Given heuristic Admissible?
  S                            6                 5 Yes
A                            5                 4 Yes
B                            5                 4 Yes
C                            3                 2 Yes
G                            0                 0 Yes

The given heuristic values do not overestimate the actual remaining
costs.
Overestimation experiment
In this experiment, only the heuristic value of C is changed from 2 to
10. All other heuristic values and graph costs stay the same.

The new heuristic is not admissible because the actual remaining cost
from C to G is 3, but the heuristic value is 10.

Expected result with this changed heuristic: - A* path: S → B → G -
Total cost: 9

This experiment shows that an overestimated heuristic can cause A* to
select a more expensive path. An inadmissible heuristic removes the
usual guarantee that A* will find an optimal path.

Screenshot to add: Insert the output screenshot of the
overestimation experiment here.
6. How to Run the Program
1. Install Python on your computer.
2. Open the Lab 4 folder in VS Code or another Python editor.
3. Open the Python file, for example lab4_astar_audit.py.
4. Run the file.
5. Check the terminal for A* and UCS paths, costs, and processed
   nodes.
6. Save screenshots of the code and output for your report.
The heapq module is included with Python, so it does not need a
separate installation.
7. Suggested Folder Structure
Lab4/
│
├── lab4_astar_audit.py
├── README.md
├── Lab4_Report.docx
│
└── outputs/
    ├── manual_calculations.png
    ├── astar_output.png
    ├── ucs_output.png
    ├── heuristic_audit.png
    └── overestimate_output.png
Use the actual names of your files if they are different. Add your own
screenshots to the outputs folder.
8. Failure or Edge-Case Analysis
One useful edge case is when the goal node cannot be reached from the
start node. In that situation, the search should finish without finding
a path and report that no path is available. If you include this
experiment in your report, run it with a modified graph and add your
actual output screenshot.
9. Reflection
In this lab, I learned how A* uses both actual cost and heuristic
values to select the next node. I also learned that UCS uses only the
actual path cost. Both algorithms found the lowest-cost path in the
given graph. The overestimation experiment helped me understand why a
good heuristic is important.
10. Responsible Practice
I used the same graph and edge costs for the A* and UCS comparison. I
checked the path costs and included the program output in the report. I
also explained the change made in the overestimation experiment.
11. Conclusion
A* and UCS both found the path S → A → C → G with a total cost of 6.
A* processed fewer nodes than UCS in this example because it used
heuristic information. The overestimation experiment showed that an
unsuitable heuristic can lead A* to a more expensive path
