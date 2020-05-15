import pandas as pd

allData = pd.read_excel("LingFeatured NLI_PL_20.03.2020.xlsx")

inputData = allData[['verb', 'verb - main semantic class', 'verb - second semantic class', 'verb - third semantic class', 'verb - tense']]

outputData = allData[['verb - veridical (positive enviroment)', 'verb - veridical (negative enviroment)']]

inputData.to_csv(path_or_buf = "input.csv", index=False)
outputData.to_csv(path_or_buf = "output.csv", index=False)
