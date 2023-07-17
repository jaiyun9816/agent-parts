from base.parts_model import PartsModel
import dill
import time

class SpringTempModel(PartsModel):
    def __init__(self):
        super().__init__()

    def run_parts(self):
        time.sleep(0.5)
        self.agent['temperature'] += 0.1
        self.agent['temperature'] = round(self.agent['temperature'], 3)
        print("tempe", self.agent)
        print("env test", self.environment)
        print("")


if __name__ == "__main__":
    loader = SpringTempModel()
    with open("./parts/spring_temp.simx", "wb") as f:
        dill.dump(loader, f)
