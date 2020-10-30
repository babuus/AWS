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
    endpoint='https://xxxxxxxxxxxxxxxxxrtvs4xpji.appsync-api.ap-south-1.amazonaws.com/graphql',
    headers={'x-api-key': 'xxx-xxxxxxxxxxxxxxx3mfaax3m'}
)

result = gq_client.execute(
    query="""
        query MyQuery {
            getallproducttableinfo {
                brand
                category
                code
                collection
                name
                entities
                retailerId
                retailerName
                sku
                dimension {
                    D
                    H
                    W
                    }
                dimensionWithStand {
                    D
                    H
                    W
                    }
                productAttributes {
                    value
                    key
                    }
                }
            }

""", 
    operation_name='MyQuery'
)
print(result)