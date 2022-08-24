import csv, json, os

# CSV (comma seperated value)

os.chdir(os.path.dirname(__file__))
file = open('example.csv')
reader = csv.reader(file)
data = list(reader)
print(data)
print(data[0][1])
file.close()

file = open('example.csv')  # can be traversed only once
reader = csv.reader(file)
for row in reader:
    print('row ' + str(reader.line_num) + ' ' + str(row))
file.close()

outputfile = open('output.csv', 'w', newline='')
writer = csv.writer(outputfile)
#   delimeter='\t',lineterminator='\n\n' in .tsv file
writer.writerow(['hello, world', 'spam', 'eggs'])
writer.writerow(['bacon', 4, 'ham'])
outputfile.close()

# JSON (javascript object notation)

jsonstr = '{"name" : "shri", "ishuman" : true, "certificates" : 0}'
pyvalue = json.loads(jsonstr)
print(pyvalue)
jsonvalue = json.dumps(pyvalue)
print(jsonvalue)