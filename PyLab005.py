part_input = (input("Enter IP address excerpt: "))


def is_valid_part(part):
    part_str = str(part)
    if part_str[0] == '0' and len(part_str) > 1:
        return False
    elif 0 <= int(part) <= 255:
        return True
    else:
        return False

print(is_valid_part(part_input))

ip_input = input("Enter a full IP address: ")

def is_valid_ip(ip):
    ip_parts = ip.split('.')
    if len(ip_parts) != 4:
        return False

    for part in ip_parts:
        if not is_valid_part(part):
            return False

    return True
print(is_valid_ip(ip_input))