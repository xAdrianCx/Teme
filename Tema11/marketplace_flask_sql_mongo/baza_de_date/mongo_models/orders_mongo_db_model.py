
class OrdersMongoDBModel:

    _id = None
    order_name = None
    order_quantity = None
    data_inregistrare = None

    def __init__(self, **fields):
        self._id = fields.get("id_comanda", None)
        self.order_name = fields["order_name"]
        self.order_quantity = fields["order_quantity"]
        self.data_inregistrare = fields.get("data_inregistrare")
