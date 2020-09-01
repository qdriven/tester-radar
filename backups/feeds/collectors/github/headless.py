#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

from pyppeteer import launch

from backups.feeds.collectors import GITHUB_USER, GITHUB_PWS

"""
pyppeteer-install
chromium extracted to: /Users/Patrick/Library/Application Support/pyppeteer/local-chromium/588429
"""


class HeadlessGithubClient():
    def __init__(self):
        self.user_name = GITHUB_USER
        self.pwd = GITHUB_PWS

    async def login(self):
        browser = await launch({"headless": False})
        page = await browser.newPage()
        await page.goto('https://github.com/login')
        await page.type("#login_field", self.user_name)
        await page.type("#password", self.pwd)
        await page.click("#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block")
        await page.goto("https://github.com/qdriven?tab=stars")
        await browser.close()

        ##


## ToDo:
# 1. Understand asyncio

if __name__ == '__main__':
    client = HeadlessGithubClient()
    asyncio.get_event_loop().run_until_complete(client.login())
