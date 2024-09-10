
import requests as rq


class fetcher:
    def __init__(self):
        self.session = None
        self.headers = {    
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-US,en;q=0.9,fa;q=0.8",
            "Origin": "https://torob.com",
            "Referer": "https://torob.com/",
            "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Linux"',
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }

    def init(self):
        self.session = rq.session()
        self.session.get("https://torob.com/", headers=self.headers)
    
    def get(self, prk, prname):
        url = "https://api.torob.com/v4/base-product/sellers"
        data = {
            "source": "next_desktop",
            "discover_method": "direct",
            "_bt__experiment": "",
            "search_id": "",
            "cities":"",
            "province":"",
            "prk": prk,
            "list_type": "products_info",
            "seed": ""
        }
        resp = self.session.get(url, params=data, headers=self.headers)
        if resp.status_code.__str__()[0] == "2" :
            return resp.json()
        raise Exception(resp)



raw = '''
https://torob.com/p/50179777-6337-4ba1-9f57-024b93367749/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3-156-%D8%A7%DB%8C%D9%86%DA%86%DB%8C-%D9%85%D8%AF%D9%84-tuf-gaming-f15-fx507vi-i7-13620h-16gb-1tb-rtx4070/
https://torob.com/p/ca8acc86-9832-47cb-a34a-1557dc004925/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-835/
https://torob.com/p/307d8a07-2b6f-4bee-8e9a-8ecce182f1fe/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D8%AF%DB%8C%D9%BE%D9%88%DB%8C%D9%86%D8%AA-%D9%85%D8%AF%D9%84-max/
https://torob.com/p/74476fbc-d8fc-4627-82a5-3f12727e6b62/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%AC%D9%86%D8%B1%D8%A7%D9%84-%D9%BE%DB%8C%D9%86-27-%D9%81%D9%88%D8%AA-%D9%85%D8%AF%D9%84-rf-m22/
https://torob.com/p/9c91dd12-bc37-4282-8822-b34884598044/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%88-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%B7%D8%B1%D8%AD-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A7%DB%8C%DA%A9%D8%B3-%D9%88%DB%8C%DA%98%D9%86-%D9%85%D8%AF%D9%84-ts552-awd-%D8%B1%D9%86%DA%AF-%D8%B3%D9%81%DB%8C%D8%AF/
https://torob.com/p/1aa282d3-8e42-4d78-8e16-3fef5413429c/%D8%B3%D8%A7%DB%8C%D8%AF-%D8%A8%D8%A7%DB%8C-%D8%B3%D8%A7%DB%8C%D8%AF-%D8%AF%D9%88%D9%88-ds-3325mw-%D8%B3%D9%81%DB%8C%D8%AF-32-%D9%81%D9%88%D8%AA-%D8%B3%D8%B1%DB%8C-%D9%BE%D8%B1%D8%A7%DB%8C%D9%85-2-%D8%AF%D8%B1%D8%A8/
https://torob.com/p/31a43f04-d2ef-4a81-b4b9-363fc9538f18/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%DA%A9%D9%84%D9%88%D8%B1-%D9%85%D8%AF%D9%84-%D8%B1%D9%88%D8%B3%D9%88-%D9%BE%D9%84%D8%A7%D8%B3-%DB%8C%D8%AE%D8%B3%D8%A7%D8%B2-%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9/
https://torob.com/p/91988a6e-286b-4c70-983c-e02d25117d14/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D8%A7%DB%8C%D8%B3%D8%AA%DA%A9%D9%88%D9%84-%D9%85%D8%AF%D9%84-tm-919-150/
https://torob.com/p/f3bc4073-21ce-4de2-a3f6-512d06949987/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A8%D8%A7%D9%84%D8%A7-%D9%BE%D8%A7%DB%8C%DB%8C%D9%86-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-20-%D9%81%D9%88%D8%AA-_-bfn20d-m-tp-em46/
https://torob.com/p/d660ceff-8220-427c-90ae-10c6fe3a6901/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%A7%D9%85%D8%B1%D8%B3%D8%A7%D9%86-%D9%85%D8%AF%D9%84-tf11t/
https://torob.com/p/99e692a0-d1d6-4c60-960d-c161c4537289/%DB%8C%D8%AE%DA%86%D8%A7%D9%84-%D9%81%D8%B1%DB%8C%D8%B2%D8%B1-%D8%AF%D9%88%D9%82%D9%84%D9%88-%D9%87%DB%8C%D9%85%D8%A7%D9%84%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-%D9%BE%D8%A7%D9%86%D8%A7%D8%B1%D9%88%D9%85%D8%A7-%D9%BE%D9%84%D8%A7%D8%B3-_-%2Bnr440p%2B-nf280p/
'''

import re
import json

f = fetcher()
for _ in range(1):
    for prk, prname in re.findall(r'https://torob.com/p/(.+)/(.+)/', raw):
        f.init()
        try:
            data = f.get(prk, prname)['results']
            data3 = map(lambda d: (d['shop_name'], d['shop_name2']), data)
            data2 = []
            for d in data3:
                if d not in data2:
                    data2.append(d)
                else:
                    print(d[0], ',' ,d[1])
                    input()
            print(data2.__len__(), data.__len__())
        except Exception as e:
            print(f'Error {e.args[0].text}')