from env_rl import EnvRL

def main():
    print("Hello Gorgeous!")

    env = EnvRL(n_nodes=5, seed=1234)
    print(env.get_current_node_features())
    print(env.get_seed())
    print(env.get_sim_name())
    print(env.get_instance_name())

if __name__ == "__main__":
    main()
