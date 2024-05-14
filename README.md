# IMDB Movie Genre Prediction
This project aims to predict the genres of movies using machine learning and deep learning techniques, achieving its goals through 3 key objectives: explore the data, create analysis and understand it's features; develop a machine learning model using the training set that predicts the main genres of the movies and run inferences of the main genres using your model on the *test_set.xlsx* file.

### Project Content

This project is composed by 3 main folders:

1. *src*: In this folder, there are 3 files. the first one is an exploratory notebook, named *eda.ipynb*, where the exploratory data analysis and notes are contained. There is also a summary of all EDA insights on the *README.md* file, located on the root folder. The other file is the machine learning notebook, named *ml.ipynb* with the pipelines, model training, etc. The last file is *struct.py*, that stores custome pre-processing structures used on the pipeline.
2. *data*: This folder contains all the project data, like the training/testing sets, indexes filter and the test predictions.
3. *models*: This part contains the saved machine learning models for predictions.

### Installing Dependencies

On the root directory of the project, execute the commands below on the terminal:

```bash
pip3 install -r requirements.txt
python -m spacy download en
```

### EDA Insights

- Outliers are present in columns such as NO_OF_VOTES, RUN_TIME, and BUDGET_AMT. Duplicated values in SRC_TITLE_ID were removed, preferring those with more votes.
- Movies can have duplicated names, but these can be resolved using the summary information.
- All movie types (TITLE_TYPE) are the same.
- Some release dates (RELEASE_DT) exceed the title year (TITLE_YR), which might warrant further investigation.
- There are more movie releases between March-May, September-November, and December, with fewer releases between June-August.
- Different types of movie summaries (PLOT_OUTLINE, PLOT_MEDIUM, PLOT_SUMMARY) have varying lengths and content but there is a high intersection between them.
- Average rating (RATING_AVG) and runtime (RUN_TIME) distributions vary among movie genres, aiding in predictive modeling.
- Positive skewness is observed in the number of votes (NO_OF_VOTES) and budget amount (BUDGET_AMT).
- While TITLE_YR, RELEASE_YR, RELEASE_MN, and BUDGET_AMOUNT distributions don't seems to significantly differ between genres, they may indirectly relate to other variables.
- The number of releases by Genre distribution remains relatively consistent across months.
- Action, Animation, Comedy, and Drama are  the genres that spend the most money.
- Animation tends to be the most expensive genre, followed by Action, Biography, and Adventure.
- Certain genres like War and Short (as expected) have shorter runtimes.
- Rating varies significantly across different movie genres.


### Potential Enhancements & Next Steps (weren't addressed due to time constraints)
- Data Augmentation: Try to balance test_train set Smote or gathering more samples from external sources.
- Try Word2Vec instead of TF-IDF on Natural Language Processing.
- Add other variables and more FE, RELEASE_MN, RELEASE_YR.
- Categorize BUDGET_AMT, NO_OF_VOTES, into classes (like: low, medium, high).
- Apply outliers and other parameters tunning, like strategies OneHotEncoder, MinMaxScaler.
- Analyse ROC Curve instead of accuracy, etc.
- Normalization of Skewed Data NO_OF_VOTES, BUDGET_AMT.
- Dimensionality reduction (PCA, etc.)
- Reduce test size on the current dataset (actual is 20%)
- Test other NN architectures (CNN, RNN, LSTM, GRU, etc.)

### Potential Enhancements (Infrastructure)
- Add docstrings, git pre-commit syntax reviewer, pep8 style guide
- Add Unit tests