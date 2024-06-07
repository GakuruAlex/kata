from memory_profiler import profile
@profile
def tower_builder(n_floors):
    width = (2 * n_floors) - 1
    tower = []
    for i in range(n_floors):
        mul = 2 * i + 1
        tower.append(f"{'*' * mul}".center(width))
    return tower

@profile
def build_tower(n_floors):
    return [f"{'*'*(2 * i + 1)}".center(2 * n_floors -1) for i in range(n_floors)] 

if __name__ == "__main__":
    build_tower(1000)
    tower_builder(1000)