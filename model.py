#  statefull of classroom agent
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