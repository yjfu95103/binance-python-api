from binance.client import Client
import pandas as pd    
#Binance your ticker transfer to piechart

def CoinExchange(curSymbol, exchangeSymbol): #exchange two currencies
    if curSymbol == exchangeSymbol:
        return 1
    symbolType = curSymbol+exchangeSymbol
    result = client.get_symbol_ticker(symbol=symbolType)
    coinPrice = float(result['price'])
    return coinPrice

def BinanceLogin(api_key, api_secret):
    client = Client(api_key, api_secret)
    print("Binance login") #check binance login

    return client

def OwnCurrenciesToData(client):
    info = client.get_account()

    myCoin = info['balances']

    noValueArray = ['LDBNB','XYM'] ## no feture or BNB Vault 
    currArray = []
    currUSDT = []
    for coinName in myCoin:
        if (float(coinName['free']) > 0 or float(coinName['locked']) > 0) and coinName['asset'] not in noValueArray:
            exUSDT = (float(coinName['free'])+float(coinName['locked']))*CoinExchange(coinName['asset'],'USDT')
            if exUSDT > 0.5:
                currUSDT.append(exUSDT) ## change to usdt
                currArray.append(coinName)

    df = pd.DataFrame(currArray)
    df['usd'] = currUSDT
    PieChart(df)
    print(df)
    return df

def PieChart(data):
    import matplotlib.pyplot as plt
    
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    fig1.subplots_adjust(0.1, 0, 1, 1)
    
    theme = plt.get_cmap('jet')
    ax1.set_prop_cycle("color", [theme(1. * i / len(data['usd']))
                                for i in range(len(data['usd']))])
    
    _, _ = ax1.pie(data['usd'], startangle=70, radius=900, pctdistance=1)
    ax1.axis('equal')
    total = sum(data['usd'])
    # print("total:",total)
    plt.legend(
        loc='upper left',
        labels=['%s, %1.1f%%' % (
            l, (float(s) / total) * 100)
                for l, s in zip(data['asset'], data['usd'])],
        prop={'size': 8},
        bbox_to_anchor=(0.0, 1),
        bbox_transform=fig1.transFigure
    )
    from datetime import datetime
    nowTime = datetime.now().strftime('%Y%m%d_%H%M%S')

    plt.savefig(nowTime+'.png', bbox_inches='tight')
    plt.show()

if  __name__ == '__main__':

    api_key = your_api_key 
    api_secret = your_api_secret

    client = BinanceLogin(api_key, api_secret)

    OwnCurrenciesToData(client)

    # print(client.get_deposit_history(asset='BTC'))

    # print(client.get_withdraw_history(asset='BTC'))

    # print(client.get_account_status())

    # print(client.get_asset_balance(asset='BTC')) #search coin free and lock
    # print(client.futures_account_balance())
    # print("lastest price:",client.get_symbol_ticker(symbol="BTCUSDT"))



