from abc import abstractmethod


class PartsModel:
    def __init__(self):
        self.agent = {}
        # agent 명 : sbuscribe 받은 agent data(dictionary)
        self.environment = {}
        # environment 명 : subscribe 받은 environment data(dictionary)

    def clear_data(self):
        # data reset
        self.agent = {}
        self.environment = {}

    def set_agent(self, name, source):
        def set_rx(obj):  # agent data 구독
            self.agent[name] = obj

        source.subscribe(set_rx)

    def set_environment(self, name, source):
        def set_rx(obj):  # environment data 구독
            self.environment[name] = obj

        source.subscribe(set_rx)

    def serial_agent(self, agent_name, set_list):
        pass

    def serial_environment(self, environment_name, name_list):
        pass

    @abstractmethod
    def run_parts(self):
        pass
