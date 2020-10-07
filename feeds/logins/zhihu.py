#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
import subprocess
import time
from http import cookiejar

import requests
from requests import RequestException

cookie_path = os.path.join(os.path.expanduser("~"), "Desktop", "cookies")

if not (os.path.exists(cookie_path)):
    os.makedirs(cookie_path)

cookies_file = os.path.join(cookie_path, 'zhihu_cookie.txt')


class ZhihuAccount:
    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    BASE_HEADER = {
        'Host': 'www.zhihu.com',
        'User-Agent': UA
    }

    # 1: successful,0:fail

    def __init__(self):
        self.session = requests.Session()
        self.session.cookies = cookiejar.LWPCookieJar(filename=cookies_file)
        self.LOGIN_STATUS = 1
        try:
            self.session.cookies.load(ignore_discard=True)
        except FileNotFoundError:
            pass

    def sign_in(self):
        pass

    def sign_status(self) -> int:
        resp = self.session.get('https://www.zhihu.com/signup',
                                headers=ZhihuAccount.BASE_HEADER, allow_redirects=False)
        if resp.status_code == 302:
            return 1
        else:
            return 0

    def __login(self):
        try:
            self.session.get("https://www.zhihu.com/signup?next=%2F",
                             headers=ZhihuAccount.BASE_HEADER)

            captcha_head = {"Referer": "https://www.zhihu.com/"}
            captcha_head.update(ZhihuAccount.BASE_HEADER)
            self.session.get("https://www.zhihu.com/api/v3/oauth/captcha?lang=en",
                             headers=captcha_head)
            resp = self.session.post("https://www.zhihu.com/udid", headers=ZhihuAccount.BASE_HEADER)
            token_head = {
                'Origin': 'https://www.zhihu.com',
                'Referer': 'https://www.zhihu.com/signup?next=%2F',
                'x-udid': resp.content.decode('utf8')
            }
            token_head.update(ZhihuAccount.BASE_HEADER)
            resp = self.session.post("https://www.zhihu.com/api/v3/account/api/login/qrcode",
                                     headers=token_head)

            token = resp.json().get('token')
            qr = self.session.get(
                f'https://www.zhihu.com/api/v3/account/api/login/qrcode/{token}/image',
                headers=token_head)

            self.__show_qr_code(qr.content)
            time.sleep(10)
            start = time.time()
            while True:
                rjs = self.session.get(
                    f'https://www.zhihu.com/api/v3/account/api/login/qrcode/{token}/scan_info',
                    headers=captcha_head).json()
                # 登录成功后返回的数据包含user_id等
                # 用户在APP取消登录返回的状态码(status)是6
                # 登录成功后再次检查登录状态会返回错误信息，表示已登录
                if rjs.get('user_id', None) or rjs.get('status', None) == 6 or rjs.get('error'):
                    break
                # 用户有60秒的时间扫码并并确认登录，超时就退出。
                if time.time() - start >= 60:
                    print('登录超时！(<90s)')
                    break
                time.sleep(2)
                return True
        except RequestException as e:
            print(e)
            return False

    @staticmethod
    def __show_qr_code(image):
        """
        展示二维码供用户扫描
        """
        image_file = os.path.abspath('QR.jpg')

        with open(image_file, 'wb') as foo:
            foo.write(image)

        if platform.system() == 'Darwin':
            subprocess.call(['open', image_file])
        elif platform.system() == 'Linux':
            subprocess.call(['xdg-open', image_file])
        else:
            os.startfile(image_file)

    def sign_in(self):
        if self.sign_status() == 1:
            print('已登录！')
        else:
            print('开始登录...')
            if self.__login():
                if self.sign_status() == 0:
                    self.session.cookies.save()
                    print('登录成功！')
                    return
            print('登录失败！')

    def sign_out(self):
        if self.sign_status() == 1:
            self.session.get('https://www.zhihu.com/logout',
                             headers=ZhihuAccount.BASE_HEADER, allow_redirects=False)
            self.session.cookies.save()
        print('已退出！')

    def __enter__(self):
        self.sign_in()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sign_out()


if __name__ == '__main__':
    with ZhihuAccount() as acc:
        # do something
        print("login waiting")
