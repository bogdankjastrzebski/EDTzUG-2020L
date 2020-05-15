import pandas as pd

allData = pd.read_excel("LingFeatured NLI_PL_20.03.2020.xlsx")

inputData = allData[['verb', 'verb - main semantic class', 'verb - second semantic class', 'verb - third semantic class', 'verb - tense']]

outputData = allData[['verb - veridical (positive enviroment)', 'verb - veridical (negative enviroment)']]

inputData.to_csv(path_or_buf = "input.csv", index=False)
outputData.to_csv(path_or_buf = "output.csv", index=False)

param_grid_mlp = {
    'activation' : ['identity', 'logistic', 'tanh', 'relu'],
    'solver' : ['lbfgs', 'sgd', 'adam'],
    'alpha' : [0.0001, 0.0005, 0.00001, 0.001],
    'learning_rate' : ['constant', 'invscaling', 'adaptive']
}

param_grid_randomForest = {
    'n_estimators' : range(100, 1000, 10),
    'criterion' : ['gini', 'entropy'],
    'max_features' : ['auto', 'sqrt', 'log2']
}