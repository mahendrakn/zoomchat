import pandas as pd
from datetime import date

#read_data = open("file path and file_name", 'r')           #mention file path which you want to transform               
data = read_data.readlines()

txt_list = []                                               #creating an empty list to store texts 
Info_list = []                                              #creating an empty list to store information
for j,i in enumerate(data):
    # finding whether this words present or not
    con_check = i.find('From') and i.find('to') and i.find('(')  
    if con_check == 0:                                      #if found it will return zero else will return -1
        #print(i)
        temp_dict = {}
        txt_list = []
        
        fin_from = i.find('From')                           #finding sub string and location present in the line 
        fin_to = i.find('to')
        to = i.find(':')
        txt_fin = i.find('(')
        fin_txt = i.find(')')
        fin_time = i.find('\n')
        
        info_from = i[fin_from+5: fin_to -1]
        temp_dict['From'] = info_from                      #assigning values with respect particular key to the Dictionary variable 
        info_to = i[fin_to+3 : to]
        temp_dict['To'] = info_to
        info_msgtype = i[to+4: fin_txt]
        temp_dict['MessageType'] = info_msgtype
        info_time = i[fin_txt+2:fin_time]
        temp_dict['MessageTime'] = info_time
        Info_list.append(temp_dict)
        
    else:
        txt = ""                                           #creating an empty string variable to store the text
        i = i.strip("\n")
        txt_list.append(i)
        
        for i in txt_list:
            txt = txt +" "+ i
        temp_dict['Text'] = txt                            #assigning values with respect particular key to the Dictionary variable
        if j == len(data)-1 or data[j+1].find('From') and data[j+1].find('to') and data[j+1].find('(') == 0:
            Info_list.append(temp_dict)  

df = pd.DataFrame(Info_list)                               #converting dict variable into dataframe
df.drop(df.tail(1).index,inplace=True)           # droping last 1 row

today = date.today()
#print("Today's date:", today)

#converting dataframe into csv 
df.to_csv(f"C:\\Users\\user\\Desktop\\ZoomChat_{today}.csv", index = False)



   
