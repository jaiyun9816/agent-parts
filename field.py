from base.environment_manage import EnvironmentManagement


class Field(EnvironmentManagement):
    def __init__(self, name, temp):
        super().__init__()
        self.field = {"name": name, "temperature": temp}
