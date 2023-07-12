from rx import create
class AgentManagement :
    def __init__(self) :
        self.agent = {}
    
    def set_agent_data(self, name, data) : 
        self.agent[name] = data
        
    def del_agent_data(self, name) :
        del self.agent[name]
                
    def get_source(self) :
        return create(self.object_rx)
    
    def object_rx(self, observer, scheduler) :
        observer.on_next(self.agent)
        observer.on_completed()
        