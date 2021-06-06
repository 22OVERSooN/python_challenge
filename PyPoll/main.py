import os
import csv

election_csv = os.path.join("Resources","PyPoll_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader,None)

    max_vote = 0
    K_v = []
    C_v = []
    L_v = []
    O_v = []
    for row in csvreader:
        if row[0] is not None:
            max_vote += 1
            if row[2] == "Khan":
                K_v.append(row[2])
            elif row[2] == "Correy":
                C_v.append(row[2])
            elif row[2] == "Li":
                L_v.append(row[2])
            elif row[2] == "O'Tooley":
                O_v.append(row[2])
    lenk = len(K_v)
    lenc = len(C_v)
    lenl = len(L_v)
    leno = len(O_v)
    if lenk>lenc and lenk>lenl and lenk>leno:
        winner = "Khan"
    elif lenc>lenk and lenc>lenl and lenc>leno:
        winner = "Correy"
    elif lenl>lenk and lenl>lenc and lenl>leno:
        winner = "Li"
    elif leno>lenk and leno>lenl and leno>lenc:
        winner = "O'Tooley"

    
    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(max_vote)+"")
    print("------------------------")
    print("Khan: " + "%.3f%%"% (lenk/max_vote*100) + " (" + str(lenk)+ ")")
    print("Correy: " + "%.3f%%"% (lenc/max_vote*100) + " (" + str(lenc)+ ")")
    print("Li: " + "%.3f%%"% (lenl/max_vote*100) + " (" + str(lenl)+ ")")
    print("O'Tooley: " + "%.3f%%"% (leno/max_vote*100) + " (" + str(leno)+ ")")
    print("------------------------")
    print("Winner: " + winner)
    print("------------------------")


    file = open("Analysis/Pypoll.txt","w")
    file.write("Election Results\n")
    file.write("------------------------\n")
    file.write("Total Votes: " + str(max_vote)+"\n")
    file.write("------------------------\n")
    file.write("Khan: " + "%.3f%%"% (lenk/max_vote*100) + " (" + str(lenk)+ ")\n")
    file.write("Correy: " + "%.3f%%"% (lenc/max_vote*100) + " (" + str(lenc)+ ")\n")
    file.write("Li: " + "%.3f%%"% (lenl/max_vote*100) + " (" + str(lenl)+ ")\n")
    file.write("O'Tooley: " + "%.3f%%"% (leno/max_vote*100) + " (" + str(leno)+ ")\n")
    file.write("------------------------\n")
    file.write("Winner: " + winner+"\n")
    file.write("------------------------\n")
    file.close()