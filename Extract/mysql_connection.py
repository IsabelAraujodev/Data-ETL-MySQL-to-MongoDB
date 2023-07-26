from sqlalchemy import create_engine

class MySQLConnection: 
    def __init__(self, user, passwd = None, host = 'localhost', port = 3306, database = None):
        """Initialize a connection of the class with the MySQL database

        Args:
            user: database user
            passwd: a password if exist one
            host: localhost, ip or domain of destiny
            port: default port 3306
            database: the database who be accessed
        """
        self.user = user
        self.passwd = passwd
        self.database = database
        self.host = host
        self.port = port
        self.engine = None

    def set_mysql_engine(self):

        connection_string = ''.join(['mysql+pymysql://', self.user, ':', self.passwd, '@',
                                     self.host, ':', str(self.port), '/', self.database])
        #'mysql://user:passwd@host:port/database'
        self.engine = create_engine(connection_string)
        try:
            self.engine.connect()
        except ConnectionError():
            raise 'Error During the connection'
        

    QUERY = query = (
        "SELECT o.order as 'id_order', \
               c.customerNumber as 'id_customer',\
               o.orderDate as 'orderDate',\
               o.status, \
               p.productsCode as 'id_product'\
               p.productName as 'name',\
               p.productLine as 'category',\
               od.quantityOrdered as 'quantity',\
               od.priceEach as 'price',\
               c.city,\
               c.state,\
               c.country,\
            FROM orders o\
                INNER JOIN orderdetails ON o.orderNumber = od.orderNumber\
                INNER JOIN prodducts p ON od.productCode = p.productCode\
                INNER JOIN customers c ON c.customerNumber = o.customerNumber\
            ORDER BY o.orderNumber;"\
    )