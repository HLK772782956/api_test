# 主要实现的是用户添加，修改，删除和查询
from api.base import Base
from loguru import logger


class UserManager(Base):


    # 初始化接口路径
    def __init__(self):
        self.add_user_url = self.get_url('/admin/admin/create')
        self.edit_user_url = self.get_url('/admin/admin/update')
        self.search_user_url = self.get_url('/admin/admin/list?page=1&limit=20&sort=add_time&order=desc')
        self.delete_user_url = self.get_url('/admin/admin/delete')


    # 新增管理员
    def add_user(self,username,password,**kwargs):
        """
        请求的是添加管理员的接口
        :return: 添加管理员返回的json数据
        """
        # user_data这里是一个环境变量，每个方法里面都不会冲突
        user_data = {'username':username,'password':password}
        if kwargs:
            logger.info('添加管理员可选参数:{}',**kwargs)
            user_data.update(**kwargs)
        return self.post(self.add_user_url,user_data)



    # 查询管理员
    def search_user(self):
        """
        请求的是查询管理员接口
        :return:
        """
        return self.get(self.search_user_url)



    # 修改管理员
    def edit_user(self,id,username,password,**kwargs):
        """
        请求的是修改管理员接口
        :return: 返回的是修改管理员的json数据
        """
        user_data = {'id':id,'username':username,'password':password}
        if kwargs:
            logger.info('修改管理员可选参数:{}',**kwargs)
            user_data.update(**kwargs)
        return self.post(self.edit_user_url,user_data)





    # 删除管理员
    def delete_user(self,id,username,**kwargs):
        """
        请求的是删除管理员接口
        :return: 删除管理员返回的json数据
        """
        user_data = {'id':id,'username':username}
        if kwargs:
            logger.info('删除管理员可选参数:{}', **kwargs)
            user_data.update(**kwargs)
        return self.post(self.delete_user_url,user_data)


