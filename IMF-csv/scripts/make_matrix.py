import csv, glob

# parse the csvs and make a matrix based on preferred countries.
# BEWARE: of names: Slovak Republic, Bahamas, British Virgin Islands (sed -i before)

# testfile = csv.reader(open("AUT.csv"))

#make a list with countries that we want to explore
countrieslist = csv.reader(open('../../countries-check.csv'))
countries = []
for row in countrieslist:
    countries.append(row[0])    

newdata = []
newdata.append(countries)


for csvf in glob.glob("../*.csv"):

    reader = csv.reader(open(csvf))
    newrow = ['..'] * (len(countries)) #create an empty list as long as the list of countries we have.

    for nr,row in enumerate(reader):

        if nr == 0:
            main_Cname = csvf.replace("../IMF-","").replace("_"," ").replace(".csv","") # name of the csv sheet
            newrow[0] = main_Cname
            print main_Cname

        else:
            for cell in row:
                if cell in countries:
                    print cell
                    pos = countries.index(cell) # first item is the country name
                    print pos

                    newrow[pos] = row[-1] # year 2011 is the last (or second) column

    newdata.append(newrow)

writer = csv.writer(open("IMF-matrix.csv","wb"))
writer.writerows(newdata)
