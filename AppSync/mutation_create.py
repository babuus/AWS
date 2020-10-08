from urllib import request
from datetime import datetime
import simplejson


class GraphqlClient:

    def __init__(self, endpoint, headers):
        self.endpoint = endpoint
        self.headers = headers

    @staticmethod
    def serialization_helper(o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S.000Z')

    def execute(self, query, operation_name, variables={}):
        data = simplejson.dumps({
            "query": query,
            "variables": variables,
            "operationName": operation_name
        },
            default=self.serialization_helper,
            ignore_nan=True
        )
        r = request.Request(
            headers=self.headers,
            url=self.endpoint,
            method='POST',
            data=data.encode('utf8')
        )
        response = request.urlopen(r).read()
        return response.decode('utf8')

gq_client = GraphqlClient(
    endpoint='https://xxxxxxxxxxxxxxrtvs4xpji.appsync-api.ap-south-1.amazonaws.com/graphql',
    headers={'x-api-key': 'xxx-xxxxxxxxxxxxxxxxxxmfaax3m'}
)

var = {
  "codee": {
    "code": 55313,
    "brand": "LOGIK",
    "category": "Fridge freezers",
    "collection": "",
    "entities": [{"name": "Bixby"},{"name":"Ace Pro Ultra"}],
    "productAttributes": {"key": "dd","value": "je"}
  }
}

result = gq_client.execute(
    query="""

mutation MyQuery($codee: CreateProductTableInput!) {
  InsertProductTable(input: $codee) {
    code
    brand
    entities {
      name
    }
    productAttributes {
      key
      value
    }
    collection
    category
    sku
  }
}


""", 
    operation_name='MyQuery',
    variables=var
)
print(result)