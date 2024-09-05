from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# Base是用来给模型类继承的
Base = declarative_base()

# 创建同步数据库引擎
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI,
                       pool_recycle=7200,
                       pool_size=100,  # 连接池最多个数
                       pool_pre_ping=True,
                       )

# 创建会话，autocommit自动提交，autoflush 自动刷新，bind 绑定创建的引擎
Session = sessionmaker(bind=engine)

# 向数据库发出建表完成类与表的映射
Base.metadata.create_all(engine)


# engin e =create_engine(
#     "mysql+pymysql://root:xxxx@1.2.2.3:3306/db",
#     pool_size=100,  # 连接池最多个数
#     pool_recycle=3600,  # 若设置-1 则链接永久有效，但是mysql sever 会有默认链接时间8H 超时会自动断开
#     pool_pre_ping=True,  # 是否在使用连接前先进行ping。强烈建议带上。
#     pool_timeout=30,
# )
# DBSession = sessionmaker(bind=engine)  # 可以加上自动提交的参数，能避免之后的很多问题
# dbsession = DBSession()
#
# # 如果加上了自动提交参数，本文的以后内容可以不用再看了。
# # 但是如果有些场景需要手动提交事务，那么下文的问题就极其容易出现
