import csv,sys
            
imf = csv.DictReader(open("IMF-csv/data/IMF-matrix-2011.csv"))
unctad_f = csv.DictReader(open("UNCTAD-csv/data/UNCTAD-matrix-2011.csv"))

# create dictionary with UNCTAD data
unctad = {}
for row in unctad_f:
    country = row['country']
    unctad[country] = row
    del unctad[country]['country']

newdict = {}
fieldnames = ['country']

for row in imf: # go row by row through IMF file and import UNCTAD cells if encountering an empty cell

    country = row['country']
    newdict[country] = {}
    fieldnames.append(country)

    for column in row:
        if column == 'country':
            cell = row[column]

        else:
            try:
                cell = float(row[column])
            except (ValueError, KeyError):
                try:
                    cell = float(unctad[country][column])
                except (ValueError, KeyError):
                    cell = ''

        newdict[country][column] = cell        

# import pprint
# pprint.pprint(newdict)

writer = csv.DictWriter(open("IMF-UNCTAD-matrix.csv","wb"), fieldnames=fieldnames)

writer.writeheader()

for country in newdict:
    writer.writerow(newdict[country])

