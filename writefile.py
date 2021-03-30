def write_csv(package_ID,data):
    Filename = os.path.join("session",str(package_ID),"data")

    with open('{}.csv'.format(Filename),'a',newline='\n') as file:
        writer = csv.writer(file, delimiter=",",quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data)
    pass