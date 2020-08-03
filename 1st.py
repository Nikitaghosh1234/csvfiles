import csv,json
jsonFilePath="happy.json"
# Read the data from csv
# data={}
with open('20200617_analytics_v2.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    csv_headings = next(csv_reader)
    first_line = next(csv_reader)
    second_line=next(csv_reader)
   
    print(csv_headings[4])
    print(first_line[2])
    print(second_line[0])

    # for row in csv_reader:
    #     # AAAU=row["AAAU"]
    #     # data[AAAU]=row
    #     print(row['AAAU'])

# wtire data to Json file

# with open(jsonFilePath,"w") as jsonFile:
#     jsonFile.write(json.dumps(data,indent=4))
