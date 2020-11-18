# -*- coding:utf-8 -*-

# 引入依赖库
import pyautogui as pag
import clipboard as cb
import pandas as pd
import os
import sys


def locate():
    """定位关键点"""
    tbox = pag.locateOnScreen("wechat/data/top.png")
    cbox = pag.locateOnScreen("wechat/data/contact.png") if pag.locateOnScreen(
        "wechat/data/contact.png") else pag.locateOnScreen(
            "wechat/data/contact2.png")
    bbox = pag.locateOnScreen("wechat/data/bottom.png")
    abox = pag.locateOnScreen("wechat/data/A.png")

    return tbox, cbox, bbox, abox


def cal_pos(cbox, bbox, abox):
    """计算点击位置"""
    # 联系人图标位置
    cc = pag.center(cbox)
    # 第一个联系人位置
    if abox is None:
        print("Guess contact from contact icon.")
        acx = cc[0] + 40
        acy = cc[1] - 50
    else:
        acx, acy = pag.center(abox)
    fc = (acx + 20, acy + 50)
    # 底部点击位置
    bc = pag.center(bbox)
    return cc, fc, bc


def is_bottom(cur_y, bom_y):
    """判断是否到达底部"""
    return cur_y > (bom_y + 80)


def gender():
    """获取性别"""
    if pag.locateOnScreen("data/female.png"):
        return 'female'
    elif pag.locateOnScreen("data/male.png"):
        return 'male'
    else:
        return ""


def nick_name_and_signature(tc, drag_speed):
    """获取微信昵称和签名"""
    box = pag.locateOnScreen("data/sep.png")
    rx, ry = pag.center(box)
    tcx, tcy = tc[0], tc[1]
    pag.moveTo(rx, ry, 0.1)
    pag.dragTo(tcx + 50, tcy + 50, drag_speed)
    text = copy()

    pag.click()
    if text:
        li = text.split("\n")
        if len(li) > 1:
            return li[0], li[1]
        else:
            return text, ""
    else:
        return "", ""


def copy():
    """复制内容：非重复性拷贝"""
    ori_text = str(cb.paste()) if cb.paste() else ""
    pag.hotkey('ctrl', 'c')
    text = str(cb.paste()) if cb.paste() else ""
    if text != ori_text:
        return text
    else:
        return ""


def district(drag_speed):
    """获取地区"""
    box = pag.locateOnScreen("data/dis.png") if pag.locateOnScreen(
        "data/dis.png") else pag.locateOnScreen("data/dis2.png")
    if box:
        cx, cy = pag.center(box)
        pag.moveTo(cx, cy, 0.1)
        pag.dragTo(cx + 400, cy + 20, drag_speed)
        text = copy()
        pag.click()
        if text:
            return text
        else:
            return ""
    else:
        return ""


def from_(drag_speed):
    """好友来源"""
    box = pag.locateOnScreen("data/from.png") if pag.locateOnScreen(
        "data/from.png") else pag.locateOnScreen("data/from2.png")
    if box:
        cx, cy = pag.center(box)
        pag.moveTo(cx, cy, 0.1)
        pag.dragTo(cx + 400, cy + 20, drag_speed)
        pag.hotkey("ctrl", "c")
        text = cb.paste()
        pag.click()
        if text:
            return text
        else:
            return ""
    else:
        return ""


def wx_id(drag_speed):
    """获取微信id"""
    box = pag.locateOnScreen("data/wx-id.png") if pag.locateOnScreen(
        "data/wx-id.png") else pag.locateOnScreen("data/wx-cn-id.png")
    if box:
        cx, cy = pag.center(box)
        pag.moveTo(cx, cy, 0.1)
        pag.dragTo(cx + 400, cy + 20, drag_speed)
        pag.hotkey("ctrl", "c")
        text = cb.paste()
        pag.click()
        if text:
            return text
        else:
            return ""
    else:
        return ""


def click(tbox, cbox, bbox, abox, gap, drag_speed, out, is_all):
    """模拟点击"""
    cc, fc, bc = cal_pos(cbox, bbox, abox)
    # 点击联系人图标
    pag.click(cc)
    # 循环点击用户列表
    btm_y = bc[1]
    # 当前工作位置
    curr_x = fc[0]
    curr_y = fc[1]
    # 循环滚动点击
    cnt = 0
    IDs = []  # 记录ID列表
    scroll_flag = True  # 滚动标记
    same_list = []  # 记录入库值
    Info = {
        "WechatID": [],
        "From": [],
        "District": [],
        "Gender": [],
        "NickName": [],
        "Signature": [],
    }  # 存储用户信息
    while not is_bottom(curr_y, btm_y):
        pag.moveTo(curr_x, curr_y, 0.1)
        pag.click()
        _id = wx_id(drag_speed)
        if _id != "":
            IDs.append(_id)
            Info["WechatID"].append(_id)  # id
            if is_all:
                _from = from_(drag_speed)  # 来源
                Info["From"].append(_from)
                dis = district(drag_speed)  # 地区
                Info["District"].append(dis)
                g = gender()  # 性别
                Info["Gender"].append(g)
                tc = pag.center(tbox)
                nick_name, signature = nick_name_and_signature(
                    tc, drag_speed)  # 昵称、签名
                Info["NickName"].append(nick_name)
                Info["Signature"].append(signature)
            else:
                Info["From"].append("")
                Info["District"].append("")
                Info["Gender"].append("")
                Info["NickName"].append("")
                Info["Signature"].append("")
            save(out, Info, "contacts")
            cnt += 1
            print("{} WechatID:{}".format(cnt, Info["WechatID"][-1]))
        else:  # 未找到信息，滚动
            print("Nothing found.")
            pag.moveTo(curr_x, curr_y, 0.1)
            pag.scroll(int(-1 * gap * 1.2))
            continue
        # 获取信息完毕，滚动
        if scroll_flag:
            if len(same_list) < 3:
                same_list.append(_id)
            elif len(set(same_list)) == 1:
                scroll_flag = False
            else:
                same_list.pop(0)
                same_list.append(_id)
        if scroll_flag:  # 滚动状态
            pag.moveTo(curr_x, curr_y, 0.1)
            pag.scroll(int(-1 * gap * 1.2))
        else:  # 结束滚动
            curr_y += gap


def save(out, data, sheet):
    """保存结果"""
    writer = pd.ExcelWriter(out)
    df = pd.DataFrame(data)
    df2 = df.drop_duplicates(subset=None, keep='first', inplace=False)
    df2.to_excel(writer, sheet, index=False)
    writer.save()
    return True


def main(out, is_all):
    """主程序执行入口"""
    # 执行文件判重，重复则序号增1
    file_name, rear = os.path.splitext(out)
    cnt = 1
    while os.path.isfile(out):
        out = file_name + "_" + str(cnt) + rear
        cnt += 1
    print("Locating...")
    tbox, cbox, bbox, abox = locate()  # 定位
    if tbox is None or cbox is None or bbox is None:
        print(
            "tbox:{} cbox:{} bbox:{} abox:{} .\nCould not locate box position.Try again."
            .format(tbox, cbox, bbox, abox))
        return
    click(tbox, cbox, bbox, abox, 100, 0.4, out, is_all)  # 开始运行
    print("All done.")


if __name__ == "__main__":
    out = "contacts.xlsx"  # 保存地址
    out = os.path.abspath(out)
    args = sys.argv
    if len(args) < 2:
        main(out, False)
    elif args[1] == "all":
        main(out, True)
    else:
        main(out, False)