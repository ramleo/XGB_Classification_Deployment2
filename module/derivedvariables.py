def derived_vars(data=None):
    # avg_rech_amt_6,avg_rech_amt_7,avg_rech_amt_8
    for i in range(6, 9):
        data['avg_rech_amt_' + str(i)] = round(
            data['total_rech_amt_' + str(i)] / (data['total_rech_num_' + str(i)] + 1), 2)

    # Action Phase - would be looking at the change in user behavior from June + July to August.
    # Deriving new features for the same
    data['arpu_diff'] = data.arpu_8 - ((data.arpu_6 + data.arpu_7) / 2)
    data['total_og_mou_diff'] = data.total_og_mou_8 - ((data.total_og_mou_6 + data.total_og_mou_7) / 2)
    data['total_ic_mou_diff'] = data.total_ic_mou_8 - ((data.total_ic_mou_6 + data.total_ic_mou_7) / 2)
    data['total_rech_num_diff'] = data.total_rech_num_8 - ((data.total_rech_num_6 + data.total_rech_num_7) / 2)
    data['total_rech_amt_diff'] = data.total_rech_amt_8 - ((data.total_rech_amt_6 + data.total_rech_amt_7) / 2)
    data['max_rech_amt_diff'] = data.max_rech_amt_8 - ((data.max_rech_amt_6 + data.max_rech_amt_7) / 2)

    # Drop variables which are used for creating derived variables
    drop_var = ['arpu_8', 'arpu_7', 'arpu_6', 'total_og_mou_8', 'total_og_mou_7', 'total_og_mou_6', 'total_ic_mou_8',
                'total_ic_mou_7', 'total_ic_mou_6', 'total_rech_num_8', 'total_rech_num_7', 'total_rech_num_6',
                'total_rech_amt_8', 'total_rech_amt_7', 'total_rech_amt_6', 'max_rech_amt_8', 'max_rech_amt_7',
                'max_rech_amt_6']

    data.drop(columns=drop_var, inplace=True)

    return data.copy()