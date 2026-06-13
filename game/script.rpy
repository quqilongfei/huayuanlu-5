label splashscreen:

    $ renpy.movie_cutscene("video/kaitou.webm")

    return

## 主菜单背景：用 ATL 在同一 image 内切换，叠化才会播放。
## （ConditionSwitch + restart_interaction 会每次新建显示able，过渡永远不会出现。）
define gui.MM_BG_HOLD = 6.0
define gui.MM_BG_DISSOLVE = 1.0

image cycling_main_menu_bg:
    "zhujiemian.png"
    pause gui.MM_BG_HOLD
    block:
        "bg2.png" with Dissolve(gui.MM_BG_DISSOLVE)
        pause gui.MM_BG_HOLD
        "bg3.png" with Dissolve(gui.MM_BG_DISSOLVE)
        pause gui.MM_BG_HOLD
        "zhujiemian.png" with Dissolve(gui.MM_BG_DISSOLVE)
        pause gui.MM_BG_HOLD
        repeat
# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("旁白")
define j = Character("吉鸿昌")
define d = Character("地下党员")
define a = Character("爱国志士")
define t = Character("特务")
define g = Character("刽子手")
define jj = Character("讲解员")
define c = Character ("参观者")
define flag=0
image 呆猫生气:
     "images/生气呆猫.png"
     yanchor 0.5
     ypos 600
image 现代旧居:
     "images/现代旧居.png"
image 讲解员:
     "images/讲解员.png"
image 1932guju:
     "images/1932年的故居.jpg"
     xalign 0.5
     yalign 0.5
     zoom 1.6

image jimage:
    "images/吉鸿昌2.png"
    zoom 0.55
    xanchor 0.5
    yanchor 0.5
    xpos 400
    ypos 700

image dimage:
    "images/地下党员1.png"
    xanchor 0.5
    yanchor 0.5
    xpos 1600
    ypos 900
image aimage:
    "images/爱国志士.png"
    xanchor 0.5
    yanchor 0.5
image 特务:
    "images/特务.png"
    xanchor 0.5
    yanchor 0.5
image 参观者:
    "images/参观者.png"
    xanchor 0.5
    yanchor 0.5
image 刽子手:
    "images/刽子手.png"
    xanchor 0.5
    yanchor 0.5
image 天津国民饭店:
    "images/天津国民饭店.png"
image 刑场:
    "images/刑场.png"
image 场景1:
    "images/场景1.png"
image 红:
    "images/红.png"
image 坚定的吉鸿昌:
    "images/吉鸿昌3.png"
# 游戏在此开始。

label s5:
    play music "TheRussian-Various Artists.mp3" fadein 1.0
    scene 1932guju
    with fade

    "1932年冬，天津法租界花园路5号，一座红砖小楼内，吉鸿昌刚刚从上海来到这里。"
    show jimage:
        zoom 1.4
        xanchor 0.5
        yanchor 0.5
        xpos 960
        ypos 500
    with dissolve
    j "这座小楼要改造成我们的秘密联络站，每层都要设密室，会议室要多开门，方便同志们疏散！"
    hide jimage
    show dimage
    with dissolve
    d "吉将军，您散尽家财购买武器，还亲自印制《民族战旗》，真是为抗日救国费尽心血！"
    show jimage at left
    with dissolve
    j "国家危难之际，个人安危和财产又算得了什么！只要能抗日救国，我吉鸿昌万死不辞！"
    scene 1932guju
    "从此，这座红楼成为了华北地区抗日救亡运动的重要指挥中心，灯光常常彻夜通明。"
jump fenzhi
return
label s2:
    stop music fadeout 1.0
    scene 1932guju with fade
    play music "Threatened in Havana-Tim Wynn.mp3" fadein 1.0
    "1934年，吉鸿昌在红楼秘密成立中国人民反法西斯大同盟，联合各抗日力量。"
    show jimage:
        zoom 1.4
        xanchor 0.5
        yanchor 0.5
        xpos 960
        ypos 600
    with dissolve
    j "我们要联合全国一切抗日力量，不管是哪个党派、哪个团体，只要愿意抗日，就是我们的同志！"
    hide jimage
    show aimage:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    with dissolve
    a "吉将军，我们愿意跟随您，为抗日救国贡献自己的一份力量！"
    hide aimage
    show jimage
    with dissolve
    j "好！让我们共同努力，把日本侵略者赶出中国去！"
jump jixu
return
label s3:
    stop music fadeout 1.0
    scene 天津国民饭店 with fade
    play music "Revolver-Duane Decker.mp3" fadein 1.0
    "1934年11月9日，天津国民饭店45号房间，吉鸿昌正在等待与爱国人士会谈。"
    show 特务:
        xalign 0.5
        ypos 700
        zoom 1.0
    with dissolve
    t "吉鸿昌！你跑不了了！"
    hide 特务 with dissolve
    show jimage:
        zoom 1.3
        xpos 1000
        ypos 550
    with dissolve
    j "（身中数弹仍挣扎）你们这些卖国贼！休想阻止抗日救国的大业！"
    hide jimage with dissolve
    "吉鸿昌因伤势过重被捕，被押往国民党51军军部。"
    show 特务:
        xalign 0.5
        ypos 700
        zoom 1.0
    with dissolve
    t "吉鸿昌，只要你放弃抗日主张，供出共产党的秘密，我们就放你一条生路！"
    hide 特务 with dissolve
    show jimage:
        zoom 1.3
        xpos 1000
        ypos 550
    with dissolve
    j "休想！我吉鸿昌生为抗日生，死为抗日死，绝不会向你们屈服！"
jump s4
return

label s4:
    stop music fadeout 1.0
    play music "The Tale of a Cruel World-DM DOKURO.mp3" fadein 1.0
    scene 刑场 with fade
    "1934年11月24日，北平陆军监狱刑场，吉鸿昌写下绝笔诗后，从容赴死。"
    show 坚定的吉鸿昌:
        zoom 1.0
    with dissolve
    j "（朗诵绝笔诗）恨不抗日死，留作今日羞。国破尚如此，我何惜此头！"
    hide 坚定的吉鸿昌 with dissolve
    show 刽子手:
        xanchor 0.5
        yanchor 0.5
        xpos 960
        ypos 700
        zoom 1.0
    with dissolve
    g "吉鸿昌，跪下受刑！"
    hide 刽子手 with dissolve
    show 坚定的吉鸿昌:
        zoom 1.0
    with dissolve
    j "我为抗日而死，死得光明正大，不能跪下挨枪！我死了也不能倒下！"
    j "（高呼）打倒日本帝国主义！中国共产党万岁！"
    hide 坚定的吉鸿昌 with dissolve
    "随着一声枪响，吉鸿昌将军壮烈牺牲，年仅39岁。他的爱国精神永垂不朽！"
jump jixu2
return
label start:
    stop music fadeout 1.0
    scene 场景1 with fade
    pause 2.0
    play music "China (The Atomic Era)-Geoff Knorr, Phill Boucher.mp3" fadein 3.0
    scene 现代旧居 with fade
    "这里是天津市和平区花园路5号的红楼，已成为重要的爱国主义教育基地。"
    show 讲解员:
        zoom 2.0
        xpos 1400
        ypos 400
    with dissolve
    jj "各位游客，这座红楼就是抗日民族英雄吉鸿昌将军当年的居所和秘密联络站。"
    jj "在这里，发生了许多可歌可泣的事迹。"
    hide 讲解员 with dissolve
    label fenzhi:
    menu:
        "要去探寻哪段历史？"
        "1932年的故居": 
            $flag=1
        "1934年的故居": 
            $flag=2
        "钝角":
            $flag=3
    if flag==1:
        jump s5
    elif flag==2:
        jump s2
    elif flag==3:
        stop music
        scene 红
        show 呆猫生气
        "好好作答！"
        jump start
label jixu:
    scene 现代旧居 with fade
    jj "然而在1934年的11月，不幸发生了"
jump s3
label jixu2:
    scene 现代旧居 with fade
    show 参观者:
        zoom 1.5
        xanchor 0.5
        yanchor 0.5
        xpos 400
        ypos 650
    with dissolve
    c "吉将军「做官即不许发财」的名言，真是令人敬佩！"
    hide 参观者 with dissolve
    show 讲解员:
        zoom 1.5
        xpos 1400
        ypos 500
    with dissolve
    jj "是的，吉将军用生命诠释了爱国与忠诚，他的精神激励着一代又一代中国人。"
    hide 讲解员 with dissolve
    "吉鸿昌将军的故事在天津广为流传，成为中华民族宝贵的精神财富。"
    "他的精神将永远激励我们为实现中华民族伟大复兴的中国梦而努力奋斗！"
menu:
    "播放制作员名单":
        $ renpy.movie_cutscene("video/演职员表.webm")
return




