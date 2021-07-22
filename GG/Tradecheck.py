from steampy.client import SteamClient

steam_client = SteamClient('E478B2112F2DFD1C242B22C5E6739C6F')
params = {'key': 'E478B2112F2DFD1C242B22C5E6739C6F'}
summaries =  steam_client.api_call('GET', 'IEconService', 'GetTradeOffersSummary', 'v1', params).json()
print(summaries)
