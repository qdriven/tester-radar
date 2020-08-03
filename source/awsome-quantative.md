金融量化数据源主要有三种：一是大数据网站，一般只有日线级数据；二是专业金融数据公司，如通联和万德，收费价格高但数据齐全且比较稳定；三是开源数据模块库，如Tushare，pandas-datareader，ccxt数字货币等，github上还有很多不一一列举。



Python开源数据

TuShare pro，中文财经数据接口包，有积分限制。

 https://tushare.pro/

BaoStock，与tushare类似，主要提供国内股票行情数据、公司基本面和宏观数据：http://baostock.com/

Quandl :https://www.quandl.com/


     国际金融和经济数据。

pandas_datareader：https://pandas-datareader.readthedocs.io/en/latest/

    从pandas中独立出来的数据开源库，丰富的数据源，包括美股、A股、宏观数据等。

yfinance：https://pypi.org/project/yfinance/

     雅虎财经数据api的修复。

ccxt：https://github.com/ccxt/ccxt

python数字货币开源接口



其他数据源

通达信 （免费）

聚宽：jqdatasdk（免费）

新浪、雅虎、东方财富网（免费）

Wind资讯-经济数据库（收费）

东方财富Choice金融终端（收费）

同花顺金融数据终端 （可免费导出）


平台之间大同小异，可以重点关注各大平台的策略大赛（练手）、社区（借鉴参考优秀项目）和学院（系统学习量化知识框架）板块。



国内平台（排名不分先后）：

BigQuant ：https://bigquant.com/

人工智能量化平台，社区和学院提供了较丰富的资源。

聚宽 ：https://www.joinquant.com/       

免费量化数据、投研工具、量化学习体系

优矿 ：https://uqer.io/       

特色是深度报告、量化学堂和量化社区

万矿 ：https://www.windquant.com/      

 金融大数据、策略研究和数据可视化

Ricequant ：https://www.ricequant.com/welcome/

涵盖金融数据、投资组合管理与风险分析、量化投研交易模块

掘金量化 ：https://www.myquant.cn/

Factors ：http://factors.chinascope.com/

专注于多因子分析，界面操作，黑盒子。



国外量化平台：  

    国外量化平台非常多，这里只推荐两个。

Quantopian ：https://www.quantopian.com/posts

比较知名的平台，旗下有量化三大件：pyFolio，zipline，alphalens

Quantstart：https://www.quantstart.com/

平台文章提供了构建自己量化交易系统的思路框架



开源框架（实现本地化）：     

     一般是直接在终端（cmd）上使用pip install xxx(库名）进行安装，有些可能需要下载安装包离线安装。

Zipline - 回测框架

vnpy - python开源开发框架

easytrader - 自动程序化股票交易

pyalgotrade - 基于事件驱动回测框架

quantmod - 量化金融建模

backtrader -量化回测框架

量化投资专业网站、博客、论坛

ARQ：https://www.aqr.com/

Quantivity：https://quantivity.wordpress.com/page/2/ 

QuantLib:http://www.implementingquantlib.com/ 


NuclearPhynance: http://www.nuclearphynance.com/ 

QuantNet Community：

https://quantnet.com/ 

Udacity ：

https://www.udacity.com/course/machine-learning-for-trading--ud501

Quant At Risk ：

http://www.quantatrisk.com/ 

经管之家：

https://bbs.pinggu.org/forum-2166-1.html

知乎 -宽客：

https://bbs.pinggu.org/forum-2166-1.html 

知乎 -量化：

https://www.zhihu.com/topic/19815465/hot

GitHub : https://github.com/

FMZ发明者量化交易平台: https://www.fmz.com/bbs

量化投资书籍

     如果完全不懂金融投资理论，就谈量化投资，很容易流于形式，画出来漂亮的图表和策略，也就能忽悠一下外行而已。一直强调Python只是工具，不要舍本逐末，量化投资核心是策略和思路，而策略的来源需要一定的统计和投资学的积累与沉淀。

曼昆的宏微观经济学、米什金的《货币金融学》、罗斯《公司理财》、博迪《投资学》、《金融工程》、索罗斯《金融炼金术》）

《计量经济学导论：现代观点》

     主要学习时间序列分析、多元统计线性回归，可结合Python的statsmodels、scipy、sklearn模块进行学习。

多因子模型：基础好的话可以阅读砝码三因子的PAPER。

    此外，Barra风险模型（多因子模型扩展）是现在非常主流的量化模型，有很多可以参考的资料，如《Barra Risk Model Handbook（US）》。



投资相关书籍

《打开量化投资的黑箱》 里什·纳兰

《宽客》[美] 斯科特·帕特森

《解读量化投资：西蒙斯用公式打败市场的故事》忻海

《漫步华尔街》麦基尔

《海龟交易法则》柯蒂斯·费思

《交易策略评估与最佳化》罗伯特·帕多

《统计套利》 安德鲁·波尔

《信号与噪声》纳特•西尔弗

《量化投资—策略与技术》丁鹏

《量化投资策略:如何实现超额收益Alpha》吴冲锋

《以交易为生》埃尔德

《高级技术分析》布鲁斯·巴布科克

《积极型投资组合管理》格里纳德，卡恩

《金融计量学:从初级到高级建模技术》斯维特洛扎

《量化交易如何建立自己的算法交易事业》欧内斯特·陈

《聪明的投资者》 本杰明·格雷厄姆

《期权、期货和其他衍生品》 约翰·赫尔




学术期刊

金融三大顶级期刊：

Journal of Finance、

Journal of Financial Economics、

Review of Financial Studies

其他金融投资期刊：

Journal of Accounting and Economics、Journal of Financial and Quantitative Analysis、Financial Analysts 、Journal Financial Management、Journal of Empirical Finance、Quantitative Finance、Journal of Alternative Investments、Journal of Fixed Income、Journal of Investing、Journal of Portfolio Management、Journal of Trading、Review of Asset Pricing Studies