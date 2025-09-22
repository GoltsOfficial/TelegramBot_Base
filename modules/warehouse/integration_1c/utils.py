def format_1c_order(order):
    return (
        f"Order {order['id']} | "
        f"Customer: {order['customer']} | "
        f"Total: {order['total']} ₽"
    )
