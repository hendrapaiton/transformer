import pandas as pd


def get_data_csv(files):
    data = pd.read_csv(files)
    return data


if __name__ == '__main__':
    result = pd.DataFrame(
        columns=[
            'Company', 'Country', 'Date From', 'Date To',
            'Type', 'Emission in tCO2', 'Verified By'
        ]
    )
    data = get_data_csv('source.csv')
    for i in data.index:
        if data['Scope 1 Emissions Total tCO2'] is not None or data['Scope 1 Emissions Total tCO2'] is not None:
            result = pd.concat([result, pd.DataFrame.from_records([{
                'Company': data['Company'][i],
                'Country': data['Country'][i],
                'Date From': data['Date From'][i],
                'Date To': data['Date To'][i],
                'Type': 'Scope 1',
                'Emission in tCO2': data['Scope 1 Emissions Total tCO2'][i],
                'Verified By':data['Scope 1 Emissions Verified By'][i]
            }])])
        if data['Scope 2 Emissions Total tCO2'] is not None or data['Scope 2 Emissions Total tCO2'] is not None:
            result = pd.concat([result, pd.DataFrame.from_records([{
                'Company': data['Company'][i],
                'Country': data['Country'][i],
                'Date From': data['Date From'][i],
                'Date To': data['Date To'][i],
                'Type': 'Scope 2',
                'Emission in tCO2': data['Scope 2 Emissions Total tCO2'][i],
                'Verified By':data['Scope 2 Emissions Verified By'][i]
            }])])
        if data['Scope 3 Emissions Total tCO2'] is not None or data['Scope 3 Emissions Total tCO2'] is not None:
            result = pd.concat([result, pd.DataFrame.from_records([{
                'Company': data['Company'][i],
                'Country': data['Country'][i],
                'Date From': data['Date From'][i],
                'Date To': data['Date To'][i],
                'Type': 'Scope 3',
                'Emission in tCO2': data['Scope 3 Emissions Total tCO2'][i],
                'Verified By':data['Scope 3 Emissions Verified By'][i]
            }])])
    print(result)
