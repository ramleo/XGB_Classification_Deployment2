def hvc_filter(data=None):
    '''Filtering high value customers'''
    
    # Creating new column by taking average of total recharge fro month 6 and month 7
    data['avg_amt_6_7'] = (data['total_rech_amt_6']+data['total_rech_amt_7'])/2

    # Filtering high value customers taking 70th percentile as a theshold
    hvc = data.loc[data['avg_amt_6_7']>=data['avg_amt_6_7'].quantile(q=0.7), :].copy()

    # Dropping the 'avg_amt_6_7' variable as it is not required now
    hvc.drop('avg_amt_6_7', axis=1, inplace=True)

    return hvc.copy()