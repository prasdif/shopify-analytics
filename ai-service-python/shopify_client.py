class ShopifyClient:
    def __init__(self):
        pass

    def execute(self, store_id: str, query: str):
        """
        Executes a ShopifyQL query against the store API.
        In this demo, we return mock data based on the query type.
        """
        print(f"Executing Query against {store_id}: {query}")
        
        # Mock responses
        if "inventory" in query.lower() or "products" in query.lower():
            return [
                {"title": "T-Shirt", "inventory_quantity": 5, "sales_velocity": 2.5},
                {"title": "Jeans", "inventory_quantity": 2, "sales_velocity": 1.0},
                {"title": "Sneakers", "inventory_quantity": 0, "sales_velocity": 3.0},
            ]
        
        if "orders" in query.lower():
            return [
                {"order_id": 101, "amount": 50.00},
                {"order_id": 102, "amount": 120.00},
                {"order_id": 103, "amount": 35.00},
            ]
            
        return []
