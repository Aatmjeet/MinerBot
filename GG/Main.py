from steampy.client import SteamClient

steam_client = SteamClient('E478B2112F2DFD1C242B22C5E6739C6F')
steam_client.login('caseXchangeBot','7a82d317@', 'Steamguard.txt')
#api_key = 'E478B2112F2DFD1C242B22C5E6739C6F'
#username = 'caseXchangeBot'
#password = '7a82d317@'
#steamguard_path = './Steamguard.txt'
is_session_alive = steam_client.is_session_alive()


'''def main():
    print('This is the donation bot accepting items for free.')
    if not are_credentials_filled():
        print('You have to fill credentials in storehouse.py file to run the example')
        print('Terminating bot')
        return
    client = SteamClient(api_key)
    client.login(username, password, steamguard_path)
    print('Bot logged in successfully, fetching offers every 60 seconds')
    while True:
        offers = client.get_trade_offers()['response']['trade_offers_received']
        for offer in offers:
            if is_donation(offer):
                offer_id = offer['tradeofferid']
                num_accepted_items = len(offer['items_to_receive'])
                client.accept_trade_offer(offer_id)
                print('Accepted trade offer {}. Got {} items'.format(offer_id, num_accepted_items))
        time.sleep(60)


def are_credentials_filled() -> bool:
    return api_key != '' and steamguard_path != '' and username != '' and password != ''


def is_donation(offer: dict) -> bool:
    return offer.get('items_to_receive') \
           and not offer.get('items_to_give') \
           and offer['trade_offer_state'] == TradeOfferState.Active \
           and not offer['is_our_offer']


if __name__ == "__main__":
    main()'''
