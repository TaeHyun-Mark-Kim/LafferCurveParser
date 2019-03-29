import re
import urllib.request
myfile = urllib.request.urlopen('http://www.ksbc.kerala.gov.in/circular/prmtrlisthigh1218.txt')
data = myfile.readlines()
dict_list = []
for line in data:
    match = re.match('.*\s(?P<SLNO>[0-9]+)\s(?P<IC>[0-9][0-9][0-9][0-9][0-9][0-9]).*\s'
                     '(?P<DESC>[A-Z].*[A-Z]).*\s(?P<MQ>[0-9]+[.][0-9][0-9]).*', str(line))
    if match:
        new_dict = dict()
        new_dict['SERIAL.NO'] = match.group('SLNO')
        new_dict['ITEM_CODE'] = match.group('IC')
        new_dict['DESCRIPTION'] = match.group('DESC')
        new_dict['MAX_AMOUNT'] = match.group('MQ')
        dict_list.append(new_dict)
for line in dict_list:
    print(dict_list)
print(len(dict_list))
