from apiclient import APIClient
from apiclient.response_handlers import JsonResponseHandler
from pprint import pprint

class MyClient(APIClient):

    BASE_URL = 'https://data-api.polymarket.com/v1'

    def get_leaderboard(self):
        url = f'{self.BASE_URL}/leaderboard'
        return self.get(url, params= {
          'category':'OVERALL', 
          'timePeriod':'DAY', 
          'orderBy':'PNL', 
          'limit':1})

    # {
    #   "rank": "1",
    #   "proxyWallet": "0xa380c504a480f591c7dfbf9944fac3994b9b21ff",
    #   "userName": "JewishNinja",
    #   "xUsername": "",
    #   "verifiedBadge": false,
    #   "vol": 2847212.62269,
    #   "pnl": 365525.156500942,
    #   "profileImage": ""
    # },
    def get_leader_positions(self):
        leaderboard = self.get_leaderboard()
        first_user = leaderboard[0]
        proxy_wallet = first_user['proxyWallet']
        url = f'{self.BASE_URL}/positions'
        return self.get(url, params= {
            'user':proxy_wallet,
            'sizeThreshold':1,
            'limit':100,
            'sortBy':'TOKENS',
            'sortDirection':'DESC'
        })

def main():
    my_client = MyClient(response_handler=JsonResponseHandler)
    json = my_client.get_leader_positions()
    wanted_keys = ['slug', 'title', 'curPrice']
    # The direct answer solution
    new_data = []
    for position in json:
        picked_data = {
            k: position[k] 
            for k in wanted_keys 
            }
        new_data.append(picked_data)
    #json = response.get_json()
    pprint(new_data)

if __name__ == "__main__":
  main()


  

 