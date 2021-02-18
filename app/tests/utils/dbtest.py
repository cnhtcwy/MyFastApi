from app.db.session import SessionLocal
from app.utils.tools_func import serialize_sqlalchemy_obj


def get_db():
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        print('获取数据库会话')
        yield db
    finally:
        db.close()
        print('数据库关闭')
def fun():
    try:
        print('1')
        db = 'SessionLocal()'
        yield db
    finally:
        print('3')
# db 是 sqlalchemy会话对象
# sql = 'SELECT * FROM sys_authorities'
#
# site_info = db.execute(sql).fetchall()
if __name__ == '__main__':
    sql = 'SELECT * FROM sys_authorities'
    for db in get_db():
        site_info = db.execute(sql).fetchall()
        print('执行查询')
        print(site_info)
        print(serialize_sqlalchemy_obj(site_info))