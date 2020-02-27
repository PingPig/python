import shodan
api = shodan.Shodan("xxxxxxx")
results = api.search('cisco')
for result in results['matches']:
    iplist = result['ip_str']+":"+ str(result['port'])
    print(iplist)
