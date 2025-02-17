DEBUG = True
# 服务默认端口
PORT = 8000
# 数据库配置
DB_HOST = 'web_mysql'
DB_PORT = 3306
DB_NAME = 'insight2'
DB_USER = 'root'
DB_PASS = 'crediteaseitsec'
# Redis配置
REDIS_HOST = 'web_redis'
REDIS_PORT = 6379
REDIS_PASS = 'crediteaseitsec'
REDIS_DB = 0
REDIS_CHANNEL = "SERVICE_CHANNEL"


ACTION_DIR_NAME = ("action", )

STATIC_DIR_NAME = "static"

TEMPLATE_DIR_NAME = "template"

COOKIE_SECRET = "U2FsdGVkX1/u1YaeTuRdWM9adoqFpGm9seFRccbhRR/O2qyTwP78Cok="
COOKIE_EXPIRES_DAYS = 30
# 接口前缀
API_VERSION = "/api"
# 洞察1  数据迁移使用，可不做配置，如果进行数据迁移，请配置成洞察1数据库信息。
FROM_DB = dict(
            host = 'web_mysql',
            port = 3306,
            user = "root",
            password = "crediteaseitsec",
            database = "insight"
        )

