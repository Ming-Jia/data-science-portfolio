def find_col_with_na(df):
    '''
    Find column that contains NA in DataFrame
    
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
    
    Returns
    -------
    col_with_na: pandas.core.indexes.base.Index
        Column(s) that contains NA
    has_na: pandas.core.series.Series
        True/False for each column in the DataFrame
    '''
    
    col_sum_na = df.isnull().sum()
    has_na = col_sum_na > 0
    col_with_na = df.columns[has_na]
    
    return col_with_na, has_na


def calculate_na_pct(df):
    '''
    Calculate the NA percentage per column
    
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
    
    Returns
    -------
    pandas.core.series.Series
        Percentage of NA in columns by descending order
    '''
    
    col_sum_na = df.isnull().sum()
    has_na = col_sum_na > 0
    col_na_pct = (col_sum_na / len(df) * 100)[has_na].sort_values(ascending=False)
    
    return col_na_pct