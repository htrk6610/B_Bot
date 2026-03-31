def is_allowed_phone(phone: str) -> bool:
    phone = phone.replace(" ", "").replace("-", "")

    if phone.startswith("+"):
        phone = phone[1:]

    return phone.startswith("380")