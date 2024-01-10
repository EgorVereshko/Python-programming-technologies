import cProfile
from pstats import Stats
from functions_to_profile import load_files, read_database, get_id, get_user_data, generate_words


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    load_files()
    read_database()
    get_id()
    get_user_data()
    generate_words()

    profiler.disable()
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('tottime')
    stats.print_stats()

    for func in [load_files, read_database, get_id, get_user_data, generate_words]:
        func_name = func.__name__
        print(f"{stats.stats[func_name][3]:.4f}: {stats.stats[func_name][2]:.0%}")
