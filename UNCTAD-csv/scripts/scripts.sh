for i in `ls *xls`; do in2csv --sheet outstock "webdiaeia2014d3_"$i".xls" > $i.csv; done
