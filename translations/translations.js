const puppeteer = require('puppeteer');

(async () =>{
    const browser = await puppeteer.launch()
    const page = await puppeteer.newPage()
    await page.goto("https://cn.bing.com/translator/?ref=TThis&text=bing+translation&from=en&to=zh-Hans")
})();