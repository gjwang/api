import json

from py.betaex_client import BetaexApiKeyClient

API_BASE_URL = ''
API_KEY = ''
API_SECRET = ''


betaexClient = BetaexApiKeyClient(API_BASE_URL, API_KEY, API_SECRET)

# 查询余额列表
ret = betaexClient.list_balance()
result = json.loads(ret.text)
print(result)
