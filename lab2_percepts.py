class ClassroomAgent:
    def __init__(self):
        self.pervious_temp = None 
    def act(self, temp, occupied): 
        
        if not occupied: 
            traget_temp = "ECO" 
        
        elif temp > 26: 
             traget_temp = "COOL" 
        
        elif temp < 20: 
            traget_temp = "WARM" 
        
        else: 
            traget_temp = "IDLE"   
        
        if traget_temp != self.pervious_temp:
            send_message = True
        else:
            send_message =  False
        
        old_temp =  self.pervious_temp
        self.pervious_temp = traget_temp
        
        return old_temp, traget_temp, send_message
    

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

    
    
 