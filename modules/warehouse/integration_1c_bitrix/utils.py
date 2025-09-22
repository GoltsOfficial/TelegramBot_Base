def merge_order_data(onec_order, bitrix_deal):
    return {
        "id": onec_order["id"],
        "customer": onec_order["customer"],
        "total": onec_order["total"],
        "bitrix_title": bitrix_deal.get("TITLE")
    }
