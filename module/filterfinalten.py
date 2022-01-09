def filter_10(data=None):
    '''
    Final 10 features selected by the final 3 feature selection techniques such as 'f_classif',
    SelectKBest (with score_func='f_classif') and SelectKBest (with score_func='f_regression')
    '''
    # Importing relevant packages
    from module.createvariables import create_vars

    final_10, _, _ = create_vars()
    data = data[final_10]

    return data.copy()