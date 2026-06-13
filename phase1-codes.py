# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:36:02 2023

@author: 1
"""
import pandas as pd
import matplotlib.pyplot as plt
root = 'C:/Users/1/Desktop/Sharif/Python Programming/project2'
DF = pd.read_csv(root + '/gorgan_census95_activity.csv')
#print(DF)

####################################################################
DF_U = DF[DF['settlement']=='شهري']
DF_R = DF[DF['settlement']=='روستايي']

X_Urban = DF_U['emp_ratio'].tolist()
X_Rural = DF_R['emp_ratio'].tolist()


####################################################################
DF_W = DF[DF['gender']=='زن']
DF_M = DF[DF['gender']=='مرد']

X_Women = DF_W['emp_ratio'].tolist()
X_Men = DF_M['emp_ratio'].tolist()


####################################################################
DF_1014 = DF[DF['age_group']=='10-14']
DF_1519 = DF[DF['age_group']=='15-19']
DF_2024 = DF[DF['age_group']=='20-24']
DF_2529 = DF[DF['age_group']=='25-29']
DF_3034 = DF[DF['age_group']=='30-34']
DF_3539 = DF[DF['age_group']=='35-39']
DF_4044 = DF[DF['age_group']=='40-44']
DF_4549 = DF[DF['age_group']=='45-49']
DF_5054 = DF[DF['age_group']=='50-54']
DF_5559 = DF[DF['age_group']=='55-59']
DF_6064 = DF[DF['age_group']=='60-64']
DF_6500 = DF[DF['age_group']=='65+']

X_1014 = DF_1014['emp_ratio'].tolist()
X_1519 = DF_1519['emp_ratio'].tolist()
X_2024 = DF_2024['emp_ratio'].tolist()
X_2529 = DF_2529['emp_ratio'].tolist()
X_3034 = DF_3034['emp_ratio'].tolist()
X_3539 = DF_3539['emp_ratio'].tolist()
X_4044 = DF_4044['emp_ratio'].tolist()
X_4549 = DF_4549['emp_ratio'].tolist()
X_5054 = DF_5054['emp_ratio'].tolist()
X_5559 = DF_5559['emp_ratio'].tolist()
X_6064 = DF_6064['emp_ratio'].tolist()
X_6500 = DF_6500['emp_ratio'].tolist()


####################################################################
def hist_chart(name , x , num_bins):
    plt.hist(x , bins=num_bins)
    name1 = (name.split('_'))[1]
    name1 += ' emp_ratio'
    plt.title((name1 + ' chart'))
    plt.xlabel(str(name1))
    plt.ylabel('count')
    plt.show()

######
hist_chart('X_Urban', X_Urban, 20)
hist_chart('X_Rural', X_Rural, 20)
######

######
hist_chart('X_Women', X_Women, 20)
hist_chart('X_Men', X_Men, 20)
######

######
hist_chart('X_1014', X_1014, 20)
hist_chart('X_1519', X_1519, 20)
hist_chart('X_2024', X_2024, 20)
hist_chart('X_2529', X_2529, 20)
hist_chart('X_3034', X_3034, 20)
hist_chart('X_3539', X_3539, 20)
hist_chart('X_4044', X_4044, 20)
hist_chart('X_4549', X_4549, 20)
hist_chart('X_5054', X_5054, 20)
hist_chart('X_5559', X_5559, 20)
hist_chart('X_6064', X_6064, 20)
hist_chart('X_6500', X_6500, 20)
######

##############################################################################
D1 = DF_M[DF_M['age_group'] != '10-14']
D1 = D1[D1['age_group'] != '65+']
#D1.info()
D1_d = (D1.sort_values('emp_ratio' , ascending = True))
D1_d[['county_name' , 'age_group' , 'settlement']].reset_index().head(40)

D2 = DF_W[DF_W['age_group'] != '10-14']
D2 = D2[D2['age_group'] != '65+']
#D2.info()
D2_d = (D1.sort_values('emp_ratio' , ascending = False))
D2_d[['county_name' , 'age_group' , 'settlement']].reset_index().head(40)































