#python3
#count Starbucks location in each area in Bangkok
#note: need to use postcode because Starbucks use different spelling on the same district
#note2: search store by using postcode because Starbucks website don't show all stores when search by large area (eg. Bangkok)

from selenium import webdriver
import csv,time

output_csv = open("count_store_result.csv", "w", newline="")
count_csv = csv.writer(output_csv)

url_start = "http://www.starbucks.co.th/store-locator/search/location/"
url_end = "%2C%20Thailand"

postcodes = open('postcode.txt').read().split(",")
for postcode in postcodes:  #loop through each postcode
    web_url = "".join([url_start,str(postcode),url_end])
    count = 0
    browser = webdriver.Firefox()
    browser.get(web_url)
    stores = browser.find_elements_by_class_name("result")
    for store in stores:
        store_txt = store.text
        if postcode in store_txt:
            count+=1
    count_csv.writerow([str(postcode),count])
    time.sleep(5)
output_csv.close()
