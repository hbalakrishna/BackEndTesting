import pymysql

class DBConnect():

    def __init__(self):
        pass

    #private class
    def __conect(self,db): #pass in the database which needs to be connected
        host = '127.0.0.1'
        conn = pymysql.connect(host=host, port=3306,user='root',db=db,password='mysql')

        return conn

    def select(self,db,query):
        conn = self.__conect(db)
        #create a cursor
        cur = conn.cursor()
        #execute the query
        cur.execute(query)
        #Fetch all the results
        result = cur.fetchall()

        result_set = [] #create a result for all the rows & columns
        for line in result:
            row = []
            for col in line:
                row.append(str(col))
            result_set.append(row)

        #Close the connection & the cursor
        conn.close()
        cur.close()

        return result_set

    def update(self,db,query):
        conn = self.__conect(db)
        #create a cursor
        cur = conn.cursor()
        #execute the query
        result = cur.execute(query)

        #commit the changes to the database
        conn.commit()

        #close the connection & the cursor
        conn.close()
        cur.close()

        # return the result
        return result


