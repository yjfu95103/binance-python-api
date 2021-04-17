# binance-python-api
![](https://img.shields.io/static/v1?label=python&message=3.8&color=blue)
> Using Binance official api to display your currency distribution.

## Result  
* my ticker distribution for example
![image](https://github.com/yjfu95103/binance-python-api/blob/main/picture/20210417_011819.png)

## Environment setup
* create & launch env
```
$ pip3 install pipenv  #install lib
$ pipenv --python 3.8
$ pipenv shell         #launch env
$ pip3 install -r requirements.txt
```
* quit
```
$ exit                 
```

## How to use
* add your binance api in ticker_percent.py
```
$ api_key = your_api_key 
$ api_secret = your_api_secret
```
* run api
```
$ python3 ticker_percent.py
```


