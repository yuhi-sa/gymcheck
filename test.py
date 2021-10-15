from src.check_env import check_env

MAX_TIME = 2000
ENVIRONMENTS = [
    {"env_name":"CartPole","env_id": "CartPoleContinuousBulletEnv-v0"},
    {"env_name":"InvertedPendulum", "env_id": "InvertedPendulumBulletEnv-v0"},
    {"env_name":"Swingup", "env_id": "InvertedPendulumSwingupBulletEnv-v0"},
    {"env_name":"DoublePendulum","env_id": "InvertedDoublePendulumBulletEnv-v0"},
    ]

def main():
    for environment in ENVIRONMENTS:
        # 略称
        name = environment["env_name"]
        # 環境ID
        ENV_ID = environment["env_id"]
        # 環境情報を表示
        check_env(name, ENV_ID)
    
if __name__ == "__main__":
    main()
