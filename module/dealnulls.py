def deal_with_nulls(data=None):
    '''Columns with more than 70% missing but meaningful missing'''
    col = ['total_rech_data_6','max_rech_data_6','count_rech_2g_6','count_rech_3g_6','av_rech_amt_data_6',
           'arpu_3g_6','arpu_2g_6','total_rech_data_7','max_rech_data_7','count_rech_2g_7','count_rech_3g_7',
           'av_rech_amt_data_7','arpu_3g_7','arpu_2g_7','total_rech_data_8','max_rech_data_8',
           'count_rech_2g_8', 'count_rech_3g_8', 'av_rech_amt_data_8','arpu_3g_8', 'arpu_2g_8']

    # Imputing 'NaN' with '0'
    for i in col:
        data[i].fillna(0, inplace=True)

    # Columns with more than 70% missing and unnecessary columns that needs to be dropped
    date_cols_drop = ['circle_id', 'mobile_number', 'date_of_last_rech_6', 'date_of_last_rech_7',
                      'date_of_last_rech_8', 'night_pck_user_6', 'night_pck_user_7', 'night_pck_user_8',
                      'fb_user_6', 'fb_user_7', 'fb_user_8', 'date_of_last_rech_data_6', 'date_of_last_rech_data_7',
                      'date_of_last_rech_data_8']

    data.drop(columns=date_cols_drop, inplace=True)

    return data.copy()