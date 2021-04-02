import csv
import os
import numpy as np #import numpy
from tqdm import tqdm
import matplotlib.pyplot as plt

sessionname = "session"

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
    
def create_learning_curve(sessionname,names):
    
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
    plt.plot(main_part[:,19][:,19],main_part[:,19][:,0],label="Nahton")
    plt.plot(main_part[:,0][:,19],main_part[:,0][:,0],label="Commodore")
    
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
    
def extract_learning_curve_data(sessionname):
    
    data = read_csv(sessionname,2) 
    
    header = np.zeros((np.shape(data)[0],10))
    main_part = np.zeros((np.shape(data)[0],22,27))
    
    print("processing data")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        main_part[i] = data[i][10:].reshape(22,-1)
    
    #finding the first valid lap, aka when last lap time is not zero anymore
    x = np.array(np.where(main_part[:,0][:,0] == 0))[0]
    y = np.argmax(x)
    
    start = x[y]+1 #adding one to remove last zero
    #slice accordingly
    header = header[start:]
    main_part = main_part[start:]
           
    return main_part[:,0][:,19]  , main_part[:,0][:,0]
    
def extract_participants(sessionname):
    data = read_csv(sessionname,4)   
    
    print(data)
    
    header = np.empty((np.shape(data)[0],10))
    main_part = np.empty((np.shape(data)[0],22,54),dtype=np.unicode)
    num_cars = np.zeros((np.shape(data)[0],1))
    
    print("processing data")
    for i in tqdm(range(np.shape(data)[0])):
    
        header[i] = data[i][0:10]
        
        num_cars[i] = data[i][10:11]
        
        main_part[i] = data[i][11:].reshape(22,-1)
    
    names = []
    
    for i in range(22):
        tmp = ""
        names.append(tmp.join(main_part[0][i][5:52].tolist()).replace('b','')) #A stupid workaround to remove the encoding error from ÄÖÜ
    return names

def compare_drivers(session1,session2):
    data1_laps,data1 = extract_learning_curve_data(session1)
    data2_laps,data2 = extract_learning_curve_data(session2)
            
    plt.plot(data1_laps,data1,label=session1)
    plt.plot(data2_laps,data2,label=session2)
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    
    names = extract_participants(sessionname)
    print(names)
    
    #compare_drivers("Tele_Nahton","Tele_Sentexi")
    
    create_learning_curve(sessionname,names)
    #data = read_csv(sessionname,packet)
    
    
    