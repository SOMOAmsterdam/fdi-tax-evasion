for i in `ls .`; do in2csv --sheet Outward $i | tail -n+7 | head -n -10 | csvcut -c 1,2 > $i.csv; done
for i in `ls .csv`;do sed -i 's/Bahamas,\ The/Bahamas/' xls; done (+Slovak Republic, Slovakia; British Virgin Islands)
