import re

uk_postcode = re.compile(r'\b(?:[A-Z]|[A-Z]{2})(?:\d|\d{2})[A-Z]? \d[A-Z]{2}\b')
uk_vehicle_reg = re.compile(r'\b[A-Z]{2}\d{2} ?[A-Z]{3}\b')