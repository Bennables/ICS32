#imports the returnquests library for https calls
import requests

#inports the session lib that will allow us to create a session object for the purpose of shar
from requests import Session
#imports a json library called pretty print to print json more visually appealing "pretty"
from pprint import pprint as pretp

class CryptoClassAPI:

    
    def __init__(self) -> None:
        #api url to connect to
        self.apiurl = 'https://pro-api.coinmarketcap.com'
         
        #defintes data structure to store the type of data we will accpt as wel as a variabl to
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY':'52de344a-eecb-43de-83b1-143dee0349a8'}
        
        #creates a session object instance that we will use for our data exchange session with the api
        self.session = Session()
        
        #Defines the shared connection info we are going to retain accross the session
        self.session.headers.update(self.headers)

    def getPrice(self,symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params = parameters)
        data = r.json()['data']
        return data
    
    def getAllListings(self,start,end):
        url = self.apiurl + '/v1/cryptocurrency/listings/latest'
        parameters = {'start':start, 'limit':end}
        r = self.session.get(url, params = parameters)
        data = r.json()['data']
        return data

if __name__ == '__main__':
    cryptoinstance = CryptoClassAPI()
    # print(cryptoinstance.getPrice())
    pretp(cryptoinstance.getPrice('BTC'))
    pretp(cryptoinstance.getAllListings('1','1000'))