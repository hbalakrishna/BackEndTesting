from woocommerce import API

class REQ():

    def __init__(self):
        admin_consumer_key = "ck_82f82456dfe3b95b2b9dc83c56411bb5277807bd"
        admin_consumer_secret = "cs_5af4b6bdfef28ce5337d6a189ef342eb8545079e"

        self.wcapi = API(
            url="http://127.0.0.1/hbstore/",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            wp_api=True,
            version="wc/v1"

        )

    def testAPI(self):
        print(self.wcapi.get("").json())

    def post(self,endpoint,data):
        result = self.wcapi.post(endpoint,data)
        res_code = result.status_code
        res_body = result.json()
        res_url = result.url

        return [res_code, res_body, res_url]

    def get(self,endpoint):
        result = self.wcapi.get(endpoint)
        res_code = result.response_code
        res_body = result.json()
        res_url = result.url

        return [res_code, res_body, res_url]



#
# obj = REQ()
# obj.testAPI()