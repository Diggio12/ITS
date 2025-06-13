def is_valid_ipv4(address: str) -> bool:

    parts_address: list[str] = address.split('.')

    if len(parts_address) > 4 or len(parts_address) < 4:
        return False
    
    for part in parts_address:
        
        if part.isdigit() == False:
            return False
        
        elif not 0 <= int(part) <= 255:
            return False
        
        
    return True

is_valid_ipv4("192.168.0.1")
is_valid_ipv4("255.255.255.255")
is_valid_ipv4("256.100.10.1")
is_valid_ipv4("192.168.1")
is_valid_ipv4("192.168.1.a")