#   设置 classic_data


import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc


'''

这段代码是将 app 的settings 数据上传

'''




classic_list = {
    'classic_list':
    [{
        'name':
        '美妆护肤',
        'image':
        'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
        'top': [
            {
                'name':
                '唇膏唇釉',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/403cc2fac612515bcd73/WechatIMG2680.jpeg',
                'key':
                'list_skincare_0002',
            },
            {
                'name':
                '香水',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/bb66759c1a9ffc19df5d/WechatIMG2678.jpeg',
                'key':
                'list_skincare_0008',
            },
        ],
        'list': [
            {
                'name':
                '洁面',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/eaa313abd34481d39896/%E6%B4%97%E9%9D%A2%E5%A5%B6.png',
                'key':
                'list_skincare_0003',
            },
            {
                'name':
                '面膜',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/01ac5e871f8612f59571/%E9%9D%A2%E8%86%9C.png',
                'key':
                'list_skincare_0001',
            },
            {
                'name':
                '唇膏唇釉',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/3cbb77541450a880bd08/%E5%8F%A3%E7%BA%A2.png',
                'key':
                'list_skincare_0002',
            },
            {
                'name':
                '香水',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/3cbb77541450a880bd08/%E5%8F%A3%E7%BA%A2.png',
                'key':
                'list_skincare_0008',
            },
            {
                'name':
                '精华/美容液',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/f950726f69ccb7aee49a/%E7%BE%8E%E5%AE%B9%E6%B6%B2.png',
                'key':
                'list_skincare_0005',
            },
            {
                'name':
                '面霜',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/f950726f69ccb7aee49a/%E7%BE%8E%E5%AE%B9%E6%B6%B2.png',
                'key':
                'list_skincare_0009',
            },
            {
                'name':
                '乳液',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/17cc3b1c63357568f459/%E6%B0%B4%E4%B9%B3.png',
                'key':
                'list_skincare_0006',
            },
            {
                'name':
                '眼霜/眼膜',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/c054302e2fa2be00633a/%E7%9C%BC%E9%9C%9C.png',
                'key':
                'list_skincare_0007',
            },
            {
                'name':
                '防晒',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/eaa313abd34481d39896/%E6%B4%97%E9%9D%A2%E5%A5%B6.png',
                'key':
                'list_skincare_0004',
            },
            {
                'name':
                '化妆水',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/eaa313abd34481d39896/%E6%B4%97%E9%9D%A2%E5%A5%B6.png',
                'key':
                'list_skincare_0010',
            },
            {
                'name':
                'BB/CC霜',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/a344730acf5550d1aef1/%E5%BD%A9%E5%A6%86.png',
                'key':
                'list_skincare_0011',
            },
            {
                'name':
                '隔离/妆前',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/eaa313abd34481d39896/%E6%B4%97%E9%9D%A2%E5%A5%B6.png',
                'key':
                'list_skincare_0012',
            },
            {
                'name':
                '粉底',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/a344730acf5550d1aef1/%E5%BD%A9%E5%A6%86.png',
                'key':
                'list_skincare_0013',
            },
            {
                'name':
                '粉饼/散粉',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/17cc3b1c63357568f459/%E6%B0%B4%E4%B9%B3.png',
                'key':
                'list_skincare_0014',
            },
            {
                'name':
                '眼妆',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/c054302e2fa2be00633a/%E7%9C%BC%E9%9C%9C.png',
                'key':
                'list_skincare_0015',
            },
            {
                'name':
                '腮红',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/9d6eeb87d0b13f76c835/%E9%A6%99%E6%B0%B4.png',
                'key':
                'list_skincare_0016',
            },
            {
                'name':
                '遮瑕',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/c054302e2fa2be00633a/%E7%9C%BC%E9%9C%9C.png',
                'key':
                'list_skincare_0017',
            },
            {
                'name':
                '其他',
                'image':
                'http://lc-XBtceMXX.cn-n1.lcfile.com/9d6eeb87d0b13f76c835/%E9%A6%99%E6%B0%B4.png',
                'key':
                'list_skincare_0018',
            },
        ]
    },
     {
         'name':
         '美妆护肤品牌',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'list': [{
             "name": "esteelauder",
             "key": "list_esteelauder"
         }, {
             "name": "kiehls",
             "key": "list_kiehls"
         }, {
             "name": "givenchy",
             "key": "list_givenchy"
         }, {
             "name": "nars",
             "key": "list_nars"
         }, {
             "name": "ysl",
             "key": "list_ysl"
         }, {
             "name": "chanel",
             "key": "list_chanel"
         }, {
             "name": "shiseido",
             "key": "list_shiseido"
         }, {
             "name": "dior",
             "key": "list_dior"
         }, {
             "name": "clinique",
             "key": "list_clinique"
         }, {
             "name": "armani",
             "key": "list_armani"
         }, {
             "name": "guerlain",
             "key": "list_guerlain"
         }, {
             "name": "tomford",
             "key": "list_tomford"
         }, {
             "name": "bobbibrown",
             "key": "list_bobbibrown"
         }, {
             "name": "clarins",
             "key": "list_clarins"
         }, {
             "name": "miumiu",
             "key": "list_miumiu"
         }, {
             "name": "versace",
             "key": "list_versace"
         }, {
             "name": "lamar",
             "key": "list_lamar"
         }, {
             "name": "sk2",
             "key": "list_sk2"
         }, {
             "name": "decorte",
             "key": "list_decorte"
         }, {
             "name": "cpb",
             "key": "list_cpb"
         }, {
             "name": "laparirie",
             "key": "list_laparirie"
         }, {
             "name": "pola",
             "key": "list_pola"
         }, {
             "name": "suqqu",
             "key": "list_suqqu"
         }, {
             "name": "sisley",
             "key": "list_sisley"
         }, {
             "name": "ipsa",
             "key": "list_ipsa"
         }, {
             "name": "hacci",
             "key": "list_hacci"
         }, {
             "name": "three",
             "key": "list_three"
         }, {
             "name": "sofina",
             "key": "list_sofina"
         }, {
             "name": "shuuemura",
             "key": "list_shuuemura",
             "name": "植村秀"
         }, {
             "name": "rmk",
             "key": "list_rmk"
         }, {
             "name": "lancome",
             "key": "list_lancome"
         }, {
             "name": "hr",
             "key": "list_hr"
         }, {
             "name": "haba",
             "key": "list_haba",
             "name": "无添加主义"
         }, {
             "name": "freeplus",
             "key": "list_freeplus"
         }, {
             "name": "fancl",
             "key": "list_fancl"
         }, {
             "name": "elixir",
             "key": "list_elixir",
             "name": "怡丽丝尔"
         }, {
             "name": "drlabo",
             "key": "list_drlabo",
             "name": "城野医生"
         }, {
             "name": "dhc",
             "key": "list_dhc"
         }, {
             "name": "curel",
             "key": "list_curel",
             "name": "珂润"
         }, {
             "name": "covermark",
             "key": "list_covermark",
             "name": "傲丽"
         }, {
             "name": "nike",
             "key": "list_nike"
         }, {
             "name": "coach",
             "key": "list_coach"
         }, {
             "name": "adidas",
             "key": "list_adidas"
         }, {
             "name": "mk",
             "key": "list_mk"
         }, {
             "name": "itcosmetics",
             "key": "list_itcosmetics"
         }, {
             "name": "drjart",
             "key": "list_drjart"
         }]
     },
     {
         'name':
         '保健养生 日本站',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'top': [{
             'name':
             '常备药',
             'image':
             'http://lc-XBtceMXX.cn-n1.lcfile.com/3d796e16adc5d0cf8459/%E5%B8%B8%E5%A4%87%E8%8D%AF.png',
             'key':
             'list_drug__0001',
         },
                 {
                     'name':
                     '美容',
                     'image':
                     'http://lc-XBtceMXX.cn-n1.lcfile.com/2a1a8d876bd2f4e87025/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-03-30%20%E4%B8%8A%E5%8D%8812.44.57.png',
                     'key':
                     'list_drug_0002',
                 }],
         'list': [{
             'name': '汉方药',
             'key': 'list_drug_jp_1112'
         }, {
             'name': '健康食品',
             'key': 'list_drug_jp_1202'
         }, {
             'name': '减肥',
             'key': 'list_drug_jp_1203'
         }, {
             'name': '滋养强壮',
             'key': 'list_drug_jp_1107'
         }, {
             'name': '营养液',
             'key': 'list_drug_jp_1108'
         }, {
             'name': '保健品',
             'key': 'list_drug_jp_1200'
         }, {
             'name': '营养饮食',
             'key': 'list_drug_jp_1201'
         }, {
             'name': '生发剂',
             'key': 'list_drug_jp_1115'
         }, {
             'name': '生活改善',
             'key': 'list_drug_jp_1120'
         }, {
             'name': '便秘药',
             'key': 'list_drug_jp_1111'
         }, {
             'name': '肠胃药',
             'key': 'list_drug_jp_1109'
         }, {
             'name': '湿疹皮炎',
             'key': 'list_drug_jp_1113'
         }, {
             'name': '鼻炎治疗药',
             'key': 'list_drug_jp_1104'
         }, {
             'name': '外用阵痛消炎',
             'key': 'list_drug_jp_1118'
         }, {
             'name': '保健机能食品',
             'key': 'list_drug_jp_1204'
         }, {
             'name': '整肠剂  止泻药',
             'key': 'list_drug_jp_1110'
         }, {
             'name': '総合感冒薬',
             'key': 'list_drug_jp_1102'
         }, {
             'name': '薬用酒',
             'key': 'list_drug_jp_1122'
         }, {
             'name': '鎮痛解熱消炎剤',
             'key': 'list_drug_jp_1101'
         }, {
             'name': '感冒辅助药',
             'key': 'list_drug_jp_1105'
         }, {
             'name': '眼药',
             'key': 'list_drug_jp_1100'
         }, {
             'name': '鎮咳去痰剤',
             'key': 'list_drug_jp_1103'
         }, {
             'name': '口腔用剂',
             'key': 'list_drug_jp_1115'
         }]
     },
     {
         'name':
         '网红零食 日本站',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'list': [{
             'name': '半生菓子',
             'key': 'list_snacks_jp_5507'
         }, {
             'name': '口香糖',
             'key': 'list_snacks_jp_5500'
         }, {
             'name': '米菓',
             'key': 'list_snacks_jp_5504'
         }, {
             'name': '巧克力饼干',
             'key': 'list_snacks_jp_5502'
         }, {
             'name': '焼菓子',
             'key': 'list_snacks_jp_5505'
         }, {
             'name': '嗜好品',
             'key': 'list_snacks_jp_5509'
         }, {
             'name': '糖果',
             'key': 'list_snacks_jp_5501'
         }, {
             'name': '甜点',
             'key': 'list_snacks_jp_5511'
         }, {
             'name': '珍味',
             'key': 'list_snacks_jp_5508'
         }, {
             'name': '子供菓子',
             'key': 'list_snacks_jp_5506'
         }]
     }]
}

#  这个是电商
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

#   将写好的boject输出到 json模式，上传到 redis hash表中
def object_to_json_update_to_field(key, field,value):
    dt = json.dumps(value)
    print(key,field)
    print(dt)
    load = cloudfunc.run('setField', key=key, field=field,value=dt)
    print(load)


object_to_json_update_to_field('lottery_app_settings', 'classic_data',classic_list)
