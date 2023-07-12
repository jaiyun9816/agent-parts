from base.parts_model import PartsModel
import dill


class SpringTempModel(PartsModel):
    def __init__(self):
        super().__init__()

    def run_parts(self):
        print(self.agent)


if __name__ == "__main__":
    loader = SpringTempModel()
    with open("./parts/state_check.simx", "wb") as f:
        dill.dump(loader, f)
