from abc import abstractmethod

class ExecutionEngine :
    def __init__(self) :
        self.state = "IDLE"
        self.environment = {}
        self.agent = {}
        self.parts = {}

    def append_agent_source(self, name, source) :
        self.agent[name] = source
        pass
    
    def append_environment_source(self, name, source) :
        self.environment[name] = source
        pass    
        
    #parts list clear
    def clear_parts(self) :
        self.parts = []

    #parts run
    def run_parts(self) :
        for parts in self.parts :
            parts.run_parts()
    
    @abstractmethod
    def set_parts(self) :
        pass
    
    @abstractmethod  
    def update_kernel_obj(self) :
        self.kernel_obj.set_kernel_obj()
        
