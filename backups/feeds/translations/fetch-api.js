fetch("https://cn.bing.com/ttranslate?&category=&IG=4087582A95EF496C879C525D9693B51E&IID=translator.5038.3", {
    "credentials": "include",
    "headers": {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded"
    },
    "referrer": "https://cn.bing.com/translator/?ref=TThis&text=bing+translation&from=en&to=zh-Hans",
    "referrerPolicy": "origin-when-cross-origin",
    "body": "&text=bing%20translation%20test&from=en&to=zh-CHS",
    "method": "POST",
    "mode": "cors"
});