import random

def create_fake_ip():
    first_octet = str(random.randint(10, 172))
    if first_octet == '172':
        second_octet = str(random.randint(16, 31))
    else:
        second_octet = str(random.randint(0, 255))

    third_octet = str(random.randint(0, 255))
    fourth_octet = str(random.randint(0, 255))

    return '.'.join([first_octet, second_octet, third_octet, fourth_octet])

fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
fake_ip = create_fake_ip()
print(f"The fake IP address is: {fake_ip}")
input('Here your fake ip!')
