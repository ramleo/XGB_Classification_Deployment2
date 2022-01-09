def create_churn_var(file=None):

    '''
    Now tag the churned customers (churn=1, else 0) based on the fourth month as follows:¶
    Those who have not made any calls (either incoming or outgoing) AND have not used mobile\
    internet even once in the churn phase. The attributes we need to use to tag churners are\
    total_ic_mou_9, total_og_mou_9, vol_2g_mb_9, vol_3g_mb_9
    '''

    # Import relevant packages
    import pandas as pd

    # Importing the dataset
    data = pd.read_csv(r'C:\Users\DA1041TU\Documents\UpGrad\Data\Telecom_churn_CaseStudy_Data'+file)

    data['churn'] = data.apply(lambda row: 1 if (row.total_og_mou_9 == 0 and row.total_ic_mou_9 == 0
                                                 and row.vol_2g_mb_9 == 0 and row.vol_3g_mb_9 == 0
                                                 ) else 0, axis=1)
    # Dropping columns related to month 9
    month_9_cols = [i for i in data.columns if i[-1] == '9']
    data.drop(labels=month_9_cols, axis=1, inplace=True)

    return data