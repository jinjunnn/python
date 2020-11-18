import csv
import leancloud
from datetime import datetime
import json
from leancloud import cloudfunc

settings = {
    'teams_gift_images':'http://lc-XBtceMXX.cn-n1.lcfile.com/1643f7223eca3ab7573f/WechatIMG2446.jpeg',
    'share_page_share_title':'快帮我积攒购买3M-N95医用口罩啦，您也会享受好礼',
    'share_page_tapped_title':'邀请好友助力点赞可以享受36元购买一只3M-N95标准口罩',
    'share_page_not_tap_title':'点赞您的好友，帮TA获得爱心口罩一只',
    'customer_service_name':'SUGAR快闪店专属客服',
    'current_username':'10000715',
    'teams_gift_content':'活动说明：\n组队成功后，即可加入微信活动群，每天会有一次微信拼手气红包发放，获得最佳手气的用户，即可获赠奖品。\n另外每次组队成功，每一个用户可以获得48点心愿。',
    'actname':'1012',
    'share_page_share_image':'http://lc-xbtcemxx.cn-n1.lcfile.com/53033e6df1a97378b2b0/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-23%20%E4%B8%8B%E5%8D%8810.20.54.png',
    'share_page_content':'积攒78元购入3M-9211-N95级专业防细菌口罩(3片装)活动，原价108元',
    'share_page_rule':'活动规则：\n1.您集赞24个后，可以以最优价格购买本店美国亚马逊海淘的3M 8511一次性呼吸器面罩或NIOSH认证的N95一次性安全呼吸器面罩。\n2.本店原价108元3M 8511（三只装）口罩积攒后价格78元;原价90元的NIOSH N95（三只装）口罩积攒后60元，国内快递费需用户自己承担。\n3.由于美国亚马逊当前也经常断货，因此不能稳定供应，积攒成功后，请及时与客服取得联系，按照先完成先排号的原则进行发货。\n4.关于商品，本店是自营的海淘微信小程序店，所售商品100%正品，支持任何权威鉴定，本店承诺假一罚三，并赔偿1000元损失。\n5.关于发货，本次商品由本店驻美国买手亚马逊已完成下单，美国运输途中收货后第一时间空运国内，预计国内发货时间2月6日-2月14日。\n6.积攒成功后请及时联系小程序客服。',
    'categories':'[{"name":"美妆","index":"10","id":1},{"name":"包袋","index":"11","id":2},{"name":"服饰","index":"12","id":3},{"name":"女鞋","index":"13","id":4},{"name":"男士","index":"14","id":5},{"name":"潮牌","index":"15","id":6}]',
    'customer_service_content':'请截屏后扫码添加我的微信',
    'sub_categories':'[{"name":"精华","index":"1010","id":1},{"name":"香水","index":"1011","id":2},{"name":"化妆水","index":"1012","id":3},{"name":"口红","index":"1013","id":4},{"name":"面膜","index":"1014","id":5},{"name":"Lancome","index":"10*1000","id":7},{"name":"SK-II","index":"10*1001","id":6},{"name":"美容仪器","index":"1015","id":8},{"name":"底妆","index":"1016","id":9},{"name":"LA MAR","index":"10*1002","id":10},{"name":"雅诗兰黛","index":"10*1003","id":11},{"name":"眼妆","index":"1017","id":12},{"name":"防晒","index":"1018","id":13},{"name":"YSL","index":"10*1004","id":14},{"name":"WHOO","index":"10*1005","id":15},{"name":"乳液","index":"1019","id":16},{"name":"面霜","index":"1020","id":17}]',
    'customer_service_image':'http://lc-0EaEC5sQ.cn-n1.lcfile.com/f3bb2270f86b808c2a81/WechatIMG2410.jpeg',
    'teams_gift_title':'雅诗兰黛小棕瓶拼手气红包，手气最佳免费赠送',
    'current_goodname':'22000574',
    'share_page_member_limit':'12',
    'landing_page_bannder_1':'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
    'landing_page_bannder_2':'http://lc-XBtceMXX.cn-n1.lcfile.com/935286647bc96ca0cc44/2.png',
    'landing_page_bannder_3':'http://lc-XBtceMXX.cn-n1.lcfile.com/47ce40e258206431f39e/3.png',
    'customer_service_qrcode':'http://lc-0EaEC5sQ.cn-n1.lcfile.com/56c6ecae792ad06f2a9c/WechatIMG2411.jpeg',
    'about_shop':'SUGAR全球快闪店是一家自营社交电商。本店承诺所售商品全部由签约职业买手从海外正品官网或专柜购买，并承诺100%正品保证，本店承诺假一赔三并主动承担鉴定费以及1000元现金补偿。\n美国区商品海淘预计收货时间为30天，日本区商品预计收货时间为7-14天，香港区商品当周发货。\n部分商品存在优惠活动，下单前最好联系专属客服获得优惠信息。\n分享商品链接给好友，或分享小程序码给好友，好友购买成功将获得现金红包奖励。'
}

landing_page_settings = {
    'wechat_group_ad_text':
    '今日社群福利活动红包抽奖',
    'wechat_group_ad_content':
    '今日福利群发群发一个红包，手气最佳的用户将获得价值90元的丝芙兰面膜一盒。',
    'wechat_group_image':
    'http://lc-0EaEC5sQ.cn-n1.lcfile.com/0c9ae188d5fc38c29d46/WechatIMG2504.jpeg',
    'landing_page_bannder_1':
    'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
    'landing_page_bannder_2':
    'http://lc-XBtceMXX.cn-n1.lcfile.com/935286647bc96ca0cc44/2.png',
    'landing_page_bannder_3':
    'http://lc-XBtceMXX.cn-n1.lcfile.com/47ce40e258206431f39e/3.png',
    'enquiry_title':
    '海淘下单',
    'enquiry_wraps':
    [{
        "id":
        "01",
        "image":
        "http://lc-XBtceMXX.cn-n1.lcfile.com/86fab86b8ea2dae60ed7/1.png",
        "key":
        "enquiry_item_01",
        "listkey":
        "enquiry_item_01_wrap",
        "name":
        "淘美国",
        "type":
        "01",
        "wrap_key":
        "enquiry_list_01"
    },
     {
         "id":
         "02",
         "image":
         "http://lc-XBtceMXX.cn-n1.lcfile.com/9e64bba74181a90f62f9/2.png",
         "key":
         "enquiry_item_02",
         "listkey":
         "enquiry_item_02_wrap",
         "name":
         "淘日本",
         "type":
         "01",
         "wrap_key":
         "enquiry_list_02"
     },
     {
         "image":
         "http://lc-XBtceMXX.cn-n1.lcfile.com/61fb49d3d489de1d8771/3.png",
         "key":
         "enquiry_item_04",
         "listkey":
         "enquiry_item_04_wrap",
         "name":
         "淘香港",
         "type":
         "01",
         "wrap_key":
         "enquiry_list_04"
     }],
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
         'brand测试数据，请勿购买',
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
         '时尚轻奢',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'top': [{
             'name':
             'coach',
             'image':
             'http://lc-XBtceMXX.cn-n1.lcfile.com/f317a48c1ef182905dd1/WechatIMG2584.jpeg',
             'key':
             'list_coach',
         },
                 {
                     'name':
                     '潮鞋',
                     'image':
                     'http://lc-XBtceMXX.cn-n1.lcfile.com/f61374b58015282e381f/WechatIMG2583.jpeg',
                     'key':
                     'list_snakers',
                 }]
     },
     {
         'name':
         '美妆护肤 美国站',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'list': [{
             'name': '美国丝芙兰官网热销榜单',
             'key': 'list_sephora_sub_top100'
         }, {
             'name': '雅诗兰黛(Estée Lauder)',
             'key': 'list_sephora_sub_6089'
         }, {
             'name': '科颜氏(Kiehls)',
             'key': 'list_sephora_sub_6218'
         }, {
             'name': '兰蔻(Lancôme)',
             'key': 'list_sephora_sub_1741'
         }, {
             'name': '纪梵希(Givenchy)',
             'key': 'list_sephora_sub_1133'
         }, {
             'name': 'NARS',
             'key': 'list_sephora_sub_3976'
         }, {
             'name': '圣罗兰(YSL)',
             'key': 'list_sephora_sub_1070'
         }, {
             'name': '香奈儿(CHANEL)',
             'key': 'list_sephora_sub_1065'
         }, {
             'name': '资生堂(Shiseido)',
             'key': 'list_sephora_sub_5337'
         }, {
             'name': '迪奥(Dior)',
             'key': 'list_sephora_sub_1073'
         }, {
             'name': '倩碧(CLINIQUE)',
             'key': 'list_sephora_sub_1254'
         }, {
             'name': '阿曼尼(Armani Beauty)',
             'key': 'list_sephora_sub_1517'
         }, {
             'name': '娇兰(Guerlain)',
             'key': 'list_sephora_sub_1132'
         }, {
             'name': 'TOM FORD',
             'key': 'list_sephora_sub_5869'
         }, {
             'name': '芭比波朗(Bobbi Brown)',
             'key': 'list_sephora_sub_5644'
         }, {
             'name': '娇韵诗(Clarins)',
             'key': 'list_sephora_sub_2082'
         }, {
             'name': 'Miu Miu',
             'key': 'list_sephora_sub_6135'
         }, {
             'name': '范思哲(Versace)',
             'key': 'list_sephora_sub_2084'
         }, {
             'name': '海蓝之谜(La Mer)',
             'key': 'list_sephora_sub_6201'
         }, {
             'name': 'IT Cosmetics',
             'key': 'list_sephora_sub_6175'
         }, {
             'name': '蒂佳婷(Dr. Jart+)',
             'key': 'list_sephora_sub_6014'
         }, {
             'name': 'AMOREPACIFIC',
             'key': 'list_sephora_sub_5945'
         }]
     },
     {
         'name':
         '日本护肤站',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'list': [{
             'name': '人气贵妇护肤单品',
             'key': 'list_skincare_jp_0001'
         }, {
             'name': '人气平价护肤单品',
             'key': 'list_skincare_jp_0101'
         }, {
             'name': '人气面膜',
             'key': 'list_skincare_jp_0801'
         }, {
             'name': '防晒',
             'key': 'list_skincare_jp_0901'
         }, {
             'name': '洁面',
             'key': 'list_skincare_jp_1001'
         }, {
             'name': '卸妆',
             'key': 'list_skincare_jp_1101'
         }, {
             'name': '爽肤水/化妆水',
             'key': 'list_skincare_jp_1201'
         }, {
             'name': '精华/美容液',
             'key': 'list_skincare_jp_1501'
         }, {
             'name': '乳液/凝胶',
             'key': 'list_skincare_jp_1601'
         }, {
             'name': '面霜',
             'key': 'list_skincare_jp_1301'
         }, {
             'name': '眼部护理',
             'key': 'list_skincare_jp_1401'
         }, {
             'name': '手/足护理',
             'key': 'list_skincare_jp_1701'
         }, {
             'name': '唇部护理',
             'key': 'list_skincare_jp_1801'
         }, {
             'name': '男士护肤',
             'key': 'list_skincare_jp_1901'
         }, {
             'name': '旅行装',
             'key': 'list_skincare_jp_2001'
         }, {
             'name': '护肤仪器',
             'key': 'list_skincare_jp_2101'
         }]
     },
     {
         'name':
         '日本美妆站',
         'image':
         'http://lc-XBtceMXX.cn-n1.lcfile.com/911454be17233dce278b/1.jpeg',
         'list': [{
             'name': '人气贵妇美妆单品',
             'key': 'list_beauty_makeup_jp_0001'
         }, {
             'name': '人气平价美妆单品',
             'key': 'list_beauty_makeup_jp_0101'
         }, {
             'name': '口红',
             'key': 'list_beauty_makeup_jp_0201'
         }, {
             'name': '香水',
             'key': 'list_beauty_makeup_jp_0301'
         }, {
             'name': 'BB霜/CC霜',
             'key': 'list_beauty_makeup_jp_1001'
         }, {
             'name': '唇膏/唇彩',
             'key': 'list_beauty_makeup_jp_1101'
         }, {
             'name': '隔离/妆前',
             'key': 'list_beauty_makeup_jp_1201'
         }, {
             'name': '粉底',
             'key': 'list_beauty_makeup_jp_1301'
         }, {
             'name': '粉饼/散粉',
             'key': 'list_beauty_makeup_jp_1401'
         }, {
             'name': '美甲',
             'key': 'list_beauty_makeup_jp_1501'
         }, {
             'name': '眼线笔/眉笔',
             'key': 'list_beauty_makeup_jp_1601'
         }, {
             'name': '睫毛膏',
             'key': 'list_beauty_makeup_jp_1701'
         }, {
             'name': '眼影',
             'key': 'list_beauty_makeup_jp_1801'
         }, {
             'name': '腮红',
             'key': 'list_beauty_makeup_jp_1901'
         }, {
             'name': '遮瑕',
             'key': 'list_beauty_makeup_jp_2001'
         }, {
             'name': '高光/修颜',
             'key': 'list_beauty_makeup_jp_2101'
         }, {
             'name': '化妆工具',
             'key': 'list_beauty_makeup_jp_2201'
         }, {
             'name': '化妆单品',
             'key': 'list_beauty_makeup_jp_2301'
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

# {
#     'name': '日本五大药妆店精选单品',
#     'key': 'list_jp_100'
# },


#  这个是电商
leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

# good_csv = []
# goods_list = cloudfunc.run('getListItemHash', key='act*')


def download_settings():
    settings = cloudfunc.run('getHash', key='settings')
    print(settings)

# 将写好的settings,上传到redis中。
def upload_settings(settings):
    for field, value in settings.items():
        result = cloudfunc.run('setField', key='settings', field= field, value= value)

#   将写好的boject输出到 json模式，方便上传。
def object_to_json(key,obj):
    obj_json = json.dumps(obj)
    #  将   landing_page_settings 、的json表上传
    upload_json_obj = cloudfunc.run('setString', key=key, value=obj_json)

# upload_settings(settings)
object_to_json('landing_page_settings', landing_page_settings)
# upload_settings(settings)
# print(landing_page_settings)
