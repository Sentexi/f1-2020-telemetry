import csv
import os
import numpy as np #import numpy
from tqdm import tqdm
import matplotlib.pyplot as plt

sessionname = "TW2_UK_Medium"

def read_csv(sessionname,packet):
    Filename = generate_path(sessionname,packet)
    rows = []
    
    with open('{}.csv'.format(Filename),'r') as csv_file:
        lines = len(csv_file.readlines())
    
    print("Reading file")
    if os.path.isfile('{}.csv'.format(Filename)):
        with open('{}.csv'.format(Filename),encoding="utf8") as file:
             reader = csv.reader(file, delimiter=',')
             for row in tqdm(reader, total=lines):
                 rows.append(row)
    else:
        print("File does not exist")
        
    return np.array(rows)

def generate_path(sessionname,packet):
    return os.path.join(sessionname,str(packet),"data")

def analyze_trial_run(sessionname):
 
    data = read_csv(sessionname,6)  
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,30))
    appendix = np.zeros((np.shape(data)[0],4))
    
    print("processing data")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
         
        main_part[i] = data[i][10:-4].reshape(22,-1)
        
        appendix[i] = data[i][-4:]
    
    #Example: plot speed vs session time
    plt.plot(header[:,6],main_part[:,0][:,0])
    plt.show()
    
def create_learning_curve(sessionname,names,num_driver):
    
    data = read_csv(sessionname,2) 
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,27))
    
    print("processing data")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        main_part[i] = data[i][10:].reshape(22,-1)
    
    #finding the first valid lap, aka when last lap time is not zero anymore
    x = np.array(np.where(main_part[:,19][:,0] == 0))[0]
    y = np.argmax(x)
    
    start = x[y]+1 #adding one to remove last zero
    #slice accordingly
    #header = header[start:]
    #main_part = main_part[start:]
           
    #Example: plot lap time vs lap num
    plt.plot(main_part[:,num_driver][:,19],main_part[:,num_driver][:,0],label=names[num_driver])
    
    '''
    laps = main_part[:,17][:,19]
    num_laps = laps[-1]
    print(num_laps)
    exp_const = np.shape(main_part)[0] / num_laps
    main_part1 = main_part[int(exp_const*2.5):int(exp_const*12)]
    main_part2 = main_part[int(exp_const*12):]
    
    
    #Tyre wear analysis
    plt.plot(main_part1[:,17][:,19],main_part1[:,17][:,0],label="90kg")
    plt.plot(main_part2[:,17][:,19]-11,main_part2[:,17][:,0],label="45kg")
    '''
    
    #Example: plot lap time vs lap nr
    #for i in range(np.shape(names)[0]):
    #    plt.plot(main_part[:,i][:,19],main_part[:,i][:,0],label=names[i])
    plt.legend()
    plt.show()
    
def compare_many_drivers(sessionname,names,num_driver):
    
    data = read_csv(sessionname,2) 
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,27))
    
    print("processing data")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        main_part[i] = data[i][10:].reshape(22,-1)
    
    #finding the first valid lap, aka when last lap time is not zero anymore
    x = np.array(np.where(main_part[:,19][:,0] == 0))[0]
    y = np.argmax(x)
    
    start = x[y]+1 #adding one to remove last zero
    #slice accordingly
    #header = header[start:]
    #main_part = main_part[start:]
           
    #Example: plot lap time vs lap num
    for i in range(len(num_driver)):
        plt.plot(main_part[:,num_driver[i]][:,19],main_part[:,num_driver[i]][:,0],label=names[num_driver[i]])
    
    '''
    laps = main_part[:,17][:,19]
    num_laps = laps[-1]
    print(num_laps)
    exp_const = np.shape(main_part)[0] / num_laps
    main_part1 = main_part[int(exp_const*2.5):int(exp_const*12)]
    main_part2 = main_part[int(exp_const*12):]
    
    
    #Tyre wear analysis
    plt.plot(main_part1[:,17][:,19],main_part1[:,17][:,0],label="90kg")
    plt.plot(main_part2[:,17][:,19]-11,main_part2[:,17][:,0],label="45kg")
    '''
    
    #Example: plot lap time vs lap nr
    #for i in range(np.shape(names)[0]):
    #    plt.plot(main_part[:,i][:,19],main_part[:,i][:,0],label=names[i])
    plt.legend()
    plt.show()
    
    
def list_directories():
    dirs = []
    for file in os.listdir(os.path.join(".")):
        if os.path.isdir(file) and file != ".git" and file != "__pycache__":
            dirs.append(file)
            
    return dirs
    
    
def show_menu(names):
    for i in range(len(names)):
        print("{}.: {}".format(i,names[i]))
    pass

    
def extract_lapdata(sessionname):
    
    data = read_csv(sessionname,2) 
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,27))
    
    print("processing lapdata")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        main_part[i] = data[i][10:].reshape(22,-1)
               
    return header , main_part 
    
def extract_tyredata(sessionname):
    
    data = read_csv(sessionname,7) 
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,36))
    
    print("processing lapdata")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        main_part[i] = data[i][10:].reshape(22,-1)
           
    return header , main_part 

    
def extract_learning_curve_data(sessionname,num_driver):
    
    data = read_csv(sessionname,2) 
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,27))
    
    print("processing data")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        main_part[i] = data[i][10:].reshape(22,-1)
    
    #finding the first valid lap, aka when last lap time is not zero anymore
    x = np.array(np.where(main_part[:,num_driver][:,0] == 0))[0]
    y = np.argmax(x)
    
    start = x[y]+1 #adding one to remove last zero
    #slice accordingly
    header = header[start:]
    main_part = main_part[start:]
           
    return main_part[:,num_driver][:,19]  , main_part[:,num_driver][:,0]
    
def extract_participants(sessionname):
    data = read_csv(sessionname,4)   
        
    header = np.empty((np.shape(data)[0],10))
    main_part = np.empty((np.shape(data)[0],22,54),dtype=np.unicode)
    num_cars = np.zeros((np.shape(data)[0],1))
    
    print("processing names")
    for i in range(np.shape(data)[0]):
    
        header[i] = data[i][0:10]
        
        num_cars[i] = data[i][10:11]
        
        main_part[i] = data[i][11:].reshape(22,-1)
    
    names = []
    
    for i in range(22):
        tmp = ""
        names.append(tmp.join(main_part[0][i][5:52].tolist()).replace('b','')) #A stupid workaround to remove the encoding error from ??????
    return names

def compare_drivers(session1,session2,num_driver1,num_driver2):
    data1_laps,data1 = extract_learning_curve_data(session1,num_driver1)
    data2_laps,data2 = extract_learning_curve_data(session2,num_driver2)
            
    plt.plot(data1_laps,data1,label=session1)
    plt.plot(data2_laps,data2,label=session2)
    plt.legend()
    plt.show()
    
def create_tyre_wear_curve(sessionname,num_driver,graphics):
    header1, lapdata = extract_lapdata(sessionname)
    header2 ,tyredata = extract_tyredata(sessionname)
    
    if np.shape(lapdata)[0] < np.shape(tyredata)[0]:
        tyredata = tyredata[:np.shape(lapdata)[0]]
    else:
        lapdata = lapdata[:np.shape(tyredata)[0]]
    
    if graphics:
        plt.plot(tyredata[:,num_driver][:,13],lapdata[:,num_driver][:,0],label=names[num_driver])
        
        plt.xlabel("tyre wear in percent")
        plt.ylabel("lap time in s")
        
        plt.legend()
        plt.show()
        
        plt.plot(lapdata[:,num_driver][:,19],tyredata[:,num_driver][:,13],label=names[num_driver])
        
        plt.xlabel("lap Nr.")
        plt.ylabel("tyre wear in percent")
        
        plt.legend()
        plt.show()
    
    return tyredata,lapdata
    
def create_tyre_wear_analysis(soft_session,medium_session,hard_session,num_driver1,num_driver2,num_driver3):
    tyredata1,lapdata1 = create_tyre_wear_curve(soft_session,num_driver1,False)
    tyredata2,lapdata2 = create_tyre_wear_curve(medium_session,num_driver2,False)
    tyredata3,lapdata3 = create_tyre_wear_curve(hard_session,num_driver3,False)
    
    plt.plot(tyredata1[:,num_driver1][:,13],lapdata1[:,num_driver1][:,0],label="Soft")
    plt.plot(tyredata2[:,num_driver2][:,13],lapdata2[:,num_driver2][:,0],label="Medium")
    plt.plot(tyredata3[:,num_driver3][:,13],lapdata3[:,num_driver3][:,0],label="Hard")
    
    plt.xlabel("tyre wear in percent")
    plt.ylabel("lap time in s")
    
    plt.legend()
    plt.show()    
    
    plt.plot(lapdata1[:,num_driver1][:,19],lapdata1[:,num_driver1][:,0],label="Soft")
    plt.plot(lapdata2[:,num_driver2][:,19],lapdata2[:,num_driver2][:,0],label="Medium")
    plt.plot(lapdata3[:,num_driver3][:,19],lapdata3[:,num_driver3][:,0],label="Hard")
    
    plt.xlabel("lap Nr.")
    plt.ylabel("lap time in s")
    
    plt.legend()
    plt.show()
    
    plt.plot(lapdata1[:,num_driver1][:,19],tyredata1[:,num_driver1][:,13],label="Soft")
    plt.plot(lapdata2[:,num_driver2][:,19],tyredata2[:,num_driver2][:,13],label="Medium")
    plt.plot(lapdata3[:,num_driver3][:,19],tyredata3[:,num_driver3][:,13],label="Hard")
    
    plt.xlabel("lap Nr.")
    plt.ylabel("tyre wear in percent")
    
    plt.legend()
    plt.show()
    pass
    
def create_race_results(sessionname,names):
    def s_to_min(seconds):
        minutes = int(seconds / 60)
        seconds = round(((seconds / 60) - int(seconds / 60))*60,3)
        laptime_string = "{}:{}".format(minutes,seconds)
        return laptime_string
        
    def create_status(statuscode):
        if statuscode == 0:
            status = "INVALID"
        if statuscode == 1:
            status = "INACTIVE"
        if statuscode == 2:
            status = "ACTIVE"
        if statuscode == 3:
            status = "FIN"
        if statuscode == 4:
            status = "DSQ"
        if statuscode == 5:
            status = "NOT CLASSIFIED"
        if statuscode == 6:
            status = "DNF"
        return status
        

    data = read_csv(sessionname,8)   
        
    header = np.empty((np.shape(data)[0],10))
    main_part = np.empty((np.shape(data)[0],22,27))
    num_cars = np.zeros((np.shape(data)[0],1))
    
    print("processing names")
    for i in range(np.shape(data)[0]):
    
        header[i] = data[i][0:10]
        
        num_cars[i] = data[i][10:11]
        
        main_part[i] = data[i][11:].reshape(22,-1)    
        
    #for i in range(len(names)):
    print(main_part[-1][:,0])
    print(np.argsort(main_part[-1][:,0]))
    for i in np.argsort(main_part[-1][:,0]).astype("int"):
        if int(main_part[-1][i][0]) != 0:
            print("{} \n Pos: {}. \t Grid: {} \t Best Lap: {} \t Penalties: {} \t Pit Stops: {} \t Status: {}".format(names[i], \
            int(main_part[-1][i][0]),int(main_part[-1][i][2]), \
            s_to_min(main_part[-1][i][6]),int(main_part[-1][i][8]),int(main_part[-1][i][4]), create_status(main_part[-1][i][5])))

    pass
    
def analyse_assists(sessionname,names):
   header , main_part = extract_tyredata(sessionname)
   pos = int(np.shape(main_part)[0]/2)
   for i in range(len(names)):
        print("{} \n Traction Control: {} \t ABS: {} \t".format(names[i],main_part[pos][i][0],main_part[pos][i][1]))
   
   pass
        
if __name__ == "__main__":


    dirs = list_directories()     
    
    print("1. analyse one driver")
    print("2. analyse many drivers")
    print("3. Analyse tyre wear (one set only) ")
    print("4. Create tyre wear analysis")
    print("5. Compare two individual drivers")
    print("6. race summary")
    print("7. Analyse assists")
    
    program_val = int(input("Choose program"))
    
    
    #names = extract_participants(sessionname)
            
    
    if program_val == 1:    
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for first session"))    
    
        names = extract_participants(dirs[num_dir1])
        show_menu(names)
        num_driver = int(input("Which driver do you want to analyze?"))
        create_learning_curve(dirs[num_dir1],names,num_driver)
    if program_val == 2:
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for first session"))    
      
        names = extract_participants(dirs[num_dir1])      
        show_menu(names)
        num = int(input("How many drivers do you want to analyse"))
        num_driver = []
        for i in range(num):
            val = input("Choose driver {}\n".format(i+1))
            num_driver.append(int(val))
            print(num_driver)
        compare_many_drivers(dirs[num_dir1],names,num_driver)
    if program_val == 3:
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for first session"))          

        names = extract_participants(dirs[num_dir1])    
        show_menu(names)
        num_driver = int(input("Which driver do you want to analyze?"))
        create_tyre_wear_curve(dirs[num_dir1],num_driver,True)
    if program_val == 4:
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for soft tyres"))
        
        names = extract_participants(dirs[num_dir1])
        show_menu(names)
        num_driver1 = int(input("Which driver do you want to analyze?"))
        
        show_menu(dirs)
        num_dir2 = int(input("Choose directory for medium tyres"))
        
        names = extract_participants(dirs[num_dir2])
        show_menu(names)
        num_driver2 = int(input("Which driver do you want to analyze?"))
        
        show_menu(dirs)
        num_dir3 = int(input("Choose directory for hard tyres"))
        
        names = extract_participants(dirs[num_dir3])
        show_menu(names)
        num_driver3 = int(input("Which driver do you want to analyze?"))
        
        create_tyre_wear_analysis(dirs[num_dir1],dirs[num_dir2],dirs[num_dir3],num_driver1,num_driver2,num_driver3)
        
        
    if program_val == 5:
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for first session"))
        
        names = extract_participants(dirs[num_dir1])
        show_menu(names)
        num_driver1 = int(input("Which driver do you want to analyze?"))

        show_menu(dirs)
        num_dir2 = int(input("Choose directory for second session"))
        
        names = extract_participants(dirs[num_dir2])
        show_menu(names)
        num_driver2 = int(input("Which driver do you want to analyze?"))        
        
        compare_drivers(dirs[num_dir1],dirs[num_dir2],num_driver1,num_driver2)
        
    if program_val == 6:
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for race results"))        

        names = extract_participants(dirs[num_dir1])
        
        create_race_results(dirs[num_dir1],names)
        
    if program_val == 7:
        show_menu(dirs)
        num_dir1 = int(input("Choose directory for assist analysis"))        

        names = extract_participants(dirs[num_dir1])
        
        analyse_assists(dirs[num_dir1],names)
        
    
    #compare_drivers("Tele_Nahton","Tele_Sentexi")
    
    #data = read_csv(sessionname,packet)
    
    
    