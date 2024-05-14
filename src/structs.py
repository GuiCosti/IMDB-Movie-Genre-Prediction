class BasePreProcessorStep():
    """
    Base pre-processor class that can be used to stack custom
    steps for data cleaning and manipulation
    """
    def __init__(self):
        pass
    
    def fit_transform(self, df, numeric_features, categorical_features):
        raise NotImplementedError("Subclasses must implement fit_transform method.")
    
    def add_to_list(self, li, item):
        """
        Add item to list. Can be used to modify numeric and categorical values
        on Feature Engineering process, for example.
        """
        if item not in li:
            li.append(item)
            
    def remove_item_from_list(self, li, item):
        """
        Remove item from list. Can be used to modify numeric and categorical values
        on Feature Engineering process, for example.
        """
        li = [x for x in li if x != item]

class PreProcessor():
    """
    Pre-processor class that execute BasePreProcessor steps chain.

    Parameters:
    -----------
    steps : array
        Chain of BasePreProcessor steps to be executed.
    numeric_features : array
        Numeric features of the dataframe.
    categorical_features : array
        Categorical features of the dataframe.
    """
    def __init__(self, steps, numeric_features=[], categorical_features=[]):
        self.steps = steps
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features

    def run(self, df):
        """
        Execute the pre-processor pipeline on DataFrame

        Parameters:
        -----------
        df : DataFrame
            Target DataFrame to be processed.
        """
        for step in self.steps:
            step.fit_transform(df, self.numeric_features, self.categorical_features)