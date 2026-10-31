Lab 2: Intelligent Agents and PEAS
 student infor
 name: HAdiya NAeem
 
- Course: Artificial Intelligence
- Lab: 02 -- Intelligent Agents and PEAS
1. Introduction
This lab introduces intelligent agents and the PEAS model. An
intelligent agent observes its environment and takes actions to achieve
a goal. PEAS stands for Performance Measure, Environment, Actuators, and
Sensors.
2. Task 1: PEAS Specifications
In this task, prepare PEAS specifications for two systems:
1. Delivery Robot
2. LLM Student Support Agent
For each system, describe all four PEAS parts.
A. Delivery Robot
  PEAS part                           Description
  Performance Measure                 \(How successful and safe the
                                      delivery is measured\)

  Environment                         \(Places and conditions in which
                                      the robot works\)

  Actuators                           \(Parts used by the robot to
                                      perform actions\)
Sensors                             \(Parts used by the robot to
                                      collect information\)
B. LLM Student Support Agent
  PEAS part                           Description
  Performance Measure                 \(How helpful, correct, and useful
                                      its answers are measured\)

  Environment                         \(The setting in which students use
                                      the agent\)

  Actuators                           \(How the agent responds or takes
                                      action\)
Sensors                             \(Information or input the agent
                                      receives\)
Complete the tables with your own descriptions based on the lab task.

Screenshots to add: Insert screenshots of both completed PEAS tables
from your report or document. These should be your own completed tables,
not pictures copied from the lab manual.
3. Task 2: Environment Properties
In this task, classify the environment properties requested in the lab
for the given agent examples. The important properties include:
- Observable / Partially Observable: Whether the agent can see all
  relevant information about the environment.
- Deterministic / Stochastic: Whether an action has a predictable
  result or may have different results.
- Other properties: Use the exact environment-property categories
  and examples given in your lab manual.
Make a table for your answers:

  Agent or example             Property                  Reason
  \(Example 1 from the lab\)   \(Your classification\)   \(Simple reason\)
\(Example 2 from the lab\)   \(Your classification\)   \(Simple reason\)

Use the examples in your lab manual and explain each answer briefly. Do
not add classifications for examples that were not part of your task.

Screenshot to add: Insert a screenshot of your completed
environment-classification answers.
4. Task 3: Stateful Classroom Agent
In this task, design or update a classroom agent so that it remembers
its previous actions and avoids repeating the same command
unnecessarily.

A stateful agent keeps information about what has already happened. This
helps it make better decisions instead of repeating an action without
checking its previous state.

Explain: - What information the agent remembers. - How it checks whether
an action has already been performed. - How it decides what to do
next. - How the state helps prevent repeated commands.

Add the code and output if the task requires implementation.

Screenshots to add: Insert a screenshot of your stateful agent code
and its output.
5. How to Run the Program
1. Open the Lab 2 folder in VS Code.
2. Open the Python file for the stateful classroom agent, if your task
   includes code.
3. Run the file.
4. Check the terminal output.
5. Save screenshots of the code and actual output.
If your PEAS and environment-property tasks are completed in Word, take
clear screenshots of your own completed tables.
6. Suggested Folder Structure
Lab2/
├── lab2_classroom_agent.py
├── README.md
├── Lab2_Report.docx
└── outputs/
    ├── delivery_robot_peas.png
    ├── student_support_agent_peas.png
    ├── environment_properties.png
    └── classroom_agent_output.png
Use the actual names of your files if they are different. If you used
more than one Python file, include all of them.
7. Reflection
In this lab, I learned how to describe an intelligent agent using the
PEAS model. I also learned that an agent's environment can have
different properties. The classroom-agent task helped me understand why
remembering previous actions can prevent unnecessary repeated commands.
8. Responsible Practice
I used clear descriptions for the PEAS model and explained the reasons
for my environment classifications. I checked the classroom agent's
behavior and used screenshots of my own work.
9. Conclusion
This lab helped me understand intelligent agents, the PEAS model,
environment properties, and the use of memory or state in an agent.
