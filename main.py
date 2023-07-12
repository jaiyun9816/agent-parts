from base.execution_engine import ExecutionEngine
from human import Human
from field import Field

from multiprocessing import Pool
from rx import create

if __name__ == "__main__":
    agent_list = []
    env_list = []

    agent_list.append(["jaiyun", Human("jaiyun", 36.7, "arctic clothes")])
    agent_list.append(["seyoung", Human("seyoung", 36.9, "t-shirt")])

    env_list.append(["spring", Field("spring", 20)])
    env_list.append(["summer", Field("summer", 30)])
    env_list.append(["fall", Field("fall", 15)])
    env_list.append(["winter", Field("winter", 0)])

    """
    for i in range(5):
        engine.append(ExecutionEngine(5))
        for ag in agent_list:
            engine[i].append_agent_source(ag[0], ag[1].get_source())
        for env in env_list:
            engine[i].append_env_source(env[0], env[1].get_source)
            
    """
    engine = ExecutionEngine(5)

    engine.append_bootloader("spring", "./bootloader/spring.simx")

    engine.state = "spring"
    for ag in agent_list:
        engine.append_agent_source(ag[0], ag[1].get_source())
    for env in env_list:
        engine.append_env_source(env[0], env[1].get_source())

    engine.run_boot_loader()
    engine.run_multi_parts()
