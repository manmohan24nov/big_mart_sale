import load_data

test, train = load_data.main()

# print(test.describe())


def main():

    train['Item_Fat_Content'] = train['Item_Fat_Content'].map({'Low Fat':'0.1',
                                                               'Regular':'0.2',
                                                               'low fat':'0.1',
                                                               'LF':'0.1',
                                                               'reg':'0.1'}).astype('float')
    train['Item_Type'] = train['Item_Type'].map({'Dairy':'0.11', 'Soft Drinks':'0.12', 'Meat':'0.13',
                                                 'Fruits and Vegetables':'0.14', 'Household':'0.15','Baking Goods':'0.16',
                                                 'Snack Foods':'0.17', 'Frozen Foods':'0.18', 'Breakfast':'0.19',
                                                 'Health and Hygiene':'0.20', 'Hard Drinks':'0.1', 'Canned':'0.21',
                                                 'Breads':'0.22', 'Starchy Foods':'0.23', 'Others':'0.25',
                                                 'Seafood':'0.24'}).astype('float')

    train['Outlet_Location_Type'] = train['Outlet_Location_Type'].map({'Tier 1':'0.1', 'Tier 3':'0.3',
                                                                       'Tier 2':'0.2'}).astype('float')

    test['Item_Fat_Content'] = test['Item_Fat_Content'].map({'Low Fat': '0.1',
                                                             'Regular': '0.2',
                                                             'low fat': '0.1',
                                                             'LF': '0.1',
                                                             'reg': '0.1'}).astype('float')
    test['Item_Type'] = test['Item_Type'].map({'Dairy': '0.11', 'Soft Drinks': '0.12', 'Meat': '0.13',
                                               'Fruits and Vegetables': '0.14', 'Household': '0.15',
                                               'Baking Goods': '0.16',
                                               'Snack Foods': '0.17', 'Frozen Foods': '0.18', 'Breakfast': '0.19',
                                               'Health and Hygiene': '0.20', 'Hard Drinks': '0.1', 'Canned': '0.21',
                                               'Breads': '0.22', 'Starchy Foods': '0.23', 'Others': '0.25',
                                               'Seafood': '0.24'}).astype('float')

    test['Outlet_Location_Type'] = test['Outlet_Location_Type'].map({'Tier 1': '0.1', 'Tier 3': '0.3',
                                                                     'Tier 2': '0.2'}).astype('float')

    return test, train


# data.apply(lambda x: len(x.unique()))
# train[['Item_Identifier']] = sc.fit_transform(train[['Item_Identifier']])
# test[['total_income']] = sc.fit_transform(test[['total_income']])
# train['Item_Identifier']=pd.get_dummies(train['Item_Identifier'],prefix_sep='_')

if __name__ == '__main__':
    main()


# print(train.dtypes)
# # print(train.groupby('Item_Identifier').size())
# train['item_identifier_type'] = train['Item_Identifier'].apply(lambda x : x[:3])
# print(train['item_identifier_type'])
# print(train.columns)
# print(train.groupby(['item_identifier_type']).size())
