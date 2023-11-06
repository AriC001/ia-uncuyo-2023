import backtracking_csp as bc
import forwardChecking_csp as fc
import multiprocessing
import board as Board
import time
import csv


def runner(queens,results):
    # solutionFondBack = 0
    # statesBack = []
    # statesBackProm = 0
    # duration_Back = []
    # AVG_duration_Back = 0
    # std_duration_Back = 0

    # boards = []
    # start_time_back = time.time()
    # boards = bc.makeBoardOne(queens)
    # duration_Back.insert(0,time.time() - start_time_back)
    # AVG_duration_Back += duration_Back[0]

    # if boards[0].value == 0:
    #     solutionFondBack = True
    # results.append([str(queens), "Backtracking", str(AVG_duration_Back), str("board.std_time")])

    solutionFoundFor = 0
    statesFor = []
    statesForProm = 0
    duration_For = []
    AVG_duration_For = 0
    std_duration_For = 0

    boards = []
    start_time_for = time.time()
    boards = fc.makeBoardOne(queens)
    duration_For.insert(0,time.time() - start_time_for)
    AVG_duration_For += duration_For[0]
    with(open("boards.txt", "w")) as file:
        for board in boards:
            file.write(str(board.board) + "\n")

    results.append({"Tamaño":str(queens),"Algortimo":"Forward Checking","Sol Found":str(len(boards)) ,"AVG Time":str(AVG_duration_For), "STD Time":str("board.std_time")}) 
    return results

def resltsCSV(results):
    with open('results.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        # Check if file is empty and write headers
        if archivo.tell() == 0:
            writer.writerow(["Tamaño", "Algortimo","Sol Found" ,"AVG Time", "STD Time"])
        # Write data
        for result in results:
            writer.writerow(result)
        # for board in boards:
            # writer.writerow([str(queens), str(board.algorithm), str(AVG_duration_Back), str("board.std_time")]) 

if __name__ == '__main__':
    start_time_General = time.time()
    results = []
    queens = [4,8,10,12]
    runner(8,results)
    # position = queens - 1
    
    # available_states = list(range(1, queens + 1))  # Inicializa con todos los estados posibles

    # with multiprocessing.Pool(5) as pool:
    #     # Utiliza starmap para ejecutar la función con los argumentos
    #     pool.starmap(runner, [(queen,results) for queen in queens])
    
    resltsCSV(results)
    

    print(time.time() - start_time_General)

