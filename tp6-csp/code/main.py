import backtracking_csp as bc
import forwardChecking_csp as fc
import multiprocessing
import board as Board
import utils
import time
import csv


def runner(queens,results):
    solutionFondBack = 0
    statesBackNum = 0
    statesBack = []
    statesBackProm = 0
    duration_Back = []
    AVG_duration_Back = 0
    std_duration_Back = 0


    solutionFoundFor = 0
    statesForNum = 0
    statesFor = []
    statesForProm = 0
    duration_For = []
    AVG_duration_For = 0
    std_duration_For = 0

    for i in range(30):
        ## Backtracking
        boards = []
        start_time_back = time.time()

        boards,statesBackNum = bc.backtrackingInit(queens,statesBackNum)
        boards = list(set(boards))

        duration_Back.insert(0,time.time() - start_time_back)
        statesBack.insert(0,statesBackNum) 
        AVG_duration_Back += duration_Back[0]
        statesBackProm += statesBackNum
        solutionFondBack += len(boards)
        
        with(open("./tp6-csp/boards.txt", "a")) as file:
            for board in boards:
                file.write(str(board.board) + "\n")
        ## Fin Backtracking

        ## Forward Checking 
        boards = []
        start_time_for = time.time()

        boards,statesForNum = fc.forwardCheckingInit(queens,statesForNum)
        boards = list(set(boards))
        
        duration_For.insert(0,time.time() - start_time_for)
        statesFor.insert(0,statesForNum)
        AVG_duration_For += duration_For[0]
        statesForProm += statesForNum
        solutionFoundFor += len(boards)

        with(open("./tp6-csp/boards.txt", "a")) as file:
            for board in boards:
                file.write(str(board.board) + "\n")
        ## Fin Forward Checking 

    print("Finished " + str(queens) + " Queens")
    std_duration_Back = utils.standDev(duration_Back,AVG_duration_Back)
    std_duration_For = utils.standDev(duration_For,AVG_duration_For)
    stdStatesBack = utils.standDev(statesBack,statesBackProm/30)
    stdStatesFor = utils.standDev(statesFor,statesForProm/30)
    results.append({"Tamaño": queens,"Algortimo":"Backtracking","Sol Found": solutionFondBack ,"AVG Time":AVG_duration_Back/30, "STD Time": std_duration_Back,"AVG States":statesBackProm/30,"STD States": stdStatesBack})
    results.append({"Tamaño": queens,"Algortimo":"Forward Checking","Sol Found": solutionFoundFor ,"AVG Time":AVG_duration_For/30, "STD Time": std_duration_For,"AVG States":statesForProm/30,"STD States": stdStatesFor})
    utils.save_to_csv(results)
    if queens == 12:
        utils.plotTimes(duration_Back,duration_For,queens)
    


if __name__ == '__main__':
    start_time_General = time.time()
    results = []
    queens = [4,8,10,12]
    # runner(12,results)

    with multiprocessing.Pool(4) as pool:
        # Utiliza starmap para ejecutar la función con los argumentos
        pool.starmap(runner, [(queen,results) for queen in queens])
    
    print(time.time() - start_time_General)
    
    

