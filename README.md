# 注意

this proj is for njupt's HarmongOS debelop Course Design

> 本项目是用flask框架搭建的聊天软件服务端框架
时间仓促没有使用websocket而是使用了简单的htt通信
项目的大部分内容已使用golang重写
这个仅仅作为思路和基本框架使用
可能会有bug

- 实现了简单的登录注册
- 信息的基本收发
- 包括个人用户信息
- 使用了Redis作为基本的缓冲层，帮助存储token和基本的信息
- 没有实现消息推送，这个功能预计在后续的golang版本中使用socket实现
- 功能较为简陋，仅仅作为思路，后续golang版本会对其进行完善

