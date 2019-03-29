import re
import urllib.request
import pandas as pd
#myfile = urllib.request.urlopen('http://ksbc.kerala.gov.in/reports/may_june_july/RMCI.TXT')
myfile = urllib.request.urlopen('http://www.ksbc.kerala.gov.in/circular/prmtrlisthigh1218.txt')
data = myfile.readlines()
dict_list = []
t = ('.*\s(?P<SERIAL_NO>[0-9]+)\s(?P<ITEM_CODE>[0-9][0-9][0-9][0-9][0-9][0-9]).*\s\s'
'(?P<DESCRIPTION>[A-Z].*[A-Z])\s.*\s(?P<MAX_AMOUNT>[0-9]+[.][0-9][0-9]).*')

t1 = ('.*(?P<Product_Code>[0-9]{9}|[0-9]{8}[A-Z])\s*(?P<Description>[A-Z].*[A-Z])\s.*\s(?P<UOM>[0-9]+)'
'\s*(?P<L_Cost>[0-9]+[.][0-9][0-9])\s*(?P<Stock>[0-9]+)\s*(?P<Amount>[0-9]+[.][0-9][0-9]).*')
for line in data:
    match = re.match(t, str(line))
    if match:
        new_dict = match.groupdict()
        dict_list.append(new_dict)
for i in range(10):
    print(data[i])
for i in range (30):
    print(dict_list[i])
print(len(dict_list))
print(len(data))
#df = pd.DataFrame(dict_list)

#print(df.columns.values)
#print(df)
