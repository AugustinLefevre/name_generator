import csv

excluded_file = "ressources/excluded_words.csv"

excluded = []

with open(excluded_file, mode="r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        if(row["excluded"] != ""):
            excluded.append(row["excluded"])

firstnames_tmp_file = "target/firstnameOccurrence.csv"

firstnames_tmp = []

with open(firstnames_tmp_file, mode="r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        if(row["firstname"] != ""):
            if(row["firstname"] not in excluded):
                firstnames_tmp.append(row["firstname"])

firstnames_file = "target/firstnames.csv"

firstnames = []

with open(firstnames_file, mode="r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
        if(row["firstnames"] != ""):
                firstnames.append(row["firstnames"])

with open(firstnames_file, mode="a", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for firstname in firstnames_tmp:
        if(firstname not in firstnames):
            writer.writerow([firstname])
