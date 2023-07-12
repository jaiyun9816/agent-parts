from base.bootloader import BootLoader
import dill


class SpringLoader(BootLoader):
    def __init__(self):
        super().__init__()
        self.state = "SPRING"
        self.parts = ["spring_temp.simx", "state_check.simx"]


if __name__ == "__main__":
    loader = SpringLoader()
    with open("./bootloader/spring.simx", "wb") as f:
        dill.dump(loader, f)
