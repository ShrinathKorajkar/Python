import csv, os

os.chdir(os.path.dirname(__file__))
with open("trainingexamples.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)
    specific = data[0][:-1]
    general = [['?' for i in range(len(specific))]
               for j in range(len(specific))]

    for i in data:
        if i[-1] == "Yes":
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    specific[j] = "?"
                    general[j][j] = "?"
        elif i[-1] == "No":
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = "?"
        print("\nStep " + str(data.index(i) + 1) +
              " of Candidate Elimination Algorithm")
        print(specific)
        print(general)

    mostGeneic = ['?' for i in range(len(specific))]
    while (mostGeneic in general):
        general.remove(mostGeneic)

    print("\nFinal Specific hypothesis:\n", specific)
    print("\nFinal General hypothesis:\n", general)
