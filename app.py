# get all_email_addresses from file
all_email_addresses = ["test.email@gmail.com", "test.email@gmail.com", "test.email+alex@gmail.com"]

unique_email_addresses = []

for email in all_email_addresses:
    if email not in unique_email_addresses:
        unique_email_addresses.append(email)

# save unique_email_addresses to file called "unique_email_addresses.txt"
print(unique_email_addresses)