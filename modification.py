from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

class searchTest:
    def __init__(self, artisName):
        self.artist = artisName
        
    def test_googleSearch(self):

        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get('https://www.topticketshop.nl/')

        box = driver.find_element_by_css_selector('button.modal-close')
        time.sleep(3)
        box.click()

        clickText = driver.find_element_by_class_name('search-text')
        clickText.click()
        time.sleep(5)
                
        search = driver.find_element_by_id('ttsglobalsearchinput')
        search.send_keys(self.artist)
        search.send_keys(Keys.RETURN)
        time.sleep(5)

        button = driver.find_element_by_class_name('btn-alt')
        print(button.text)
        button.click()
        time.sleep(10)

        buttonAccesstickets = driver.find_element_by_xpath("//div[@id='event-list']//ul[@id='artiestshedulelist']//li[1]//div[@class='btn-holder']//a[@class='btn-alt']")
        print(buttonAccesstickets.text)
        buttonAccesstickets.click()
        time.sleep(5)

        dates=[]
        ArtisName=[]
        pricestickest=[]
        typeofTicket=[]
        priceofTickets=[]

        date = driver.find_element_by_xpath("//div[@class='text']//strong[@class='event-time-loc no-mobile']")
        dates.append(date.text)

        nameArtist = driver.find_element_by_xpath("//div[@class='text']//h1[@class='artevent-artiest']")
        ArtisName.append(nameArtist.text)

        priceTicket = driver.find_element_by_xpath("//div[@class='text']//div[@id='info']//p//span[@class='fvsCls']")
        pricestickest.append(priceTicket.text)

        Tickettype = driver.find_element_by_xpath("//div[@class='tickets-area']//form[@id='eventTicketsForm']//div[@class='choosequantity']//button[1]")
        Tickettype.click()
        time.sleep(3)


        ticketPrice = driver.find_element_by_xpath("//div[@class='ajax-holder']//ul[@class='ticket-list']//div[@class='btn-holder popup-opener-btn']//strong[@class='price']")
        pricestickest.append(ticketPrice.text)

        #listIterate= driver.find_element_by_xpath("//ul[@class='ticket-list']")

        ticketType = driver.find_element_by_xpath("//div[@class='descr popup-opener-descr']//h2//a[@class='popup-opener']")
        typeofTicket.append(ticketType.text)

        price = driver.find_element_by_xpath("//div[@class='ajax-holder']//ul[@class='ticket-list']//div[@class='btn-holder popup-opener-btn']//strong[@class='price']")
        priceofTickets.append(price.text)

        driver.quit()

        header = ['name Artist', 'Date and Location', 'aproxim price', 'Type of tickets', 'Final price']
        data = [ArtisName[0], dates[0], pricestickest[0], typeofTicket[0], priceofTickets[0]]

        with open('ConcertInfo.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

artist= searchTest("SEVN ALIAS")
artist.test_googleSearch()