from time import strftime, mktime, strptime

from model.Advertiser import Advertiser
from model.Buyer import Buyer

# generate 10 advertisers
from model.Daypart import Daypart

adverts = list()

for i in range(1, 11):
    advert = Advertiser()
    advert.id = i
    advert.name = "advert" + i.__str__()
    adverts.append(advert)

# for advert in adverts:
#     print advert.name

# generate 10 buyers
buyers = list()

for i in range(1, 11):
    buyer = Buyer()
    buyer.id = i
    buyer.name = "buyer" + i.__str__()
    buyers.append(buyer)

# for buyer in buyers:
#     print buyer.name

# generate dayparts
dayparts = Daypart.generate_dayparts()

for daypart in dayparts:
    print strftime("%H:%M", daypart.start_time)

for daypart in dayparts:
    print strftime("%H:%M", daypart.start_time)
