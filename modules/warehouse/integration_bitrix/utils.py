def format_bitrix_deal(deal):
    return (
        f"Deal {deal['ID']} | "
        f"Title: {deal['TITLE']} | "
        f"Stage: {deal['STAGE_ID']}"
    )
