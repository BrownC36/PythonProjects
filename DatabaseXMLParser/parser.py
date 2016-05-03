import datetime
import locale
import sys
import xml.dom.minidom

dom = xml.dom.minidom.parse("items-0.xml")
node = dom.documentElement
items = dom.getElementsByTagName("Item")

f = open("sqlitedata.dat", "w")

for item in items:
    name = item.getElementsByTagName("Name")[0].childNodes[0].data
    categories = item.getElementsByTagName("Category")
    currently = item.getElementsByTagName("Currently")[0].childNodes[0].data
    firstBid = item.getElementsByTagName("First_Bid")[0].childNodes[0].data
    numberOfBids = item.getElementsByTagName("Number_of_Bids")[0].childNodes[0].data
    bids = item.getElementsByTagName("Bids")
    location = item.getElementsByTagName("Location")[0].childNodes[0].data
    country = item.getElementsByTagName("Country")[0].childNodes[0].data
    started = item.getElementsByTagName("Started")[0].childNodes[0].data
    ends = item.getElementsByTagName("Ends")[0].childNodes[0].data
    seller = item.getElementsByTagName("Seller")[0]
    sellerID = seller.attributes["UserID"].value
    sellerRating = seller.attributes["Rating"].value
    description = item.getElementsByTagName("Description")[0]
    if len(description.childNodes) > 0:
        des = description.childNodes[0].data
        
    f.write("Name: " + name + "\n")
    for category in categories:
        cat = category.firstChild.data
        f.write("Category: " + cat + "\n")
    f.write("Description: " + des + "\n")
        
    f.write("Currently: " + currently + "\n")
    f.write("First Bid: " + firstBid + "\n")
    f.write("Number of Bids: " + numberOfBids + "\n")
    f.write("Location: " + location + "\n")
    f.write("Country: " + country + "\n")
    f.write("Started: " + started + "\n")
    f.write("Ends: " + ends + "\n")
    f.write("Seller ID: " + sellerID + " Seller Rating: " + sellerRating + "\n")
    
    

    for bidTag in bids:
        bid = bidTag.getElementsByTagName("Bid")
        for attri in bid:
            f.write("******BID INFORMATION********\n")
            bidList = attri.getElementsByTagName("Bidder")[0]
            location = attri.getElementsByTagName("Location")
            country = attri.getElementsByTagName("Country")
            bidder = bidList.attributes['UserID'].value
            rating = bidList.attributes["Rating"].value
            time = attri.getElementsByTagName("Time")[0].childNodes[0].data
            amount = attri.getElementsByTagName("Amount")[0].childNodes[0].data
            f.write("Bidder: " + bidder + " Rating: " + rating + "\n")
            if len(location) > 0:
                f.write("Location: " + location[0].childNodes[0].data + "\n")
            if len(country) > 0:
                f.write("Country: " + country[0].childNodes[0].data + "\n")
            f.write("Time: " + time + "\n")
            f.write("Amount: " + amount + "\n")
            f.write("*****************************\n")
    
    f.write("\n")


f.close()
