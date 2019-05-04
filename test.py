import re
import urllib.request
import pandas as pd
myfile = urllib.request.urlopen('http://ksbc.kerala.gov.in/reports/may_june_july/RMCI.TXT')
data = myfile.readlines()
dict_list = []
entire_list = []
title_list = []
t = '.*\s(?P<SERIAL_NO>[0-9]+)\s(?P<ITEM_CODE>[0-9][0-9][0-9][0-9][0-9][0-9]).*\s(?P<DESCRIPTION>[A-Z].*[A-Z]).*\s(?P<MAX_AMOUNT>[0-9]+[.][0-9][0-9]).*'
t1 = '.*\s(?P<REGION>[A-Z][A-Z][A-Z])\s(?P<TOWN>[A-Z]*)\s.*\s(?P<DATE>[A-Z][A-Z][A-Z]\s[0-9][0-9][0-9][0-9]).*'
t2 = '.*\'(?P<CODE>[0-9][0-9][0-9])\s(?P<DISTILLERY>[A-Z].*[A-Z])\s'
for line in data:
    #print(line)
    match = re.match(t2, str(line))
    entire_list.append(line)
    if match:
        new_dict = match.groupdict()
        """
        new_dict = dict()
        new_dict['SERIAL.NO'] = match.group('SLNO')
        new_dict['ITEM_CODE'] = match.group('IC')
        new_dict['DESCRIPTION'] = match.group('DESC')
        new_dict['MAX_AMOUNT'] = match.group('MQ')
        """
        title_list.append(new_dict)
#for line in dict_list:
#    print(dict_list)
#for i in range (50):
#    print(data[i])
#df = pd.DataFrame(data)
#if df.columns.values is None:
#    print("As expected")
#print(df.columns.values)

#for i in range(10):
#    print(title_list[i])

for line in title_list:
    print(line)
#for i in range(10):
#    print(dict_list[i])
#print(len(title_list))
