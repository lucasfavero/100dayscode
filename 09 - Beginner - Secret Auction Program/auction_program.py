import art

print("Welcome to the secret auction program!")

loop = True
client_dict = {}
print(art.logo)

while loop:

    client_name = input("What's your name?: ")
    client_bid = int(input("What's your bid?: "))
    client_dict[client_name] = client_bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if other_bidders == "no":
        loop = False


client_max_bid = max(client_dict, key=lambda x: client_dict[x])

print(f"The winner of tge auction is: {client_max_bid}")

