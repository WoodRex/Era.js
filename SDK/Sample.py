# coding:utf-8
import time
# 【第1章 第1节 准备工作】
# 欢迎来到 Era.js 的示例程序！
# 通过阅读本程序，你将学习到关于使用 Era.js 进行纯文本游戏开发的一切！
# 我们话不多说，先引入Era.js引擎的后端库，如下列语句所示：
import erajs.api as a
# import 完毕之后，引擎的全部 API 就已经可以使用了。

# 接下来引入其他自定义代码，这个是自由的，下面的语句只是用于演示。
import logic.test as t
# 推荐将游戏逻辑/功能等代码放在【logic/】目录中，再用import导入。
# 但在此之前，我还是推荐你将游戏文件的版本作为变量定义在这里，如：
version = '0.1.0-190518'
# 【推荐】请不要在此处定义任何游戏变量，引擎会有专门的命名空间共开发者储存数据，以方便实现全局调用和获得数据持久性支持。（后文将会详细提到）

# 准备工作完成了之后，接下来就是游戏的正式逻辑了，请移步到本代码文件的最末尾，并找到【第1章 第2节 游戏初始化】，以继续阅读！


# --------------------------我是分割线----------------------------


# 【第2章 第2节 游戏封面（中）】
# 欢迎回来！现在我们继续介绍界面。
# 我们在底部代码中通过使用 API 中的 goto 函数进入了一个名为 cover 的界面，这个函数定义如下：
def cover():
    # 这样，我们就有一个名为 cover 的函数了，刚才也说了，我们通过函数来搭载界面，于是我们接下来准备显示该界面的标题：
    a.title('Erajs-Tutorial v{} with Era.js v{}'.format(version, a.version))
    # 上面调用了 API 中的 title 函数，其作用是更改前端窗口的标题文字，至于为什么放在 cover 函数里呢？
    # 其实只要 init 了之后，放在哪里都可以。放在这里只是防止可能会有其它的一些会导致标题修改的界面出现。

    # 一般来说，上文中的 title 函数只需要调用一次就可以了，更普遍的情况是，代表界面的函数的第一行，就是调用下列函数：
    a.page()
    # 这是 API 中的 page 函数。其作用是新建一个空页，以后新建的所有显示元素都将在此空页中摆放。直到另一个新页面生成。

    # 接下来就是显示页面标题：
    a.h('Erajs-Tutorial v{}'.format(version))
    # 上面调用了 API 中的 h(head) 函数，是用来显示页面标题的（其实就是字号比较大的文字啦！），其用法为：
    # a.h(text)

    a.t()  # 适当的换行会让您的界面更加美观

    # 再接下来就是显示一行普通文本：
    a.t('with Era.js v{}　aka{}'.format(a.version, a.aka))
    # 这是 API 中的 t(text) 函数。是用来显示普通文本的，其用法为：
    # a.t(text='', wait=False)
    # 当 text=='' 时，换行；
    # 当 wait==True 时，进入等待模式，文字会显示到这里就不再触发下一个语句，
    # 直到玩家点击鼠标左键（下一句）或是点击鼠标右键（略过全部）

    # 显示完标题之后，我们不希望将后续内容继续放在标题后边，于是选择换行：
    a.t()
    # 换两行也是可以的：
    a.t()

    # 接下来，我们希望显示一些按钮，来将玩家引向其他界面：
    # 再调用之前，我们先来看一下按钮函数是怎么使用的：
    # a.b(text, func, *arg, **kw)
    # 其中，text 就是你想显示在按钮上面的文字啦
    # func 就是该按钮在点击时会触发的函数
    # 还有几个隐藏的参数：
    # disabled 当该参数为真时，按钮变为不可用的状态
    # popup 鼠标指针移动到按钮上面时，将会弹出的文字
    # color 按钮颜色，值只能为：red，orange，yellow，olive，green，teal，blue，violet，purple，pink，brown，grey，black。
    a.b('页面逻辑教程', a.goto, ui_gui_logic)
    # 上面这个按钮函数，我们调用了 API 中的 goto 函数，并且将一个新页面的函数作为参数传给了它，
    # 这意味着当玩家点击这个按钮时，a.goto(ui_gui_logic) 语句将会被执行。
    a.t()  # 换行（换行不只是可以给文字用哦！按钮、评级、进度条等等都可以用的哦！）
    a.b('控件使用教程', a.goto, ui_all_components)
    a.t()  # 换行
    a.b('网格排版教程', a.goto, ui_grid)
    a.t()  # 换行
    a.b('游戏数据教程', a.goto, ui_data)
    a.t()  # 换行
    a.b('引擎模块/游戏脚本（Scripts）/DLC/MOD 教程', a.goto, ui_script)
    a.t()  # 换行
    a.b('退出引擎示例程序', a.exit)  # 正确的退出程序的方式


def ui_gui_logic():
    def change_page(page):
        # 在这里定义一个简单的换页逻辑
        a.clear_gui(1)  # 从引擎的界面逻辑中去除掉当前的页面
        a.goto(page)  # 进入一个新页面，该页面与原页面属于兄弟节点

    def page1():
        # 当一个子页面完全只属于一个父页面而不需要被其他页面调用时，
        # 可以将象征这个子页面的函数（如：page1）放在父函数（ui_gui_logic）内。
        a.page(color='#f00')  # 新建一个红色页面
        a.h('第一页（暨页面着色演示）')
        a.t()
        a.b('返回', a.back)
        a.b('下一页', change_page, page2)
        a.b('回到主界面', a.back, num=2)  # 向 back 传递参数 num，可以指定返回到第几个父节点。

    def page2():
        a.page(color='#0f0')  # 新建一个页面
        a.h('第二页（暨页面着色演示）')
        a.t()
        a.b('返回', a.back)
        a.b('上一页', change_page, page1)
        a.b('下一页', change_page, page3)
        a.b('回到主界面', a.back, num=2)

    def page3():
        a.page(color='#00f')  # 新建一个页面
        a.h('第三页（暨页面着色演示）')
        a.t()
        a.b('返回', a.back)
        a.b('上一页', change_page, page2)
        a.b('回到主界面', a.back, num=2)
    a.page()  # 新建一个页面
    a.h('页面逻辑展示')
    a.t()
    a.b('第一页', a.goto, page1)
    a.b('第二页', a.goto, page2)
    a.b('第三页', a.goto, page3)
    a.b('刷新', a.repeat)  # 当您需要刷新当前界面以显示某些游戏数据的变化时，请用这个方法。
    a.b('返回', a.back)
    a.t()
    a.b('清屏（慎用（请在使用时组合一下其他界面逻辑））', a.clear)


def ui_all_components():
    def button_result():
        a.page()
        a.h('作为一个按钮，我被按了。')
        a.t()
        a.b('返回', a.back)

    def rate_result(new_rate):
        print('当前评分为{}分。'.format(new_rate))

    def radio_result(new_ratio):
        print('现在选中了“{}”。'.format(new_ratio))

    def check_result(new_check):
        print('现在复选框的值为：{}'.format(new_check))

    def input_result(new_input):
        print('输入框中的值为：')
        print('{}'.format(new_input))

    def dropdown_result(new_dropdown):
        print('下拉菜单中的值为：“{}”。'.format(new_dropdown))

    def multi_dropdown_result(multi_dropdown):
        print('下拉菜单中的值为：“{}”。'.format('，'.join(multi_dropdown)))
    a.page()  # 新建一个页面
    a.h('控件一览（包括作为标题的我自己）', color='#f00', bcolor='#ff0')
    a.t()
    a.t('【我是几个文字】')
    a.t('【我跟在左边文字后面】')
    a.t()  # 换行
    a.t('【我被换行了……】')
    a.t('而我有色彩', color='#f00', bcolor='#ff0')
    a.t()  # 再换行
    a.t('【当你看见我时，你需要点鼠标左键或右键】', True)
    a.t()  # 再换行
    a.t('【当你看见我时，你还是需要点鼠标左键或右键】', True)
    a.t()  # 再换行
    a.b('我是一个红按钮', a.goto, button_result, color='red')
    a.b('我是一个不能按的红按钮', a.goto, button_result, color='red', disabled=True)
    a.b('快拿鼠标戳我！', a.goto, button_result, popup='被你戳到了，好爽~')
    a.b('我是振动器！', a.shake, 100)
    a.t()
    a.divider()  # 我是一个分割线
    a.t()
    a.t('作为进度条，我当前值为50，总共100，在界面上显示为 200px 长：')
    a.progress(50, 100, 200)
    a.t()
    a.t('如果给这个游戏引擎评分，5分满分，我给4分：')
    a.rate(4, 5)
    a.t()
    a.t('我是一个可以点的评分哦~点击之后请在后端控制台查看效果~（对着当前评分再点击一次可以取消评分哦~（等价于评0分））:')
    a.rate(2, 5, rate_result, False)
    a.t()
    a.t('我是一个单选，目前默认选中第二项（索引为1）修改之后请在后端控制台查看效果:')
    a.radio(['一', '二', '三'], radio_result, 2)
    a.t()
    a.t('我是一个复选框，目前默认已选中，修改之后请在后端控制台查看效果:')
    a.check('我是一个复选框哦！', check_result, True)
    a.t()
    a.t('我是输入框，修改之后请在后端控制台查看效果:')
    a.input(input_result, '我是默认值哦~')
    a.t()
    a.t('我是多行文本输入框，修改之后请在后端控制台查看效果:')
    a.t()
    a.input(input_result, '我是默认值哦~\n我还会换行~', True)
    a.t()
    a.t('我是一个下拉菜单哦！（下拉选择项目并在后端查看效果）:')
    a.dropdown(['甲', '乙', '丙'], dropdown_result, default='丙')
    a.t()
    a.t('我是一个多选下拉菜单哦！（下拉选择多个项目并在后端查看效果）:')
    a.dropdown(['甲', '乙', '丙', '丁', '戊'], multi_dropdown_result,
               multiple=True, default='戊')
    a.t()
    a.t('以上，就是目前支持的全部控件及用法啦~')
    a.t()
    a.t('如果您需要新增，请跟作者联系哦~')
    a.t()
    a.b('返回', a.back)


def ui_grid():
    def ui_grid_1():
        """
        作者: @m.l
        （有改动）
        """
        # ---------默认排版模式
        a.page()
        # 新页面
        a.mode()
        # 默认排版模式。
        a.h('一、默认排版', rank=4)
        a.t()
        a.t('由a.mode()切换排版模式。当前是默认排版，所有控件从左往右排列，使用a.t()进行换行。')
        a.t()
        a.b('按钮1')
        a.b('按钮2')
        a.t()
        a.b('按钮3')
        a.t()
        a.divider()
        a.b('下一页', ui_grid_2)
        a.t()
        a.b('返回', a.back)

        # 分割线

    def ui_grid_2():
        """
        作者: @m.l
        （有改动）
        """
        a.page()
        # 新页面
        a.h('二、网格排版【居中】', rank=4)
        a.mode('grid', 1)
        # 网格排版，示例一：居中控件
        apple = [
            '墙墙窗窗墙墙窗窗墙墙',
            '墙　　　　　　　　门',
            '墙　　　　　　　　墙',
            '墙汉汉汉汉　　　　墙',
            '墙　　　汉　　　　墙',
            '墙皂我　汉　　　　墙',
            '墙　　　汉　　　　门',
            '墙墙墙墙墙墙墙墙墙墙',
        ]
        a.t('该段文字居中，由a.mode("grid",1)切换为网格排版，参数‘1’为每一行所含的最大【控件集合】数')
        a.t()
        a.t('网格排版，在使用紧凑样式时，行间距离会比默认排版时更加紧密，因此你可以实现一些不可描述的场面')
        a.t()
        a.t('紧凑网格排版如下▼')
        a.t()
        a.mode('grid', 1, compact=True)
        for n in range(0, len(apple)):
            a.t(apple[n])
            a.t()
        a.mode()
        # 建议在使用完网格排版后，运行该代码，把排版模式切换回默认模式。
        a.t()
        a.divider()
        # 使用网格后，分割线的使用代码。
        a.b('上一页', ui_grid_1)
        a.b('下一页', ui_grid_3)
        a.t()
        a.b('返回', a.back)
        a.b('彩蛋', ui_egg)

    def ui_egg():
        """
        作者：@Miswanting
        """
        a.clear()
        for pic in a.data['data.ba']:
            a.page()
            a.mode('grid', 1, compact=True)
            for line in pic:
                a.t(line)
                a.t()
            time.sleep(0.1)
            a.clear()
        print('123')
        ui_grid_2()

    def ui_grid_3():
        """
        作者: @m.l
        （有改动）
        """
        a.page()
        a.h('三、网格排版【网格】', rank=4)
        a.t()
        a.t('【默认样式】')
        # ---------网格排版模式
        a.mode('grid', 3)
        # 网格排列，一行3列
        a.b('按钮1')
        a.b('按钮2')
        a.t()
        a.b('按钮3')
        a.t()
        a.b('按钮4')
        a.t()
        a.b('按钮5')
        a.t()
        a.b('按钮6')

        a.mode()
        a.t()
        a.t('【线框样式】')
        a.mode('grid', 3, celled=True)
        # celled,带
        a.b('按钮1')
        a.b('按钮2')
        a.t()
        a.b('按钮3')
        a.t()
        a.b('按钮4')
        a.t()
        a.b('按钮5')
        a.t()
        a.b('按钮6')

        a.mode()
        a.t()
        a.t('【紧凑样式】')
        a.mode('grid', 3, compact=True, celled=True)
        a.b('按钮1')
        a.b('按钮2')
        a.t()
        a.b('按钮3')
        a.t()
        a.b('按钮4')
        a.t()
        a.b('按钮5')
        a.t()
        a.b('按钮6')
        a.mode()
        a.t()
        a.divider()
        a.b('上一页', ui_grid_2)
        a.t()
        a.b('返回', a.back)
    ui_grid_1()


def ui_data():
    def change_rate(new_rate):
        a.data['db']['rate'] = new_rate
    a.page()  # 新建一个页面
    a.h('游戏数据教程')
    a.t()
    a.t('游戏的静态数据都保存在【data/】目录中，只要放进去了，且格式匹配，就可以在游戏开始后直接调用。如：')
    a.t(a.data['data.姓名库']['外文']['男名'][0])
    a.t('←这里请翻阅代码')
    a.t()
    a.t('支持的格式为json，csv，ini，inf，cfg，config等。而且在加载的时候后都已经被自动转换为了Dict等方便的格式。')
    a.t()
    a.t('【a.data是游戏引擎的数据核心，类型为Dict。里面定义的变量都可以被全局调用，但不会被保存】')
    a.t()
    a.divider()
    a.t()
    a.t('【接下来介绍几个特殊的Key】')
    a.t()
    a.t('【a.data["data.*"]】存放着【data/】目录下所有的静态数据；')
    a.t()
    a.t('【a.data["config.*"]】存放着【config/】目录下所有的设置；')
    a.t()
    a.t(
        '【以上两种KEY使用点语法来对具体文件进行调用，如【data/姓名库.json】文件中的内容保存在【a.data["data.姓名库"]】中')
    a.t()
    a.divider()
    a.t()
    a.t('【a.data["db"]】中存放着可以被保存和读取的数据。（其他KEY中的数据都不会被保存）')
    a.t()
    a.t('演示(请修改，保存，再修改，加载。看数值是否被保存了。)：')
    a.rate(a.data['db']['rate'], 5, change_rate, False)
    a.t()
    a.divider()
    a.t()
    a.t('【a.data["class"]】保存着各种Class，属于预留。大家暂时可以忽略。')
    a.t()
    a.t('【a.data["api"]】保存着各种API，大家可以在这里加入自定义的API，然后进行全局调用（一般用于引擎插件/Script/DLC/Mod中）。')
    a.t()
    a.t('【entity】保存着各种Class的实例，属于预留。大家暂时可以忽略。')
    a.t()
    a.divider()
    a.t()
    a.b('保存', a.goto, save_game)
    a.b('加载', a.goto, load_game)
    a.b('返回', a.back)


def ui_script():
    a.page()
    a.h('引擎模块/游戏脚本（Scripts）/DLC/MOD 教程')
    a.t()
    a.t('你可以普通的调用其他包中的函数（你可以打开【logic/test.py】文件看看）：')
    a.b('logic', a.goto, t.test_page)
    a.t()
    a.t('也可以调用Script中的函数（但是复杂一点）（你可以打开【script/test.py】文件看看）：')
    a.b('script', a.goto, a.data['api']['test_page'])
    a.t()
    a.t('值得一提的是，除了script目录下的文件会自动加载以外，其他目录下如引擎脚本/DLC/MOD等，均需要再config文件中标记开启才能够被自动加载。')
    a.t()
    a.t('我们约定：')
    a.t()
    a.t('1. 引擎脚本暂时不要开发，有需要可以向我反映；')
    a.t()
    a.t('2. DLC仅用于游戏内容/数据增量更新；')
    a.t()
    a.t('3. MOD仅用于游戏临时修改；')
    a.t()
    a.t('4. Script仅用于游戏小量更新或脚本开发。')
    a.t()
    a.b('返回', a.back)


def save_game():
    # 保存游戏界面
    a.page()
    a.h('保存游戏')
    a.t()
    a.show_save_to_save()  # 显示当前存档以供保存
    a.b('返回', a.back)


def load_game():
    a.page()
    a.h('读取游戏')
    a.t()
    a.show_save_to_load(cover)  # 显示当前存档以供加载（参数为加载之后进入哪个界面（最好是根界面））
    a.b('返回', a.back)


# 【第1章 第2节 游戏初始化】
# 欢迎回来！接下来，我将为您介绍游戏的初始化。
# 游戏的初始化是全自动的，你只需要调用 API 中的这个函数：
a.init()
# 就可以实现对游戏引擎的初始化。
# 在初始化的过程中，将会依次进行以下行动
# 01. 统一全局路径
# 02. 自检（初始化游戏数据架构；检测运行必要目录是否存在；检测运行必要文件是否存在；若不存在就创建并初始化之）
# 03. 载入游戏设置（设置数据默认保存于 "config/config.ini" 文件中）
# 04. 在游戏数据架构中注册引擎 API，以实现一些不常用的骚操作。（这一个步骤可暂时忽视）
# 05. 扫描引擎插件。（引擎插件存放于 "erajs/plugin/" 目录中）
# 06. 加载引擎插件。（当检测到目录中存在该引擎插件，且在游戏设置数据中该插件处于启用的状态下，则自动加载并运行。）
# 07. 连接到前端服务器。（在执行此命令之前，前端程序应已经打开。）
# 08. 推送游戏设置至前端服务器。（游戏开发者可暂时忽视）
# 09. 加载游戏数据文件（游戏数据文件保存在 "erajs/plugin/" 目录中，该目录下的一切受支持的文件都将自动扫描并加载到游戏数据架构中，一旦载入，即可全局调用。）
# 10. 扫描游戏脚本文件。（游戏脚本文件是指实现独立功能、数据改动或与实现游戏主要逻辑无关的小文件）
# 11. 加载游戏脚本文件。（所有被扫描到的游戏脚本文件都将被在此时加载）
# 12. 扫描DLC。（机制同扫描引擎插件）
# 13. 加载DLC。（机制同加载引擎插件）
# 14. 扫描MOD。（机制同扫描DLC）
# 15. 加载MOD。（机制同加载DLC）
# 16. 向前端发送加载完成信号，准备显示游戏封面。
# 至此，游戏引擎初始化完毕！
# 【注意】API 中的绝大部分函数都应在 init 函数调用之后调用，不然会报错。init 函数只需要执行一次。

#########################################################################
a.data['db']['rate'] = 3  # 这个语句是用来做保存加载展示用的，作为教程请无视。#
#########################################################################

# 【第2章 第1节 游戏封面（上）】
# 在这里，请允许我向您介绍游戏的界面逻辑。
# 一般的，Era类游戏的界面与界面之间的逻辑是树状的逻辑，如：
# 封面
#   ├─ 开始游戏
#   │    ├─ 使用默认人物
#   │    └─ 新建自定义人物
#   ├─ 读取游戏
#   ├─ 游戏设置
#   └─ 退出游戏
# 或是：
# 游戏循环主界面
#   ├─ 探险
#   │    ├─ 查看敌人
#   │    └─ 战斗
#   ├─ 查看人物
#   ├─ 商店
#   └─ ？？？
# 但在实际开发过程中，界面与界面之间的逻辑常常会比较混乱，如：
# 从一个界面到另一个界面的转换，常常是通过显式调用的方式，这种方式有以下不方便的地方：
# 1. 上一界面应当知道自己将显示流引入了哪一个界面，才能够实现进入某一页面的逻辑
# 2. 下一个界面必须知道显示流是从哪一个界面来的，才能够实现返回上一页面的逻辑
# 因此，要实现一个进入该页面/退出到上一页面的操作，就常常需要把两个页面写死，这样就带来了开发的成本提高，降低了灵活度。
# Era.js 引擎内置了游戏界面管理机制，你只需要写出每个界面所包含的内容，并通过合适的方式进行调用，
# 游戏引擎就会自动对界面逻辑进行记忆，从而简单实现进入页面/退出到上一页面/上一页/下一页/返回根页面等操作。

# 现在，我们对其进行详细讲解：
# 我们提出了一个概念：界面=函数
# 即将一个页面绑定在一个函数上。如以下语句所示：
a.goto(cover)
# 我们调用了 API 中的 goto 函数，并指向了另一个名为 cover 的函数，
# 这样，我们就进入了我们的页面体系的首个页面：cover
# 接下来，请将本文件中的代码滚动到顶端，寻找【第2章 第2节 游戏封面（下）】并继续阅览！
