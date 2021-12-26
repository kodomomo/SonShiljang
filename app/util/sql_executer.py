from abc import ABC, abstractmethod
from pymysql.cursors import DictCursor
from config import DbConfig
import pymysql


class SqlExecuter(ABC): pass


class SqlExecuterImpl(SqlExecuter):

    def __init__(self, host, port, user, password, charset):
        self.__db = pymysql.connect(
            host=host,
            port=port,
            charset=charset,
            database='kodomo_dragon',
            autocommit=True,
            user=user,
            password=password
        )
        self.cursor = self.__db.cursor(DictCursor)

    def insert_bot(self, bot_id: str, psid: str):
        uuid = "unhex(replace(uuid(),'-',''))"
        self.cursor.execute(
            f'insert into bot(id,name,created_at,psid) values({uuid},"{bot_id}",now(),"{psid}")'
        )
        self.__db.commit()


    def update_bot_repo_id(self, repo_id: str, bot_name: str, psid: str):
        psid = self.add_double_quotation_mark(psid)
        self.cursor.execute(
            f'UPDATE bot set repo_id="{repo_id}", where name="{bot_name}" and  psid="{psid}"'
        )

    def insert_repository(self): pass

    def delete_bot_from_repo(self): pass

    def delete_repo_from_bot(self): pass

if __name__ == '__main__':
    a = SqlExecuterImpl(
        DbConfig.HOST,
        DbConfig.PORT,
        DbConfig.USER,
        DbConfig.PASSWORD,
        DbConfig.CHARSET
    )

    a.insert_bot('sdf','asdf')