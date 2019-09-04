import pandas as pd



# print(train.isnull().sum(axis=0))
# print(test.isnull().sum(axis=0))
#
# print(train.columns)
# Set ipython's max row display
pd.set_option('display.max_row', 1000)

# Set iPython's max column width to 50
pd.set_option('display.max_columns', 50)
# print(train.describe())

# print(train.Item_Type.value_counts())
# print(train.count())
# print(train.groupby(["Item_Identifier", "Outlet_Identifier","Item_Weight","Item_Fat_Content", "Item_Visibility", "Item_Type", "Item_MRP", "Item_Outlet_Sales", "Outlet_Type"]).size())
# print(train[["Item_Visibility","Item_MRP"]].corr())

# print(train[['Item_Identifier','Item_Weight','Outlet_Size']].loc[train['Item_Weight'].isnull()])
# var1 = train[['Item_Identifier','Item_Weight']].groupby(['Item_Identifier', 'Item_Weight']).agg({'Item_Identifier':'count','Item_Weight':'nunique'})
# print(var1.query('Item_Weight > 1'))


def main():
    train = pd.read_csv('Train_UWu5bXk.csv', header=0, sep=',')
    test = pd.read_csv('Test_u94Q5KV.csv', header=0)

    null_values_train = list(set(train['Item_Identifier'][train['Item_Weight'].isnull()].to_list()))
    for i in null_values_train:
        try:
            values = train[(train['Item_Identifier'] == i) & (train['Item_Weight'].notnull())].values[0][1]
        except IndexError:
            pass

        mask = train['Item_Identifier'] == i
        train.loc[mask, 'Item_Weight'] = values

    null_values_test = list(set(test['Item_Identifier'][test['Item_Weight'].isnull()].to_list()))
    for i in null_values_test:
        try:
            values = test[(test['Item_Identifier'] == i) & (test['Item_Weight'].notnull())].values[0][1]
        except IndexError:
            pass

        mask = test['Item_Identifier'] == i
        test.loc[mask, 'Item_Weight'] = values

    # print(train[['Item_Identifier','Item_Weight']][train['Item_Identifier']=='FDE52'])
    # print(train[(train['Item_Identifier'] == 'FDE52') & (train['Item_Weight'].notnull())].values[0][1])
    # print(train[['Item_Identifier','Item_Weight']][train['Item_Identifier']=='FDP10'])
    test = test.fillna(value={'Outlet_Size' : 'Unknown'})
    train = train.fillna(value={'Outlet_Size' : 'Unknown'})

    return test, train


if __name__ == '__main__':
    main()

# print(train.isnull().sum(axis=0))
# print(test.isnull().sum(axis=0))
