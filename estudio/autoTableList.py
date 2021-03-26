#coding:utf-8
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time,os,pyautogui

# 实例化
k = PyKeyboard()
m = PyMouse()

#回到全能机界面
def gotoestudio():
    m.click(469, 1060)  #需要调试
    time.sleep(2)
#重置界面，新建工程,没有弹保存提示框
def reset():
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(5)
# 重置界面，新建工程,弹保存提示框
def reset1():
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)
    m.click(1006,543)
    time.sleep(5)
def openlist():
    m.click(1000, 605)
    time.sleep(1)
    k.press_keys('test.csv')
    time.sleep(1)
    m.click(1270, 719)
    time.sleep(1)

#定义测试多条播单测试用例的方法
def test_multipleExercise():
    print('开始执行多条播单测试')
    #Ctrl+O打开工程
    k.press_key(k.control_key)
    k.press_key('o')
    k.release_key(k.control_key)
    time.sleep(1)
    # m.click(1007,544)autotabletest.pem
    k.press_keys('autotabletest.pem')
    time.sleep(1)
    m.click(1270,713)
    time.sleep(15)
    #导入播单
    m.click(994,607)
    time.sleep(1)
    k.press_keys('autotabletest.csv')
    time.sleep(1)
    m.click(1270,713)
    #20s执行播单
    a='asdfghjkqwe'
    time.sleep(5)
    for i in range(len(a)):
        # print(a[i])
        k.press_key(a[i])
        time.sleep(20)
#主界面按钮打开播单
def test_mainOpenList():
    print("第1条用例：播单主界面打开播单功能")
    openlist()
    print("第1条用例完成")
    time.sleep(5)
#主界面按钮保存-->直接保存
def test_mainSave1():
    print("第2条用例：播单主界面直接保存")
    m.click(1110,606)
    time.sleep(1)
    m.click(792,506)
    time.sleep(3)
    os.system(r'start explorer E:\media\tablelist')
    time.sleep(10)
    gotoestudio()
    print("第2条用例完成")
    time.sleep(10)
#主界面按钮保存-->打开后保存
def test_mainSave2():
    print("第3条用例：播单主界面打开后保存")
    #打开test.csv表单
    openlist()
    # 打开二级播单
    m.click(708,608)
    time.sleep(1)
    # 录制
    m.click(703,244)
    time.sleep(1)
    #鼠标拖拽
    pyautogui.mouseDown(934,202,button='left')
    time.sleep(1)
    # m.move(1683,444)
    pyautogui.moveTo(1683,444, duration=1)
    pyautogui.mouseUp(1683,444,button='left')
    time.sleep(1)
    #录制操作
    m.click(431,480)
    time.sleep(1)
    m.click(539,552)
    time.sleep(1)
    m.click(252,471)
    time.sleep(1)
    #鼠标拖拽回来
    pyautogui.mouseDown(1683, 444,button='left')
    time.sleep(1)
    # m.move(934, 202)
    pyautogui.moveTo(934, 202, duration=1)
    pyautogui.mouseUp(934, 202, button='left')
    time.sleep(1)
    #结束录制
    m.click(712, 244)
    time.sleep(1)
    #保存
    m.click(421,245)
    time.sleep(1)
    #退出二级播单
    m.click(1591,205)
    time.sleep(1)
    reset1()
    #再次打开test.csv播单
    openlist()
    # 打开二级播单
    m.click(708, 608)
    time.sleep(20)
    m.click(1591, 205)
    time.sleep(1)
    print("第3条用例完成")
    time.sleep(10)
#主界面按钮播放
def test_mainPlay():
    print("第4条用例：播单主界面播放")
    openlist()
    pyautogui.click(909,1021)
    time.sleep(5)
    pyautogui.click(865,693)
    time.sleep(1)
    pyautogui.click(909, 1021)
    time.sleep(5)
    print("第4条用例完成")
#主界面按钮上一个
def test_mainUpone():
    print("第5条用例：播单主界面上一个")
    openlist()
    #1.直接点击上一个按钮
    pyautogui.click(957,1017)
    time.sleep(3)
    #2.选中第三条点击上一个按钮
    pyautogui.click(886,720,duration=0.5)
    pyautogui.click(957,1017)
    time.sleep(3)
    #3.播放第一条后点击上一个按钮
    pyautogui.click(693,655)
    time.sleep(5)
    pyautogui.click(957, 1017)
    #4.播放第2条后点击上一个按钮
    pyautogui.click(688,694)
    time.sleep(5)
    pyautogui.click(957, 1017)
    print("第5条用例完成")
#主界面按钮下一个
def test_mainDownone():
    print("第6条用例：播单主界面下一个")
    openlist()
    # 1.直接点击下一个按钮
    pyautogui.click(1010,1023)
    time.sleep(3)
    # 2.选中第三条点击下一个按钮
    pyautogui.click(886, 720, duration=0.5)
    pyautogui.click(1010,1023)
    time.sleep(3)
    # 3.播放第一条后点击下一个按钮
    pyautogui.click(693, 655)
    time.sleep(5)
    pyautogui.click(1010,1023)
    # 4.播放最后一条后点击下一个按钮
    pyautogui.click(690, 942)
    time.sleep(5)
    pyautogui.click(1010,1023)
    print("第6条用例完成")
#主界面显示与执行
def mainShowAndExecute():
    print("第7条用例：主界面显示与执行")
    openlist()
    #点击播单的第一行的执行按钮
    pyautogui.click(693, 655)
    time.sleep(5)
    print("第7条用例完成")

#执行方法
gotoestudio()
reset()
test_mainOpenList()
reset()
test_mainSave1()
reset()
test_mainSave2()
reset1()
test_mainPlay()
reset1()
test_mainUpone()
reset1()
test_mainDownone()
reset1()
mainShowAndExecute()
reset1()
test_multipleExercise()
