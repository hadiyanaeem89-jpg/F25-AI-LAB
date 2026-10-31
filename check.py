# testing the classroom agent 
from model import ClassroomAgent

agent = ClassroomAgent() 

percept = [
    (29, True), 
    (24, True), 
    (29, False),
    (19,True),
    (30, True)
    ] 

for step, (temp , occupied) in enumerate(percept,1):
    pervious, traget , message = agent.act (temp, occupied)
    
print("step", step)
print("pervious_temp", pervious)
print("temperature", temp)
print("occuiped", occupied)
print("traget_temp", traget)
print("send_message", message ) 
print("---------------")    