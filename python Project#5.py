import os
def find_winner(bidders_details):
    highest_bid=0
    winner=""
    for bidder in bidders_details:
       bidding_price=bidders_details[bidder]
    if bidding_price>highest_bid:
        highest_bid=bidding_price
        winner=bidder
        print(f"The winner is {winner} with the bit of {highest_bid}")

end_of_bidding=False

while not end_of_bidding:
       bidders_data={}
       name=input("What is your name?")
       price=int(input("What is your bit?"))
       bidders_data[name]=price

       more_bidders=input("Are there is more bidders? Type 'yes' or 'no' : ").lower()

       if more_bidders=='no':
          end_of_bidding=True
          find_winner(bidders_data)
       elif more_bidders=='yes':
           os.system('cls')
