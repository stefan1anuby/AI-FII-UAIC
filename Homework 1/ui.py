import threading
from datetime import datetime
from main import Board, iddfs, greedy_search, manhattan_distance, hamming_distance

def iddfs_thread(puzzle, depth):
    initial_state = puzzle.state
    start_time = datetime.now()
    found, solution, iterations = iddfs(puzzle, depth)
    end_time = datetime.now() - start_time
    
    if found:
        # print(f"\nFound solution using iddfs for {str(initial_state)} in: {end_time} | {iterations} iterations")
        print(f"\niddfs: Found in: {end_time} | {iterations} iterations for {str(initial_state)}")
    else:
        print(f"\niddfs: Not found in {end_time} | {iterations} iterations for {str(initial_state)}")
    # print(datetime.now() - start_time)
    
def greedy_thread(puzzle, heuristic_function):
    initial_state = puzzle.state
    start_time = datetime.now()
    found, solution, iterations = greedy_search(puzzle, heuristic_function)
    end_time = datetime.now() - start_time
    
    if found:
        # print(f"\nFound solution using {heuristic_function.__name__} for {str(initial_state)} in: {end_time} | {iterations} iterations")
        print(f"\n{heuristic_function.__name__}: Found in: {end_time} | {iterations} iterations for {str(initial_state)}")
    else:
        print(f"\n{heuristic_function.__name__}: Not found in: {end_time} | {iterations} iterations for {str(initial_state)}")


def run_iddfs():
    t1 = threading.Thread(target=iddfs_thread, args=(Board([[8, 6, 7], [2, 5, 4], [0, 3, 1]]), 100))
    t2 = threading.Thread(target=iddfs_thread, args=(Board([[2, 5, 3], [1, 0, 6], [4, 7, 8]]), 100))
    t3 = threading.Thread(target=iddfs_thread, args=(Board([[2, 7, 5], [0, 8, 4], [3, 1, 6]]), 100))
    
    t1.start()
    t2.start()
    t3.start()
    
    # t1.join()
    # t2.join()
    # t3.join()
    
def run_greedy(heuristic_function):
    t1 = threading.Thread(target=greedy_thread, args=(Board([[8, 6, 7], [2, 5, 4], [0, 3, 1]]), heuristic_function))
    t2 = threading.Thread(target=greedy_thread, args=(Board([[2, 5, 3], [1, 0, 6], [4, 7, 8]]), heuristic_function))
    t3 = threading.Thread(target=greedy_thread, args=(Board([[2, 7, 5], [0, 8, 4], [3, 1, 6]]), heuristic_function))
    
    t1.start()
    t2.start()
    t3.start()
    
    # t1.join()
    # t2.join()
    # t3.join()

def run_all():
    run_iddfs()
    run_greedy(hamming_distance)
    run_greedy(manhattan_distance)

def selection(selection):
    match selection:
        case 1: run_iddfs()
        case 2: run_greedy(hamming_distance)
        case 3: run_greedy(manhattan_distance)
        case 5: run_all()
        case _: print(f"Invalid selection")

def main():
    print("1: Run iddfs")
    print("2: Run Greedy using Hamming Distance")
    print("3: Run Greedy using Manhattan Distance")
    print("5: Run all")
    
    selection(int(input()))
    

if __name__ == "__main__":
    main()