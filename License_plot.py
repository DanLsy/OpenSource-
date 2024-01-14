import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    enum = ['daily','weekly','monthly']
    #enum = ['daily']
    #enum = ['monthly']
    #enum = ['weekly']
    for choice in enum:
        csvFile = 'github_trending_test1_{}.csv'.format(choice)
        handle = open(csvFile,'r',encoding='utf-8')
        reader = csv.reader(handle)
        data = list(reader)
        data = np.array(data)

        # analysis language
        license = data[1:,2]
        # 将空白字符替换为 NaN
        license = np.where(license == '', np.nan, license)

        df_data = {'License':license}
        df = pd.DataFrame(df_data)
        df.dropna(subset=['License'])
        df.drop(df[df['License']== 'null'].index,inplace=True)
        df.drop(df[df['License']== 'nan'].index,inplace=True)
        df.drop(df[df['License']== 'Viewlicense'].index,inplace=True)
        groups = df.groupby("License").groups
        
        names = []
        values = []
        for item in groups:
             names.append(item)
             values.append(groups[item].size)  
        fig, axs = plt.subplots(1,2,figsize=(40, 10), sharey=True)
        #fig, axs = plt.subplots(figsize=(30, 10), sharey=True)
        #axs.bar(names, values,color='purple')
        axs[0].bar(names, values,color='purple')
        #axs[1].scatter(names, values,color='purple')
        axs[1].plot(names, values,color='purple')
        fig.suptitle('License Plotting')
        plt.savefig("License_Ploting_{}.png".format(choice))