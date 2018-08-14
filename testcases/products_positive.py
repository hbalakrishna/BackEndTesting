import json

from tools import req
from tools import dbconnect

request = req.REQ()

def post_product():

    #a simple payload
    #title = 'TEST1 TITLE'
    #price = "99.9"

    data = {
        "name": "Test1 Title",
        "type": "simple",
        "regular_price": "21.99",
        "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
        "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",


    }

    result = request.post('products',data)
    return_code = result[0]
    resp_body = result[1]

    #Assert the 201 return code
    assert return_code==201,"The status code returned creating product is not as expected. " \
                            "Expected: 201, Actual: {act}".format(act=return_code)

    #Verify the response body
    return_name = resp_body["name"]
    return_price = resp_body["regular_price"]
    return_id = resp_body["id"]

    #Assert the response body
    assert return_name==data["name"], "Mismatch in title: The name of the product" \
                                      " in the response body & posted name do not match, expected name is {0}" \
                                      " the response name is {1}".format(data["name"], return_name)

    assert return_price==data["regular_price"], "Mismatch in regular_price: The price of the product" \
                                      " in the response body & posted name do not match, expected price is {0} " \
                                                "the return price is {1}".format(data["regular_price"], return_price)


    print("all the assertions are passed")




post_product()