# wordCloud
根据聊天记录生成词云
将微信聊天记录导出成文档，知乎上有很多种方法，其中主要是两类，第一种是通过root手机，获取权限；第二种为通过Apple iTunes 备份。

这里选择第二类方法（小米note3不支持root），而我刚好有一个ipad，所以先把聊天记录全部复制到ipad，然后曲线救国了，具体过程也较为简便，感谢知乎**@hangcom**提供的免费工具，万分。
具体过程可移步查看https://zhuanlan.zhihu.com/p/32511173，不再赘述。

导出后，生成文件夹，包含视频、图片和聊天内容子文件，其中视频图片不再多说，单说聊天内容。
聊天内容HTML网页文件，文字内容以js格式保存，名为‘message’的JavaScript文件。
这里需要先将js文件用文本编辑器以txt格式打开，打开后显示包含中英文及各种字符。
本文的message.txt即是将获得的js文件去除非中文信息所得。
接下来处理就是如代码所示了
