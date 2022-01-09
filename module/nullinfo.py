def null_info(data=None):
    # Total number of missing variables
    print('Total number of missing variables are -', len(data.columns[100 * (data.isnull().sum()) / data.shape[0] > 0]))
    print('*' * 70)

    # Variables that need to be dropped
    miss_drop = data.columns[100 * (data.isnull().sum()) / data.shape[0] >= 70]
    print('Number of variables that need to be dropped are -', len(miss_drop))
    print('*' * 70)

    # Variables that need to be imputed using mean/median
    miss_bet_0_70 = list((data.columns[100 * (data.isnull().sum()) / data.shape[0] > 0] & \
                          data.columns[100 * (data.isnull().sum()) / data.shape[0] <= 70]))
    print('Variables that need to be imputed using mean/median')
    print('Number of variables beyween 0% and 70% are -', len(miss_bet_0_70))
    print('*' * 70)

    # Shape of the dataset
    print('Shape of the dataset is -', data.shape)
    print('*' * 70)