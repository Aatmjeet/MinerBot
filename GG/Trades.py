from steampy.client import SteamClient, Asset
from steampy.utils import GameOptions

steam_client = SteamClient('MY_API_KEY')
steam_client.login('MY_USERNAME', 'MY_PASSWORD', 'PATH_TO_STEAMGUARD_FILE')
partner_id = 'PARTNER_ID'
game = GameOptions.CS
my_items = steam_client.get_my_inventory(game)
partner_items = steam_client.get_partner_inventory(partner_id, game)
my_first_item = next(iter(my_items.values()))
partner_first_item = next(iter(partner_items.values()))
my_asset = Asset(my_first_item['id'], game)
partner_asset = Asset(partner_first_item['id'], game)
steam_client.make_offer([my_asset], [partner_asset], partner_id, 'Test offer')
