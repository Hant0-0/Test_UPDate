import json
import time

from django.core.management import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from api_menu.models import Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        option = Options()
        driver = webdriver.Chrome()
        data_list = []
        driver.get("https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html")
        all_items_menu = driver.find_elements(By.CLASS_NAME, 'cmp-category__item-name')
        for i in range(0, len(all_items_menu)):
            title_menu = all_items_menu[i].text
            time.sleep(1)
            all_items_menu[i].click()
            time.sleep(1)
            desc_dish = driver.find_element(By.XPATH, '//div[@class="cmp-product-details-main__description"]').text
            click_desc = driver.find_element(By.XPATH, '//button[@class="cmp-accordion__button"]').click()
            calories = driver.find_elements(By.XPATH, '//li[@class="cmp-nutrition-summary__heading-primary-item"]')[0].text.split('\n')[0]
            fats = driver.find_elements(By.XPATH, '//li[@class="cmp-nutrition-summary__heading-primary-item"]')[1].text.split('\n')[0]
            carbs = driver.find_elements(By.XPATH, '//li[@class="cmp-nutrition-summary__heading-primary-item"]')[2].text.split('\n')[0]
            proteins = driver.find_elements(By.XPATH, '//li[@class="cmp-nutrition-summary__heading-primary-item"]')[3].text.split('\n')[0]
            next_data = driver.find_elements(By.XPATH, '//li[@class="label-item"]')[0:4]
            unsaturated_fats = next_data[0].text.split('\n')[2]
            sugar = next_data[1].text.split('\n')[2]
            salt = next_data[2].text.split('\n')[2]
            portion = next_data[3].text.split('\n')[2]
            data = {
                "name": title_menu,
                "description": desc_dish,
                "calories": calories,
                "fats": fats,
                "carbs": carbs,
                "proteins": proteins,
                "unsaturated_fats": unsaturated_fats,
                "sugar": sugar,
                "salt": salt,
                "portion": portion,
            }
            get_product = Product.objects.filter(name=title_menu).exists()
            data_list.append(data)
            if get_product:
                Product.objects.filter(name=title_menu).update(
                    name=title_menu,
                    description= desc_dish,
                    calories = calories,
                    fats = fats,
                    carbs = carbs,
                    proteins = proteins,
                    unsaturated_fats = unsaturated_fats,
                    sugar = sugar,
                    salt = salt,
                    portion = portion,
                )
            else:
                Product.objects.create(
                    name=title_menu,
                    description=desc_dish,
                    calories=calories,
                    fats=fats,
                    carbs=carbs,
                    proteins=proteins,
                    unsaturated_fats=unsaturated_fats,
                    sugar=sugar,
                    salt=salt,
                    portion=portion,
                )
            with open('data.json', 'w') as json_file:
                json.dump(data_list, json_file, ensure_ascii=False)

            time.sleep(1)
            driver.get("https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html")
            # Знову знайти всі елементи після перезавантаження сторінки


            all_items_menu = driver.find_elements(By.CLASS_NAME, 'cmp-category__item-name')


        time.sleep(1)