# Will be leaving myself extensive notes, so this will be verbose
# Some info on importing web pages here: https://stackoverflow.com/questions/40879856/how-do-i-get-the-html-of-a-website-using-python-3
# Other info from another repo for getting data from AEMO here: https://github.com/KaigeWang/web-scraping/blob/master/src/module/webclient.java 
# This older repo seems to have some info as well: https://github.com/hsenot/aemo-json
# This code definitely looks like it may be useful: https://github.com/hsenot/aemo-json/blob/master/script/extract-demand-price-30mn.py 

import urllib.request

#set the URL

#target_url = "https://tomcc.com.au/triumph-motorcycle-history/" #hitting a site I control for now
#target_url = "https://aemo.com.au/aemo/apps/visualisation/index.html#/electricity/nem/dispatch-overview?Elec_enabled=Yes&Gas_enabled=No&Elec_location=NSW,QLD,SA&Gas_location=TAS,VIC,WA" #AEMO website
#target_url = "https://aemo.com.au/aemo/apps/visualisation/index.html#/electricity/nem/dispatch-overview" #AEMO website
target_url = "http://www.nemweb.com.au/mms.GRAPHS/GRAPHS/GRAPH_30VIC1.csv" #This outputs a CSV file with previous 30 min and predictions moving forward.  From https://github.com/hsenot/aemo-json

source = urllib.request.urlopen(target_url).read()

# now I need to get the last one with "TRADE" in the column, looks like row 50 (first with PD in it) is the next predicted price for next half hour

print(source)


