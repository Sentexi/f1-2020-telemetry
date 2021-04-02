import csv
import os

def write_csv(package_ID,data,sessionname):
    Filename = os.path.join(sessionname,str(package_ID),"data")

    with open('{}.csv'.format(Filename),'a',newline='\n',encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=",",quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)
    pass
