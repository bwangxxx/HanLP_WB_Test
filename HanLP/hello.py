#! python3
# coding=utf-8

from pyhanlp import *

print(HanLP.segment('您好，欢迎在Python中调用HanLP的API'))

for term in HanLP.segment('下雨天地面积水'):
    print('{}\t{}'.format(term.word, term.nature))  # 获取单词与词性

testCases = [
    "商品和服务",
    "结婚的和尚未结婚的确实在干扰分词啊",
    "买水果然后来世博园最后去世博会",
    "中国的首都是北京",
    "欢迎新老师生前来用餐",
    "欢迎新老师生前来就餐",
    "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
    "王国维和服务员",
    "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。"]

for sentence in testCases:
    print(HanLP.segment(sentence))

document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
           "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
           "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
           "严格地进行水资源论证和取水许可的批准。"

# 关键词提取
print(HanLP.extractKeyword(document, 2))

# 自动摘要
print(HanLP.extractSummary(document, 3))


def main():
    HanLP.Config.enableDebug()  # 为了避免你等得无聊，开启调试模式说点什么:-)
    # print(HanLP.segment("王国维和服务员"))
    print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标"))  # 依存句法分析
    print(HanLP.parseDependency("萨哈夫说，伊拉克将同联合国销毁伊拉克大规模杀伤性武器特别委员会继续保持合作。"))  # 依存句法分析


if __name__ == '__main__':
    main()
