import shodan
api = shodan.Shodan("QsLloESzY3u7gCtCtxv0irZZyCbQayZN")
results = api.search('cisco')
for result in results['matches']:
    iplist = result['ip_str']+":"+ str(result['port'])
    print(iplist)