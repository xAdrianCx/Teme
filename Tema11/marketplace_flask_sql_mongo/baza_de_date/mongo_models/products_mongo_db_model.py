
class ProductsMongoDBModel:

    _id = None
    product = None
    price = None
    data_inregistare = None

    def __init__(self, **fields):
        self._id = fields.get("id_produs")
        self.product = fields["product"]
        self.price = fields["price"]
        self.data_inregistare = fields.get("data_inregistrare", None)
        