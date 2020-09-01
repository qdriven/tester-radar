import requests
from selenium.webdriver.support.select import Select


class Translator:

    def translate(self, from_text, lan="CH"):
        raise NotImplementedError("abstraction class without any implementation")


class BingTranslator(Translator):

    def __init__(self, url="https://cn.bing.com/translator/"):
        self.url = url

    def translate(self, text, from_lan="en", to_lan="zh-CHS"):
        url = "https://cn.bing.com/ttranslate?&" \
              "category=&IG=4087582A95EF496C879C525D9693B51E" \
              "&IID=translator.5038.3"
        form_data = {
            "text": text,
            "from": from_lan,
            "to": to_lan
        }
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "credentials": "include",
            "referrerPolicy": "origin-when-cross-origin",
            "mode": "cors",
            "user-agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.post(url, data=form_data, headers=headers)
        print(response.text)
        translation_result = response.json()
        return translation_result['translationResponse']

    def get_apis(self):
        response = requests.get(self.url)
        print(response)
        return response.content


if __name__ == '__main__':
    translator = BingTranslator()
    with open('sample-eng.txt', 'r') as f:
        text = f.readlines()
        print(type(text))
    result = translator.translate(text="\n".join(text))
    print(result)

    # import time
    # from selenium import webdriver
    # import os
    #
    # chrome_options = webdriver.ChromeOptions()
    #
    # # chrome_options.add_argument('--headless')
    #
    # driver = webdriver.Chrome(os.path.abspath(os.curdir) + '/drivers/chromedriver',
    #                           chrome_options=chrome_options)
    #                           # service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #
    # driver.get('https://cn.bing.com/translator/?ref=TThis&text=bing+translation&from=en&to=zh-Hans')
    # print(driver.title)
    # time.sleep(3)
    # ele = driver.find_element_by_id("t_tl")
    # lan_select = Select(ele)
    # lan_select.select_by_value("zh-CHS")
    #
    # time.sleep(3)
    # driver.find_element_by_id("t_sv").send_keys("test")
    # time.sleep(10)
    # translated_content = driver.find_element_by_id("t_tv")
    # print(translated_content)



