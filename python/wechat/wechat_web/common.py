#coding=utf-8
import re
import leancloud
from leancloud import cloudfunc
import time

leancloud.init(
    "XBtceMXXkxxRQez6lQBCJ8UK-gzGzoHsz", master_key="KlbmMqYVvcOC7adJvwoRO9Ww")

card = [
    {
        'name': '4852',
        'value': 'sephora'
    },
    {
        'name': '4786',
        'value': 'sephora'
    },
    {
        'name': '5113',
        'value': 'Master'
    },
    {
        'name': '4358',
        'value': 'VISA'
    },
    {
        'name': '4034',
        'value': 'VISA'
    },
    {
        'name': '3779',
        'value': 'Amex/ae'
    },
    {
        'name': '4847',
        'value': 'Vanilla'
    },
    {
        'name': '4941',
        'value': 'Vanilla'
    },
    {
        'name': '5432',
        'value': 'Vanilla'
    },
    {
        'name': '5164',
        'value': 'Vanilla'
    },
    {
        'name': '4142',
        'value': 'Vanilla'
    },
    {
        'name': '4118',
        'value': 'Vanilla'
    },
    {
        'name': '丝芙兰',
        'value': 'sephora'
    },
    {
        'name': 'sephora',
        'value': 'sephora'
    },
    {
        'name': 'Nordstrom',
        'value': 'Nordstrom'
    },
    {
        'name': 'nd',
        'value': 'Nordstrom'
    },
    {
        'name': '诺德',
        'value': 'Nordstrom'
    },
    {
        'name': 'iTunes',
        'value': 'iTunes'
    },
    {
        'name': 'steam',
        'value': 'steam'
    },
    {
        'name': 'Google',
        'value': 'Google'
    },
    {
        'name': '谷歌',
        'value': 'Google'
    },
    {
        'name': 'Macy',
        'value': 'Macy'
    },
    {
        'name': '梅西',
        'value': 'Macy'
    },
    {
        'name': 'walmart visa',
        'value': 'wm visa'
    },
    {
        'name': '沃尔玛',
        'value': 'wm visa'
    },
    {
        'name': 'walmart visa',
        'value': 'wm visa'
    },
    {
        'name': 'wm visa',
        'value': 'wm visa'
    },
    {
        'name': 'visa',
        'value': 'visa'
    },
    {
        'name': 'ae',
        'value': 'Amex/ae'
    },
    {
        'name': 'Amex',
        'value': 'Amex/ae'
    },
    {
        'name': 'Vanilla',
        'value': 'Vanilla'
    },
    {
        'name': '香草',
        'value': 'Vanilla'
    },
    {
        'name': 'master',
        'value': 'Master'
    },
    {
        'name': '万事达',
        'value': 'Master'
    },
    {
        'name': '梅西',
        'value': '梅西'
    },
    {
        'name': 'macy',
        'value': '梅西'
    },
    {
        'name': 'NIKE',
        'value': 'NIKE'
    },
    {
        'name': '耐克',
        'value': 'NIKE'
    },
    {
        'name': 'Footlocker',
        'value': 'Footlocker'
    },
]

brand = [
    {
        'name': "KIEHL'S",
        'value': "科颜氏"
    }, {
        'name': '科颜氏',
        'value': "科颜氏"
    }, {
        'name': 'Freeplus',
        'value': 'Freeplus'
    }, {
        'name': '芙丽芳丝',
        'value': 'Freeplus'
    }, {
        'name': 'Armani',
        'value': '阿玛尼'
    }, {
        'name': '阿曼尼',
        'value': '阿玛尼'
    }, {
        'name': '阿玛尼',
        'value': '阿玛尼'
    }, {
        'name': 'Sloggi',
        'value': '黛安芬'
    }, {
        'name': '黛安芬',
        'value': '黛安芬'
    }, {
        'name': 'PANDORA',
        'value': '潘多拉'
    }, {
        'name': '潘多拉',
        'value': '潘多拉'
    }, {
        'name': 'PDC',
        'value': 'PDC'
    }, {
        'name': '碧迪皙',
        'value': 'PDC'
    }, {
        'name': 'LA MER',
        'value': '海蓝之谜'
    }, {
        'name': '海蓝之谜',
        'value': '海蓝之谜'
    }, {
        'name': 'DECORTE',
        'value': '黛珂'
    }, {
        'name': '黛珂',
        'value': '黛珂'
    }, {
        'name': 'Adidas',
        'value': 'Adidas'
    }, {
        'name': '阿迪达斯',
        'value': 'Adidas'
    }, {
        'name': 'Curel',
        'value': '珂润'
    }, {
        'name': '珂润',
        'value': '珂润'
    }, {
        'name': 'Dior',
        'value': 'Dior'
    }, {
        'name': '迪奥',
        'value': 'Dior'
    }, {
        'name': 'LAB SERIES',
        'value': '朗仕'
    }, {
        'name': '朗仕',
        'value': '朗仕'
    }, {
        'name': 'BOBBI BROWN',
        'value': 'BOBBI BROWN'
    }, {
        'name': '芭比波朗',
        'value': 'BOBBI BROWN'
    }, {
        'name': 'Nintendo',
        'value': '任天堂'
    }, {
        'name': '任天堂',
        'value': '任天堂'
    }, {
        'name': 'IPSA',
        'value': 'IPSA'
    }, {
        'name': '茵芙纱',
        'value': 'IPSA'
    }, {
        'name': 'Shiseido',
        'value': '资生堂'
    }, {
        'name': '资生堂',
        'value': '资生堂'
    }, {
        'name': 'Fancl',
        'value': '芳珂'
    }, {
        'name': '芳珂',
        'value': '芳珂'
    }, {
        'name': 'Apple',
        'value': 'Apple'
    }, {
        'name': '苹果',
        'value': 'Apple'
    }, {
        'name': 'IQOS',
        'value': 'IQOS'
    }, {
        'name': 'POLA',
        'value': 'POLA'
    }, {
        'name': '宝丽',
        'value': 'POLA'
    }, {
        'name': 'DECORTE',
        'value': '黛珂'
    }, {
        'name': '黛珂',
        'value': '黛珂'
    }, {
        'name': 'La prairie',
        'value': 'La prairie'
    }, {
        'name': '莱珀妮',
        'value': 'La prairie'
    }, {
        'name': 'CLINIQUE',
        'value': 'CLINIQUE'
    }, {
        'name': '倩碧',
        'value': 'CLINIQUE'
    }, {
        'name': 'TF',
        'value': 'TOM FORD'
    }, {
        'name': 'TOM FORD',
        'value': 'TOM FORD'
    }, {
        'name': 'NARS',
        'value': 'NARS'
    }, {
        'name': '雅诗兰黛',
        'value': 'Estee Lauder'
    }, {
        'name': 'Estee Lauder',
        'value': 'Estee Lauder'
    }, {
        'name': 'Guerlain',
        'value': 'Guerlain'
    }, {
        'name': '娇兰',
        'value': 'Guerlain'
    }, {
        'name': 'HACCI',
        'value': 'HACCI'
    }, {
        'name': 'BIODERMA',
        'value': '贝德玛'
    }, {
        'name': '贝德玛',
        'value': '贝德玛'
    }, {
        'name': 'POLA',
        'value': 'POLA'
    }, {
        'name': '宝丽',
        'value': 'POLA'
    }, {
        'name': 'IPSA',
        'value': 'IPSA'
    }, {
        'name': '茵芙莎',
        'value': 'IPSA'
    }, {
        'name': 'RMK',
        'value': 'RMK'
    }, {
        'name': 'SUQQU',
        'value': 'SUQQU'
    }, {
        'name': 'LANCOME',
        'value': 'LANCOME'
    }, {
        'name': '兰蔻',
        'value': 'LANCOME'
    }, {
        'name': "L'OREAL",
        'value': "欧莱雅"
    }, {
        'name': '欧莱雅',
        'value': "欧莱雅"
    }, {
        'name': 'Givenchy',
        'value': '纪梵希'
    }, {
        'name': '纪梵希',
        'value': '纪梵希'
    }, {
        'name': 'Elégance',
        'value': '雅莉格丝'
    }, {
        'name': '雅莉格丝',
        'value': '雅莉格丝'
    }, {
        'name': 'MAC',
        'value': 'MAC'
    }, {
        'name': '魅可',
        'value': 'MAC'
    }, {
        'name': 'SISLEY',
        'value': '希思黎'
    }, {
        'name': '希思黎',
        'value': '希思黎'
    }, {
        'name': 'Freeplus',
        'value': 'Freeplus'
    }, {
        'name': '芙丽芳丝',
        'value': 'Freeplus'
    }, {
        'name': 'Dyson',
        'value': '戴森'
    }, {
        'name': '戴森',
        'value': '戴森'
    }, {
        'name': 'Clarins',
        'value': '娇韵诗'
    }, {
        'name': 'CLARINS',
        'value': '娇韵诗'
    }, {
        'name': '娇韵诗',
        'value': '娇韵诗'
    }, {
        'name': 'HABA',
        'value': 'HABA'
    }, {
        'name': '无添加主义',
        'value': 'HABA'
    }, {
        'name': 'CHANEL',
        'value': '香奈儿'
    }, {
        'name': '香奈儿',
        'value': '香奈儿'
    }, {
        'name': 'CPB',
        'value': 'CPB'
    }, {
        'name': '肌肤之钥',
        'value': 'CPB'
    }, {
        'name': 'HR',
        'value': '赫莲娜'
    }, {
        'name': '赫莲娜',
        'value': '赫莲娜'
    }, {
        'name': 'SKII',
        'value': 'SKII'
    }, {
        'name': 'SK2',
        'value': 'SKII'
    }, {
        'name': 'YSL',
        'value': 'YSL'
    }, {
        'name': '圣罗兰',
        'value': 'YSL'
    }, {
        'name': 'BIOTHERM',
        'value': '碧欧泉'
    }, {
        'name': '碧欧泉',
        'value': '碧欧泉'
    }, {
        'name': 'NIKE',
        'value': 'NIKE'
    }, {
        'name': '耐克',
        'value': 'NIKE'
    }, {
        'name': 'Versace',
        'value': 'Versace'
    }, {
        'name': '范思哲',
        'value': 'Versace'
    }, {
        'name': "Kiehl's",
        'value': "科颜氏"
    }, {
        'name': '科颜氏',
        'value': "科颜氏"
    }, {
        'name': 'FANCL',
        'value': 'FANCL'
    }, {
        'name': '芳珂',
        'value': 'FANCL'
    }, {
        'name': 'ReFa',
        'value': 'ReFa'
    }, {
        'name': 'GUERLAIN',
        'value': '娇兰'
    }, {
        'name': '娇兰',
        'value': '娇兰'
    }, {
        'name': 'Tiffany&Co.',
        'value': '蒂芙尼'
    }, {
        'name': '蒂芙尼',
        'value': '蒂芙尼'
    }, {
        'name': '理肤泉',
        'value': '理肤泉'
    }, {
        'name': 'GUCCI',
        'value': 'GUCCI'
    }, {
        'name': '古驰',
        'value': 'GUCCI'
    }, {
        'name': 'Miu Miu',
        'value': 'Miu Miu'
    }
]


def get_card_info(data, file):
    obj = {}
    name = ''
    func = 'card'
    #   类型  出售 还是 求购
    if re.search('收', data) is not None:
        name = '求购'
        obj['type'] = 2
    elif re.search('求', data) is not None:
        name = '求购'
        obj['type'] = 2
    elif re.search('出', data) is not None:
        name = '出售'
        obj['type'] = 1
    else:
        return None

    #   卡名
    obj['brand'] = None
    for item in card:
        result = re.search(item['name'],data)
        if result is not None:
            obj['brand'] = item['value']
    if obj['brand']:
        pass
    else:
        return None
    #   汇率
    if re.search(r'(\d)(\.)(\d)(\d)', data) is not None:
        obj['price'] = re.search(r'(\d)(\.)(\d)(\d)', data).group()
    elif re.search(r'(\d)(\.)(\d)', data) is not None:
        obj['price'] = re.search(r'(\d)(\.)(\d)', data).group()
    else:
        return None

    #   数量
    result = re.sub(r'(\d)(\d)(\d)(\d)', "", data) #先去掉四位数
    if re.search(r'(\d)(\d)(\d)(\.)(\d)', result) is not None:
        amount = re.search(r'(\d)(\d)(\d)(\.)(\d)', result)
        obj['amount'] = amount.group()
    elif re.search(r'(\d)(\d)(\d)', result) is not None:
        amount = re.search(r'(\d)(\d)(\d)', result)
        obj['amount'] = amount.group()
    elif re.search(r'(\d)(\d)(\.)(\d)', result) is not None:
        amount = re.search(r'(\d)(\d)(\.)(\d)', result)
        obj['amount'] = amount.group()
    elif re.search(r'(\d)(\d)', result) is not None:
        amount = re.search(r'(\d)(\d)', result)
        obj['amount'] = amount.group()
    else:
        return None
    obj['time'] = int(time.time() * 1000)
    obj['uid'] = '10000000'
    obj['title'] = name + obj['brand'] + obj['amount'] + ',汇率' + obj['price']
    obj['msg'] = data

    try:
        file.writerow([
            obj['type'], obj['brand'], obj['amount'], obj['price'], obj['time'],
            obj['uid'], obj['title'], obj['msg']
        ])
    except:
        print('没有记录在csv')
    print(obj)
    result = cloudfunc.run('card',func=func,type=obj['type'],brand=obj['brand'],amount=obj['amount'],price=obj['price'],time=obj['time'],uid=obj['uid'],title=obj['title'],msg=obj['msg'])
    print(result)
    return obj


def get_image_info(data):
    pass


def get_goods_info(data,file):
    obj = {}
    name = ''
    func = 'goods'
    #   类型  出售 还是 求购
    if re.search('收', data) is not None:
        name = '求购'
        obj['type'] = 2
    elif re.search('求', data) is not None:
        name = '求购'
        obj['type'] = 2
    elif re.search('出', data) is not None:
        name = '出售'
        obj['type'] = 1
    else:
        return None
    #   商品名
    obj['brand'] = None
    for item in brand:
        result = re.search(item['name'], data)
        if result is not None:
            obj['brand'] = item['value']
    if obj['brand']:
        pass
    else:
        return None
    #   价格
    if re.search(r'(\d)(\d)(\d)(\d)', data) is not None:
        obj['price'] = re.search(r'(\d)(\d)(\d)(\d)', data).group()
    elif re.search(r'(\d)(\d)(\d)', data) is not None:
        obj['price'] = re.search(r'(\d)(\d)(\d)', data).group()
    elif re.search(r'(\d)(\d)', data) is not None:
        obj['price'] = re.search(r'(\d)(\d)', data).group()
    else:
        obj['price'] = None
    obj['msg'] = data
    obj['time'] = int(time.time() * 1000)
    obj['uid'] = '10000000'
    try:
        file.writerow([
            obj['type'], obj['brand'], obj['price'], obj['time'], obj['uid'],
            obj['msg']
        ])
    except:
        print('没有记录在csv')

    print(obj)
    result = cloudfunc.run(
        'card',
        func=func,
        type=obj['type'],
        brand=obj['brand'],
        price=obj['price'],
        time=obj['time'],
        uid=obj['uid'],
        msg=obj['msg'])
    print(result)
    return obj


def rcv_msg(uid, sender, gid, gname, content, file):
    try:
        file.writerow([gid, gname, uid, sender, content])
    except:
        print('没有记录在csv')
    # result = cloudfunc.run('rcv_msg', g=gid, s=gname, u=uuid, r=sender, c=content)
    # print(result)
