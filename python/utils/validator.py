import re

def validate_name(name: str) -> bool:
    return bool(re.search(r'^.{3,50}$', name))

def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_mobile(mobile: str) -> bool:
    return bool(re.fullmatch(r"\d{10}", mobile))

def validate_address(address: str) -> bool:
    return len(address.strip()) <= 300

def validate_password(password: str) -> bool:
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_alpha = re.search(r'[a-zA-Z]', password)
    return bool(has_lower and has_upper and has_alpha)

def validate_confirm_password(password: str, confirm_password: str) -> bool:
    return password == confirm_password
