def impute_conv_df(data=None):
    '''Converting the imputed ndarray into a dataframe'''

    # Importing relevant packages
    import pandas as pd
    from module.createvariables import create_vars
    # Creating list of columns to use in df
    _,null_num, total_cols = create_vars()
    total_vars = null_num

    for i in total_cols:
        if i not in total_vars:
            total_vars.append(i)

    # Creating dataframe
    data = pd.DataFrame(data, columns=total_vars)

    return data.copy()