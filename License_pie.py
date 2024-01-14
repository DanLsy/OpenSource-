import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    enum = ['daily', 'weekly', 'monthly']

    for choice in enum:
        csvFile = 'github_trending_test1_{}.csv'.format(choice)
        handle = open(csvFile, 'r', encoding='utf-8')
        reader = csv.reader(handle)
        data = list(reader)
        data = np.array(data)

        # 获取license所在的列
        license = data[1:, 2]
        # 将空白字符替换为 NaN
        license = np.where(license == '', np.nan, license)

        # 去除包含 NaN 的部分
        license = license[~pd.isnull(license)]

        df_data = {'License': license}
        # DataFrame 读入 csv 数据
        df = pd.DataFrame(df_data)
        # 数据清洗，去除空值
        df.dropna(subset=['License'], inplace=True)
        df.drop(df[df['License'] == 'null'].index, inplace=True)
        df.drop(df[df['License'] == 'nan'].index, inplace=True)
        df.drop(df[df['License'] == 'Viewlicense'].index, inplace=True)
        
        groups = df.groupby("License").groups

        labels = []
        sizes = []
        for item in groups:
            labels.append(item)
            sizes.append(groups[item].size)

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')

        plt.plot()
        plt.title("License")
        plt.savefig("License_pie_{}.png".format(choice))
        # plt.show()
