def model_metrics(model_list=None, data=None, target=None, class_type=None):
    '''
    A function for calculating the classification metrics such as accuracy_score, recall_score, precision_score, f1_score, fbeta_score,
    roc_auc_score, cohen_kappa_score, hinge_loss, hamming_loss, log_loss using a model, and returning a pandas dataframe, or
    calculating the regression metrics such as rsquare, mean_absolute_error,median_absolute_error,
    mean_squared_error and root_mean_squared_error using a model, and returning a pandas dataframe.
    model = List of either classification or regression model,
    data = Should be a pandas dataframe,
    target = Should be pandas series
    class_type = Should be a string and can be any of the 'classification', 'classif', 'regression', 'regress' or 'reg'
    '''

    # Importing classification relevant packages
    import pandas as pd
    from sklearn.metrics import (accuracy_score, recall_score, precision_score, f1_score, fbeta_score,
                                 roc_auc_score, cohen_kappa_score, hinge_loss, hamming_loss, log_loss)
    from sklearn.metrics import (r2_score, mean_absolute_error,
                                 median_absolute_error, mean_squared_error)

    # Creating empty dictionary
    dictionary = dict()

    if (class_type.lower() == 'classification') or (class_type.lower() == 'classif'):

        # Creating a loop to append empty lists provided in the empty dictionary with metrics
        for i in range(len(model_list)):
            dictionary[str(model_list[i])] = list()
            y_pred = model_list[i].fit(data, target).predict(data)
            accuracy = round(accuracy_score(target, y_pred), 2)
            recall = round(recall_score(target, y_pred), 2)
            precision = round(precision_score(target, y_pred), 2)
            f1 = round(f1_score(target, y_pred), 2)
            fbeta = round(fbeta_score(target, y_pred, beta=2.5), 2)
            roc_auc = round(roc_auc_score(target, y_pred), 2)
            cohen_kappa = round(cohen_kappa_score(target, y_pred), 2)
            hin_loss = round(hinge_loss(target, y_pred), 2)
            ham_loss = round(hamming_loss(target, y_pred), 2)
            logl_loss = round(log_loss(target, y_pred), 2)
            dictionary[str(model_list[i])].append(accuracy)
            dictionary[str(model_list[i])].append(recall)
            dictionary[str(model_list[i])].append(precision)
            dictionary[str(model_list[i])].append(f1)
            dictionary[str(model_list[i])].append(fbeta)
            dictionary[str(model_list[i])].append(roc_auc)
            dictionary[str(model_list[i])].append(cohen_kappa)
            dictionary[str(model_list[i])].append(hin_loss)
            dictionary[str(model_list[i])].append(ham_loss)
            dictionary[str(model_list[i])].append(logl_loss)

        # Creating columns list to rename the dataframe
        cols = []
        for i in list(dictionary.keys()):
            i = i.split('(')[0]
            cols.append(i)

        # Creating a dataframe out the resultant dictionary
        metric_df = pd.DataFrame(dictionary, index=['Accuracy', 'Recall', 'Precision', 'F1',
                                                    'FBeta', 'ROC_AUC', 'Cohen_Kappa_Score',
                                                    'Hinge_Loss', 'Hamming_Loss', 'Log_Loss'])

        # Renaming the dataframe
        metric_df.columns = cols

    elif (class_type.lower() == 'regression') or (class_type.lower() == 'regress') or (class_type.lower() == 'reg'):

        # Creating a loop to append empty lists provided in the empty dictionary with metrics
        for i in range(len(model_list)):
            dictionary[str(model_list[i])] = list()
            y_pred = model_list[i].fit(data, target).predict(data)
            rsquare = r2_score(target, y_pred)
            mean_ab_error = mean_absolute_error(target, y_pred)
            med_ab_error = median_absolute_error(target, y_pred)
            mean_sq_error = mean_squared_error(target, y_pred)
            rmse = np.sqrt(mean_squared_error(target, y_pred))
            dictionary[str(model_list[i])].append("{:.3f}".format(rsquare))
            dictionary[str(model_list[i])].append("{:.3f}".format(mean_ab_error))
            dictionary[str(model_list[i])].append("{:.3f}".format(med_ab_error))
            dictionary[str(model_list[i])].append("{:.3f}".format(mean_sq_error))
            dictionary[str(model_list[i])].append("{:.3f}".format(rmse))

        # Creating columns list to rename the dataframe
        cols = []
        for i in list(dictionary.keys()):
            i = i.split('(')[0]
            cols.append(i)

        # Creating a dataframe out the resultant dictionary
        metric_df = pd.DataFrame(dictionary, index=['RSquare', 'Mean_ABS_Error', 'Median_ABS_Error',
                                                    'Mean_Sq_Error', 'RMSE'])

        # Renaming the dataframe
        metric_df.columns = cols

    return metric_df