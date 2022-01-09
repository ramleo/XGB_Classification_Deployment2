def deal_with_skew(data=None):
    '''
    Dropping highly skewed variables i.e. any categorical or discrete variables having more than 70%
    # data points in particular category
    '''
    skew_num = []

    num_vars = data.columns

    for var in num_vars:
        if 100*data[var].value_counts(normalize=True).values[0] > 70:
            skew_num.append(var)
    skew_num.sort()
    var = ['monthly_3g_6', 'monthly_3g_7', 'monthly_3g_8', 'sachet_3g_6', 'sachet_3g_7', 'sachet_3g_8']
    skew_nums = [i for i in skew_num if i not in var]

    data.drop(skew_nums, axis=1, inplace=True)

    return data.copy()