import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add the driver options
options = uc.ChromeOptions() 
options.headless = False

# Configure the undetected_chromedriver options
driver = uc.Chrome(options=options) 

i = 100 
cookies = 1

while i!=0:

    with driver:
    # Go to the target website
        driver.get("https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&category_730_Weapon%5B%5D=any&appid=730&q=case#p1_default_desc")
    time.sleep(2)
    name = driver.find_elements(By.CLASS_NAME, "market_listing_item_name")
    price = driver.find_elements(By.CSS_SELECTOR, "[data-price]")
        
    for x in range(len(name)):
        print(name[x].text, price[x].text)
    print("__________%s____________"% i)

    # if driver.find_element(By.ID, "acceptAllButton"):
    #     while driver.find_elements(By.ID, "acceptAllButton"):
    #         driver.find_element(By.ID, "acceptAllButton").click()
    # popup = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "acceptAllButton"))
    # )
    # if popup:
    #     driver.find_element(By.ID, "acceptAllButton").click()
    while driver.find_elements(By.CLASS_NAME, "disabled") != driver.find_elements(By.ID, "searchResults_btn_next") and driver.find_elements(By.ID, "searchResults_btn_next"):
        if cookies == 1:
            print(len(driver.find_elements(By.ID, "acceptAllButton")) == 1)
            driver.find_element(By.ID, "acceptAllButton").click()
            cookies = 0
        time.sleep(2)
        driver.find_element(By.ID, "searchResults_btn_next").click()
        time.sleep(2)
        name = driver.find_elements(By.CLASS_NAME, "market_listing_item_name")
        price = driver.find_elements(By.CSS_SELECTOR, "[data-price]")
            
        for x in range(len(name)):
            print(name[x].text, price[x].text)
        print("__________%s____________"% i)

    i = i-1

driver.quit()
# next = driver.find_element(By.ID, "searchResults_btn_next")
# name = driver.find_elements(By.CLASS_NAME, "market_listing_item_name")
# price = driver.find_elements(By.CLASS_NAME, "normal_price")
        
# for x in range(len(name)):
#     print(name[x].text, price[x].text)
# Close the browsers

