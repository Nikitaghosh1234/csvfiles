import csv,json
jsonFilePath="happy.json"
# Read the data from csv
data={}
with open('20200617_analytics_v2.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for csvRow in csv_reader:
        AAAU=csvRow["AAAU"]
        data[AAAU]=csvRow

# wtire data to Json file

with open(jsonFilePath,"w") as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))