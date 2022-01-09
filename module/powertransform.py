def power_transf(data=None):
    '''Power transforming the variables to deal with outliers'''

    # Importing relevant packages
    from sklearn.preprocessing import PowerTransformer
    
    var = list(data.columns)
    pt = PowerTransformer()
    data[var] = pt.fit_transform(data[var])

    return data