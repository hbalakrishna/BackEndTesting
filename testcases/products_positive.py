import json

from tools import req
from tools import dbconnect

request = req.REQ()
mysql_conn = dbconnect.DBConnect()

def test_post_product():

    #Create a global variable for product_id
    global product_id
    global data

    data = {
        "name": "NewProduct2",
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
    product_id = resp_body["id"]


    #Assert the response body
    assert return_name==data["name"], "Mismatch in title: The name of the product" \
                                      " in the response body & posted name do not match, expected name is {0}" \
                                      " the response name is {1}".format(data["name"], return_name)

    assert return_price==data["regular_price"], "Mismatch in regular_price: The price of the product" \
                                      " in the response body & posted name do not match, expected price is {0} " \
                                                "the return price is {1}".format(data["regular_price"], return_price)


    print("all the assertions are passed")
    # print("Product ID {0}".format(product_id))


#Testing the product in the database after the post request
def testProduct_db():

    #MySQL query to fetch the the product name, type & price for the product posted

    mysql_query = '''
                    select posts.post_name,posts.post_type,postm.meta_value
                    from wp324.wp5b_posts as  posts 
                    JOIN wp324.wp5b_postmeta  as postm
                    ON posts.id = postm.post_id
                    where posts.id={} and meta_key = '_regular_price'
    '''.format(product_id)

    result = mysql_conn.select('wp324',mysql_query)

    #extract the values for the data posted in the database & verify them
    db_title = result[0][0]
    db_type = result[0][1]
    db_price = result[0][2]

    #Assert them
    # Assert the response body
    assert db_title == data["name"].lower(), "Mismatch in title: The name of the product" \
                                        " in the response body & posted name do not match, expected name is {0}" \
                                        " the response name is {1}".format(data["name"].lower(), db_title)

    assert db_price == data["regular_price"], "Mismatch in regular_price: The price of the product" \
                                                  " in the response body & posted name do not match, expected price is {0} " \
                                                  "the return price is {1}".format(data["regular_price"], db_price)


    # print(result)
    print("Products positive test case, the products created have been verified in the database")




test_post_product()
testProduct_db()