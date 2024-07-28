import sys
sys.path.append("../../")
from libraries.libraries import *

payload = {
    "endpoint": "https://alimexmy.tulip.co/login?redirect=%2Fprofile",
    "email": "malcolm@alimex.com.my",
    "password": "@Alimex2016",
    "workorderhistory": "https://alimexmy.tulip.co/tables",
    'tableLink':'https://alimexmy.tulip.co/table/Q64ewaqgPB2yfNjGS?sortOptions=%5B%7B%22sortBy%22%3A%22id%22%2C%22sortDir%22%3A%22desc%22%7D%5D&offset='
}



class tulipFetch():
    def __init__(self):
        pass
    def errorHandling(self):
        prompts = {
            "success": "Data Syncronized Successfully",
            "endpointError": "Endpoint URL incorrect",
            "loginElementError": "Login Elements not Found, Rerun payload",
            "renavigationError": "Bad URL or XPATH for WorkOrder History",
            "sortingError": "Bad XPATH for ID Filter"
        }
        return prompts
    def dataPush(self):
        pass
    def recordFetch(self):
        pass
    def pagination(self):
        def pageNavigation(last_page):
            for n in range(1, last_page):
                offset = (n-1) * 50
                page_url = payload["tableLink"] + str(offset)
                self.driver.execute_script(f"window.location.href='{page_url}'")
                self.recordFetch()
                time.sleep(1)
        while True:
            try:
                pagination_controls = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="pagination-controls"]')
                next_button = pagination_controls.find_elements(By.TAG_NAME, "button")[-1]
                if "See more pages" in next_button.get_attribute("aria-label"):
                    time.sleep(1)
                    next_button.click()
                    time.sleep(1)
                else:
                    final_page = int(next_button.get_attribute("aria-label").split("e ")[1])
                    last_page = final_page
                    pageNavigation(last_page)
                    break
            except:
                pass
    def dataFetch(self, endpoint, email, password):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        try:
            self.driver.get(endpoint)
            try:
                self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-username"]').send_keys(email)
                self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-password"]').send_keys(password)
                self.driver.find_element(By.CSS_SELECTOR, '[data-testid="login-submit"]').click()
                time.sleep(1)
                try:
                    self.driver.execute_script(f"window.location.href='{payload['workorderhistory']}';")
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '//*[@id="tables-overview-table-Q64ewaqgPB2yfNjGS"]').click()
                    time.sleep(1)
                    try:
                        time.sleep(1)
                        self.driver.find_element(By.XPATH, '//*[@id="tulip-root"]/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/button').click()
                        time.sleep(1)
                        self.driver.find_element(By.XPATH, '/html/body/div[13]/div/ul/li[5]/button').click()
                        time.sleep(3)
                        self.pagination()
                        self.driver.quit()
                    except:
                        response = tulipFetch().errorHandling()
                        self.driver.quit()
                        return response["sortingError"]
                except:
                    response = tulipFetch().errorHandling()
                    self.driver.quit()
                    return response["renavigationError"]
            except:
                response = tulipFetch().errorHandling()
                self.driver.quit()
                return response["loginElementError"]
        except: 
            response = tulipFetch().errorHandling()
            self.driver.quit()
            return response["endpointError"] 
    def processValidation(self, email, password):
        self.dataFetch(payload["endpoint"], email, password)
        response = self.errorHandling()
        return response["success"]

result = tulipFetch().processValidation(payload["email"], payload["password"])
print(result)