# csv2Html

import pandas as pd
import csv
import os
import re

# to read csv file 
df = pd.read_csv('A_QdmSbs.csv',encoding='utf-8')

# df_goal = pd.DataFrame(df,columns=['Absolute Number','Object Text','Objekttyp'])
# df_goal = pd.DataFrame(df,columns=['Absolute Number','Object Text','Objekttyp'])
df_goal = pd.DataFrame(df,columns=['ASIL','Objekttyp','Object Text'])

# replace the umlaut
Umlaut = 'äöüß'
for Umlaut in Umlaut:
    if Umlaut == 'ä':
        df_goal['Object Text']=df_goal['Object Text'].str.replace(Umlaut,'ae')
    elif Umlaut == 'ö':
        df_goal['Object Text']=df_goal['Object Text'].str.replace(Umlaut,'oe')
    elif Umlaut == 'ü':
        df_goal['Object Text']=df_goal['Object Text'].str.replace(Umlaut,'ue')
    elif Umlaut == 'ß':
        df_goal['Object Text']=df_goal['Object Text'].str.replace(Umlaut,'ss')

# print(df)
# to save as html file
df_goal.to_html("csv2html_sbs.html")
 
# assign it to a variable (string)
html_file = df_goal.to_html()

# csv2Html


# Json2Html

# import json
# from json2html import *

# # dict_str = open('A_QdmMueWra_links.json','r',encoding='utf-8').read()

# # data_dict = json.loads(dict_str)
# data_dict = json.load(open('A_QdmMueFnc.json', encoding='utf-8-sig'))
# data_xml = json2html.convert(data_dict)
# # data_xml = json2html.convert(json=data_dict, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
# print("data_xml", data_xml)
# html_head = '''<!DOCTYPE html>
# <body>
# {}
# </body>
# </html>'''
# result_html = html_head.format(data_xml)

# with open('json2html.html','w',encoding='utf-8') as file:
#     file.write(result_html)

# Json2Html