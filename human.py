from base.agent_manage import AgentManagement


class Human(AgentManagement):
    def __init__(self, name, temp, cloth):
        super().__init__()
        self.agent = {"name": name, "temperature": temp, "clothes": cloth}
