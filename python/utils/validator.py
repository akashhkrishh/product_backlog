
import re
from datetime import datetime

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

def validate_card_number(card_number: str) -> bool:
    # Check if card number is exactly 16 digits
    return bool(re.fullmatch(r'\d{16}', card_number))

def validate_card_holder_name(name: str) -> bool:
    # Minimum 10 characters (allow letters, spaces, dots)
    return bool(re.fullmatch(r'[A-Za-z\s\.]{10,}', name.strip()))

def validate_expiry_date(expiry: str) -> bool:
    # Format MM/YY and expiry date should not be in the past
    if not re.fullmatch(r'(0[1-9]|1[0-2])/(\d{2})', expiry):
        return False
    try:
        exp_month, exp_year = expiry.split('/')
        exp_month = int(exp_month)
        exp_year = int(exp_year)
        # Convert 2-digit year to 4-digit (assume 2000+)
        current_year = datetime.now().year % 100
        current_month = datetime.now().month

        # Expiry year in full
        full_exp_year = 2000 + exp_year

        # Card expiry is the last day of the month
        exp_date = datetime(full_exp_year, exp_month, 1)
        # Check if expiry is in future (month/year)
        if (exp_year > current_year) or (exp_year == current_year and exp_month >= current_month):
            return True
        return False
    except Exception:
        return False

def validate_cvv(cvv: str) -> bool:
    # Exactly 3 digits
    return bool(re.fullmatch(r'\d{3}', cvv))
