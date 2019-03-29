import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import re


#Need to install bs4 using the command 'pip install beatifulsoup4'

class Webscraper:

    def __init__(self):
        self.txt_url_list = []
        #Collects urls from a user-provided txt file
        txt_file = input('Please provide the name of txt file with request urls\n')
        with open(txt_file) as f:
            self.url_list = f.readlines()
        self.url_list = [u.strip() for u in self.url_list]
        self.table_list = []
        self.txt_list = []
        self.data_tables = []

    #For each txt url, create a pandas dataframe
    def read_txt_files(self):
        for url in self.txt_list:
            try:
                self.fn_txt(url)
            except:
                print("Failed to extract table from " + str(url))

    def scrape_txt_urls(self, urls, count):
        new_urls = []
        #Specifies how deep the user wants to navigate the web
        #Can modify the value '2' to allow narrower/deeper search
        if count > 2:
            return
        else:
            for url in urls:
                if '.txt' in url or '.TXT' in url:
                    self.txt_list.append(url)
                else:
                    try:
                        URL_eg = urllib.request.urlopen(url)
                        soup = BeautifulSoup(URL_eg)
                        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
                            #If link contained in url points to a txt file, store it in a list
                            #to analyze it. Else, keep navigating.
                            new_url = link.get('href')
                            if '.txt' in new_url or '.TXT' in new_url:
                                self.txt_list.append(new_url)
                            else:
                                new_urls.append(new_url)
                    except:
                        print("Couldn't connect to a link " + str(url))
        count += 1
        self.scrape_txt_urls(new_urls, count)

    def fn_txt(self, url):
        print(url)
        URL_eg = urllib.request.urlopen(url)
        df = pd.read_csv(URL_eg, sep='\t')


        """
        The code below is hardcoded to extract specfic data from txt file and separate the columns.
        It assumes txt file with the same template as http://www.ksbc.kerala.gov.in/circular/prmtrlisthigh1218.txt
        """
        myfile = urllib.request.urlopen(url)
        data = myfile.readlines()
        dict_list = []
        #Use regex to extract out the relevant fields. Need to hardcode for different txt files though.
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
        new_df = pd.DataFrame(dict_list)
        #Here, user can just pass in df instead of new_df for simplicity,  but it won't separate the columns
        self.data_tables.append(new_df)
        self.data_tables.append(df)

    def print_url(self):
        print(self.txt_list)

    def print_tables(self):
        for t in self.data_tables:
            print(t)

    #Merge tables gathered from different txt files into a single dataframe
    def merge_tables(self):
        result = pd.concat(self.data_tables)
        return result

    #Converts all datatables into csvfiles
    def to_csv(self):
        #Uncomment below block if the user wants to merge all tables from different txt files
        """"
        final_table = self.merge_tables()
        self.data_tables.append(final_table)
        """
        count = 1
        for t in self.data_tables:
            try:
                #As more templates are hardcoded, more headers are needed
                header = ['SERIAL.NO', 'ITEM_CODE', 'DESCRIPTION', 'MAX_AMOUNT']
                t.to_csv('data' + str(count) + '.csv', columns=header, index=True)
            except:
                print('Continuing')
                t.to_csv('data' + str(count) + '.csv', sep='\t', encoding='utf-8', index=True)
            finally:
                count+=1


sample = Webscraper()
sample.scrape_txt_urls(sample.url_list, 0)
sample.print_url()
sample.read_txt_files()
sample.print_tables()
sample.to_csv()