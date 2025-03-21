from data_access.data_access_csv import data_access_csv

data_access = data_access_csv()

excluded_file = "ressources/excluded_words.csv"

excluded = data_access.get_column(excluded_file, "excluded")

firstnames_tmp_file = "target/firstnameOccurrence.csv"

firstnames_tmp = data_access.get_column(firstnames_tmp_file, "firstname")

firstnames_file = "target/firstnames.csv"

firstnames = data_access.get_column(firstnames_file, "firstnames")

excluded.append(firstnames)

result = {}

for firstname in firstnames_tmp:
    if firstname not in excluded:
        result.append({"firstnames" : firstname})

data_access.append(firstnames_file, result)
