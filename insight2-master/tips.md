### 目录介绍 ###
```
├── action                                               //RequestHandler接口文件
├── init                                                 // 数据库初始化sql
├── logic                                               // 逻辑代码
├── logs                                                // 日志目录
├── static                                             // 前端编译完成将dist/static下的静态文件拷贝到此目录;将index.html拷贝到此目录下
│   ├── css
│   ├── fonts
│   ├── img
│   └── js
├── template
├── tornadoweb                                         // tornado 封装
├── transfer_data                                  // 数据迁移

```
### backend 服务启动 ##

``` python
python run.py --config=settings.py --port=8000    
python service.py --config=settings.py  
启动linux系统cron服务
``` 
或者
``` 
supervisord -c supervisord.conf
``` 
