from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        options = Options()
        options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
        self.driver = webdriver.Firefox(executable_path="/Users/denilsoncarvalhodacosta/Desktop/geckodriver", firefox_options=options)

    def login(self):
            driver = self.driver
            driver.get("https://instagram.com")
            time.sleep(3)
            campo_usuario = driver.find_element_by_xpath("//input[contains(@name,'username')]")
            campo_usuario.click()
            campo_usuario.clear()
            campo_usuario.send_keys(self.username)
            campo_senha = driver.find_element_by_xpath("//input[@name='password']")
            campo_senha.click()
            campo_senha.clear()
            campo_senha.send_keys(self.password)
            time.sleep(1)
            driver.find_element_by_xpath("//button[contains(.,'Entrar')]").click()
            time.sleep(3)
            # campo_senha.send_keys(Keys.RETURN)
            self.coments_on_photos('kerenfernandes__')

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def open_first_picture(self):
        print("entrou na primeira foto")
        try:             
            self.driver.find_element_by_class_name("kIKUG").click()
        except Exception as e:
            print("Profile has no picture")         


    def coments_on_photos(self,pagina):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ pagina +"/")
        time.sleep(3)

        # for i in range(1,3):
        #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     time.sleep(5)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if pagina in href]
        print(pagina + 'fotos ' + str(len(pic_hrefs)))
        self.open_first_picture()


        for pic_href in pic_hrefs:
            print('testeeee ' + pic_href)
            next_button = "//a[text()=\"Próximo\"]"
            self.driver.find_element_by_xpath(next_button).click()
            time.sleep(3)
            # driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                comentarios = ["Te amo!","Minha princesa, te amo!", "Minha lindeza, te amo!", "Minha gata!" "Meu baby, te amo!","Minha neguinha, te amo!"]
                # comentarios = ["Teste"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.digite_como_uma_pessoa(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(10,15))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)




denilsonBot = InstagramBot('melhora.continua','')
denilsonBot.login()

