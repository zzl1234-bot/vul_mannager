#!coding=utf-8
import os
import time
import json
from hashlib import md5
from datetime import datetime

import xlwt
import xlrd
from playhouse.shortcuts import model_to_dict

from tornadoweb import *
from logic.model import *
from logic.utility import *
from logic.define import *
from logic.util import *
import pypandoc

from docx import Document
from docx.shared import Cm
import zipfile

# 我的项目
@url(r"/project/my/list", needcheck = False, category = "项目")
class ProjectMy(LoginedRequestHandler):
    """
        项目列表

        search: 查询条件
        project_status: 漏洞状态 0:待处理, 1:已完成
        page_index: 页码
        page_size: 每页条数
        sort: 排序字段
        direction: 排序方向[asc, desc]ending
    """

    def get(self):
        search = self.get_argument('search', None)
        project_status = self.get_argument('project_status', "")
        project_type = self.get_arguments('project_type')
        page_index = int(self.get_argument('page_index', 1))
        page_size = int(self.get_argument('page_size', 10))

        sort = self.get_argument('sort', None)
        # 方向 desc
        direction = self.get_argument('direction', '')
        cond = []
        '''
        获取用户id-》组id-》role角色
        1）如果是渗透人员，只能看到自己组内的项目
        2）如果是安全员或者管理员，看到全部
        3）其他人员，不允许
        '''
        if sort:
            # add by wuq
            sort = getattr(Project, sort)
            direction = direction.replace("ending", "")
            if direction == 'desc':
                sort = sort.desc()
        else:
            sort = Project.project_id.desc()

        if project_status == "0":
            cond.append(Project.project_status.in_([0]))
        elif project_status == "1":
            cond.append(Project.project_status.in_([1]))
        else:
            cond.append(Project.project_status.in_([0, 1]))

        if search:
            # mod by wuq
            cond.append((Project.project_name.contains(search)))

        # 管理员， 安全员角色，以及本项目的负责人/管理员可以查看项目
        role = User.get_or_none(User.id == self.uid)
        if not role:
            return self.write(dict(status=False, msg='校验用户失败'))

        if role.role_id == 4:
            group_ids = []
            # 角色是渗透人员可以查看组管理owner_id以及组内的user_id为自己的项目情况
            groups = Group.select().where(Group.owner_id == self.uid)
            group_ids = [item.id for item in groups]

            groups = GroupUser.select().where(GroupUser.user_id == self.uid)
            group_ids.extend([item.group_id for item in groups])
            # 获取用户关联组所有项目
            projects = Project.select().where(Project.group_id.in_(group_ids))
            project_ids = [item.id for item in projects]

            if project_ids:
                cond.append(Project.id.in_(project_ids))

            if not cond:
                cond = [None]

            total = Project.select().where(*cond).count()
            project = Project.select().where(*cond).order_by(sort).paginate(page_index, page_size)
            # 遍历项目各应用的状态来更新项目本身的状态
            ids = [item.id for item in project]
            for id in ids:
                projectapps = Projectapp.select().where(Projectapp.project_id == id)
                projectapps = [model_to_dict(item) for item in projectapps]

                if projectapps:
                    Project.update(project_status=1).where(Project.id == id).execute()
                    for projectapp in projectapps:
                        if projectapp.get("status") == 0:
                            Project.update(project_status=0).where(Project.id == id).execute()
                            break
                else:
                    Project.update(project_status=1).where(id == id).execute()
            project = Project.select().where(*cond).order_by(sort).paginate(page_index, page_size)
            projects = [model_to_dict(item) for item in project]
            project_detail = []
            # 规范前端响应字段
            for project in projects:
                a = dict()

                id = project.get("id")
                project_name = project.get("project_name")
                project_status = project.get("project_status")
                project_date = project.get("project_date")
                group_name = project.get("group_id").get("name")
                comment = project.get("notes")

                a["id"] = id
                a["project_name"] = project_name
                a["project_status"] = project_status
                a["project_date"] = project_date
                a["group_name"] = group_name
                a["comment"] = comment

                project_detail.append(a)
        else:
            # 角色是管理员和安全员可以查看所有的项目
            if role.role_id in [1,3]:
                if not cond:
                    cond = [None]
                total = Project.select().where(*cond).count()
                project = Project.select().where(*cond).order_by(sort).paginate(page_index, page_size)
                # 遍历项目各应用的状态来更新项目本身的状态
                ids = [item.id for item in project]
                for id in ids:
                    projectapps = Projectapp.select().where(Projectapp.project_id == id)
                    projectapps = [model_to_dict(item) for item in projectapps]

                    if projectapps:
                        Project.update(project_status=1).where(Project.id == id).execute()
                        for projectapp in projectapps:
                            if projectapp.get("status") == 0:
                                Project.update(project_status=0).where(Project.id == id).execute()
                                break
                    else:
                        Project.update(project_status=1).where(Project.id == id).execute()
                project = Project.select().where(*cond).order_by(sort).paginate(page_index, page_size)
                projects = [model_to_dict(item) for item in project]
                project_detail = []
                # 规范前端响应字段
                for project in projects:
                    a = dict()

                    id = project.get("id")
                    project_name = project.get("project_name")
                    project_status = project.get("project_status")
                    project_date = project.get("project_date")
                    group_name = project.get("group_id").get("name")
                    comment = project.get("notes")
                    project_paw = project.get("project_paw")

                    a["id"] = id
                    a["project_name"] = project_name
                    a["project_status"] = project_status
                    a["project_date"] = project_date
                    a["group_name"] = group_name
                    a["comment"] = comment
                    a["project_paw"] = project_paw

                    project_detail.append(a)
            else:
                # 其他角色限制了权限
                return self.write(dict(status=False, msg='当前用户无权查看'))

        self.write(dict(page_index=page_index,total=total,result=project_detail))

@url(r"/project/my/status/group", needcheck = False, category = "项目")
class ProjectMyStatusGroup(LoginedRequestHandler):
    """
        项目状态统计
    """

    def get(self):

        role = User.get_or_none(User.id == self.uid)
        role_list = [1, 3]
        cond = []
        if role.role_id in role_list:
            cond.append(Project.project_status.in_([0, 1]))
            values = Project.select(Project.project_status, fn.SUM(1)).where(*cond).group_by(
                Project.project_status).tuples()

            result = []

            for k, v in values:
                result.append(dict(id=k, name=PROJECT_STATUS.get(str(k)), count=int(v)))
        else:
            if role.role_id ==4:
                group_ids = []
                # 获取用户关联组
                groups = Group.select().where(Group.owner_id == self.uid)
                group_ids = [item.id for item in groups]

                groups = GroupUser.select().where(GroupUser.user_id == self.uid)
                group_ids.extend([item.group_id for item in groups])
                # 获取用户关联组所有项目
                projects = Project.select().where(Project.group_id.in_(group_ids))
                project_ids = [item.id for item in projects]

                if project_ids:
                    cond.append(Project.id.in_(project_ids))
                if not cond:
                    cond = [None]
                cond.append(Project.project_status.in_([0, 1]))
                values = Project.select(Project.project_status, fn.SUM(1)).where(*cond).group_by(
                    Project.project_status).tuples()

                result = []

                for k, v in values:
                    result.append(dict(id=k, name=PROJECT_STATUS.get(str(k)), count=int(v)))
            else:
                return self.write(dict(status=False, msg='校验用户失败'))
        self.write(dict(result=result))

@url(r"/project/my/app_status/group", needcheck = False, category = "项目")
class ProjectappMyStatusGroup(LoginedRequestHandler):
    """
        项目应用状态统计
    """

    def get(self):
        project_id = self.get_argument('project_id', '')

        # 管理员， 安全员角色，以及本项目的负责人/管理员能显示状态
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))
        # 先根据app_id,project_id->projectapp->group_id
        group_ids = []
        groups = Group.select().where(Group.owner_id == self.uid)
        group_ids = [item.id for item in groups]
        groups = GroupUser.select().where(GroupUser.user_id == self.uid)
        group_ids.extend([item.group_id for item in groups])

        projectapp = Projectapp.get_or_none(Projectapp.project_id == project_id)
        if projectapp.project_id.group_id.id in group_ids and u.role_id == 4:
            pass
        else:
            if u.role_id in [1, 3]:
                pass
            else:
                return self.write(dict(status=False, msg='用户权限不足', role_id=u.role_id))

        cond = []
        cond.append(Projectapp.project_id==project_id)
        cond.append(Projectapp.status.in_([0, 1]))
        values = Projectapp.select(Projectapp.status, fn.SUM(1)).where(*cond).group_by(
                Projectapp.status).tuples()

        result = []
        for k, v in values:
            result.append(dict(id=k, name=PROJECT_STATUS.get(str(k)), count=int(v)))

        self.write(dict(result=result))

@url(r"/project/nget", needcheck=False, category="项目")
@url(r"/project/get", needcheck=False, category="项目")
class ProjectappGet(LoginedRequestHandler):
    """
        单个项目查询

        id: 漏洞id
    """

    def get(self):
        id = self.get_argument('id')
        search = self.get_argument('search', None)
        status = self.get_argument('status', "")

        page_index = int(self.get_argument('page_index', 1))
        page_size = int(self.get_argument('page_size', 10))

        # 管理员， 安全员角色，以及本项目的负责人/管理员可以查看项目的细节
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))
        # 管理员， 安全员角色，以及本项目的负责人/管理员（渗透人员）可以查看本项目的所有测试应用
        group_ids = []
        groups = Group.select().where(Group.owner_id == self.uid)
        group_ids = [item.id for item in groups]
        groups = GroupUser.select().where(GroupUser.user_id == self.uid)
        group_ids.extend([item.group_id for item in groups])

        projects = Project.get_or_none(Project.id == id)
        if projects.group_id.id in group_ids and u.role_id == 4:
            cond = []
            cond1 = []
            if projects:
                cond.append(Projectapp.project_id == projects.id)
            # if sort:
            #     # add by wuq
            #     sort = getattr(Projectapp, sort)
            #     direction = direction.replace("ending", "")
            #     if direction == 'desc':
            #         sort = sort.desc()
            # else:
            #     sort = Projectapp.project_id.desc()

            if status == "0":
                cond.append(Projectapp.status.in_([0]))
            elif status == "1":
                cond.append(Projectapp.status.in_([1]))
            else:
                cond.append(Projectapp.status.in_([0, 1]))
            if search:
                # mod by wuq
                cond1.append((App.appname.contains(search)))
                apps = App.select().where(*cond1)
                app_ids = [item.id for item in apps]
                cond.append(Projectapp.app_id.in_(app_ids))

            total = Projectapp.select().where(*cond).count()

            projectapp = Projectapp.select().where(*cond)
            projectapps = [model_to_dict(item) for item in projectapp]
            show_detail = []

            for projectapp in projectapps:
                a = dict()
                appname = projectapp.get("app_id").get("appname")
                status = projectapp.get("status")
                project_id = projectapp.get("project_id").get("id")
                app_id = projectapp.get("app_id").get("id")
                id = projectapp.get("id")

                a["appname"] = appname
                a["status"] = status
                a["project_id"] = project_id
                a["app_id"] = app_id
                a["id"] = id
                show_detail.append(a)
        else:
            if u.role_id in [1, 3]:
                cond = []
                cond1 = []
                if projects:
                    cond.append(Projectapp.project_id == projects.id)
                # if sort:
                #     # add by wuq
                #     sort = getattr(Projectapp, sort)
                #     direction = direction.replace("ending", "")
                #     if direction == 'desc':
                #         sort = sort.desc()
                # else:
                #     sort = Projectapp.project_id.desc()

                if status == "0":
                    cond.append(Projectapp.status.in_([0]))
                elif status == "1":
                    cond.append(Projectapp.status.in_([1]))
                else:
                    cond.append(Projectapp.status.in_([0, 1]))
                if search:
                    # mod by wuq
                    cond1.append((App.appname.contains(search)))
                    apps = App.select().where(*cond1)
                    app_ids = [item.id for item in apps]
                    cond.append(Projectapp.app_id.in_(app_ids))

                total = Projectapp.select().where(*cond).count()

                projectapp = Projectapp.select().where(*cond)
                projectapps = [model_to_dict(item) for item in projectapp]
                show_detail = []

                for projectapp in projectapps:
                    a = dict()
                    appname = projectapp.get("app_id").get("appname")
                    status = projectapp.get("status")
                    project_id = projectapp.get("project_id").get("id")
                    app_id = projectapp.get("app_id").get("id")
                    id = projectapp.get("id")
                    content = projectapp.get("content")
                    prod_passed = projectapp.get("prod_passed")
                    test_passed = projectapp.get("test_passed")
                    asset_address = projectapp.get("asset_address")

                    project = Project.get_or_none(Project.id ==project_id)
                    project_paw = project.project_paw
                    prod_passed = decrypt(prod_passed,project_paw, "0102030405060708")
                    test_passed = decrypt(test_passed, project_paw, "0102030405060708")

                    a["appname"] = appname
                    a["status"] = status
                    a["project_id"] = project_id
                    a["app_id"] = app_id
                    a["id"] = id
                    a["content"] = content
                    a["prod_passed"] = prod_passed
                    a["test_passed"] = test_passed
                    a["asset_address"] = asset_address

                    show_detail.append(a)
            else:
                return self.write(dict(status=False,msg = '当前用户无权查看'))


        self.write(dict(page_index=page_index, project_name=projects.project_name, total=total, result=show_detail))


@url(r"/project/app_mark", needcheck=False, category = "项目")
class AppMark(LoginedRequestHandler):
    """
       标记应用完成
    """
    def post(self):
        app_id = self.get_argument('app_id')
        project_id = self.get_argument('project_id')
        # 管理员， 安全员角色，以及本项目的负责人/管理员可以查看项目的细节
        u=User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status = False, msg = '校验用户失败'))

        # 先根据app_id,project_id->projectapp->group_id
        group_ids = []
        groups = Group.select().where(Group.owner_id == self.uid)
        group_ids = [item.id for item in groups]
        groups = GroupUser.select().where(GroupUser.user_id == self.uid)
        group_ids.extend([item.group_id for item in groups])
        # 管理员， 安全员角色，以及本项目的负责人/管理员（渗透人员）才能标记项目完成
        projectapp = Projectapp.get_or_none(Projectapp.app_id == app_id,Projectapp.project_id == project_id)
        if projectapp.project_id.group_id.id in group_ids and u.role_id==4:
            pass
        else:
            if u.role_id in [1,3]:
                pass
            else:
                return  self.write(dict(status = False, msg = '当前用户无权限修改标记'))

        if projectapp.project_id.group_id.id in group_ids and u.role_id==4:
            pass
        else:
            if u.role_id in [1,3]:
                pass
            else:
                return  self.write(dict(status = False, msg = '当前用户无权限修改标记'))
        proapp_status = projectapp.status
        if proapp_status == 1:
            self.write(dict(status=-1, msg='状态已经是完成状态！'))
        else:
            Projectapp.update(status = 1).where(Projectapp.app_id==app_id,Projectapp.project_id==project_id).execute()
            self.write(dict(msg_status = True, msg = '修改成功'))

@url(r"/project/appget", needcheck=False, category="项目")
class ProjecctappdetailGet(LoginedRequestHandler):
    """
        单个应用查询
    """

    def get(self):
        project_id = self.get_argument('project_id')
        app_id = self.get_argument('app_id')

        # 管理员， 安全员角色，以及本项目的负责人/管理员可以查看应用的细节
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))
        # 先根据app_id,project_id->projectapp->group_id
        group_ids = []
        groups = Group.select().where(Group.owner_id == self.uid)
        group_ids = [item.id for item in groups]
        groups = GroupUser.select().where(GroupUser.user_id == self.uid)
        group_ids.extend([item.group_id for item in groups])

        projectapp = Projectapp.get_or_none(Projectapp.app_id == app_id,Projectapp.project_id==project_id)
        if projectapp.project_id.group_id.id in group_ids and u.role_id == 4:
            pass
        else:
            if u.role_id in [1, 3]:
                pass
            else:
                return self.write(dict(status=False, msg='当前用户无权查看', role_id=u.role_id))

        a = dict()
        a['project_name'] = projectapp.project_id.project_name
        a['app_name'] = projectapp.app_id.appname
        a['content'] = projectapp.content

        # a['prod_address'] = projectapp.prod_address
        # a['prod_qrcode'] = projectapp.prod_qrcode
        # a['test_address'] = projectapp.test_address
        # a['test_qrcode'] = projectapp.test_qrcode
        # a['inner_test_address'] = projectapp.inner_test_address
        #
        a['asset_address'] = projectapp.asset_address
        a['asset_address_html'] = projectapp.asset_address_html


        self.write(a)


@url(r"/project/check_propwd", needcheck=False, category="项目")
class check_propwd(LoginedRequestHandler):
    """
          生产口令展示
       """

    def post(self):
        project_id = self.get_argument('project_id')
        app_id = self.get_argument('app_id')
        passwd = self.get_argument('passwd')

        # 管理员， 安全员角色，以及本项目的负责人/管理员可以查看口令
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))
        # 先根据app_id,project_id->projectapp->group_id
        group_ids = []
        groups = Group.select().where(Group.owner_id == self.uid)
        group_ids = [item.id for item in groups]
        groups = GroupUser.select().where(GroupUser.user_id == self.uid)
        group_ids.extend([item.group_id for item in groups])

        projectapp = Projectapp.get_or_none(Projectapp.app_id == app_id, Projectapp.project_id == project_id)
        if projectapp.project_id.group_id.id in group_ids and u.role_id == 4:
            pass
        else:
            if u.role_id in [1, 3]:
                pass
            else:
                return self.write(dict(status=False, msg='当前用户无权查看', role_id=u.role_id))

        pro_passwd = projectapp.project_id.project_paw
        if pro_passwd == password_md5(passwd):
            project = Project.get_or_none(Project.id == project_id)
            project_paw = project.project_paw
            prod_passed = projectapp.prod_passed
            prod_passed = decrypt(prod_passed,project_paw, "0102030405060708")

            self.write(dict(status=True, result=prod_passed))
            # self.write(dict(status=True, result=projectapp.prod_passed))
        else:
            self.write(dict(status=False, result='密码错误'))

@url(r"/project/check_testpwd", needcheck=False, category="项目")
class check_testpwd(LoginedRequestHandler):
    """
           测试口令展示
       """

    def post(self):
        project_id = self.get_argument('project_id')
        app_id = self.get_argument('app_id')
        passwd = self.get_argument('passwd')

        # 管理员， 安全员角色，以及本项目的负责人/管理员可以查看项目的口令
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))
        # 先根据app_id,project_id->projectapp->group_id
        group_ids = []
        groups = Group.select().where(Group.owner_id == self.uid)
        group_ids = [item.id for item in groups]
        groups = GroupUser.select().where(GroupUser.user_id == self.uid)
        group_ids.extend([item.group_id for item in groups])

        projectapp = Projectapp.get_or_none(Projectapp.app_id == app_id, Projectapp.project_id == project_id)
        if projectapp.project_id.group_id.id in group_ids and u.role_id == 4:
            pass
        else:
            if u.role_id in [1, 3]:
                pass
            else:
                return self.write(dict(status=False, msg='当前用户无权查看', role_id=u.role_id))

        pro_passwd = projectapp.project_id.project_paw
        if pro_passwd == password_md5(passwd):
            project = Project.get_or_none(Project.id == project_id)
            project_paw = project.project_paw
            test_passed = projectapp.test_passed
            test_passed = decrypt(test_passed, project_paw, "0102030405060708")

            self.write(dict(status=True, result=test_passed))
            # self.write(dict(status=True, result=projectapp.test_passed))
        else:
            self.write(dict(status=False, result='密码错误'))

@url(r"/project/add", category="项目")
class ProjectAdd(LoginedRequestHandler):
    """
        项目新增/编辑

        _id: 项目id
        project_name: 项目名称*
        group_name: 测试公司
        project_paw: 项目密码
        group_id：组id
        comment:备注

    """
    def post(self):
        id = self.get_argument('id', '')
        project_name = self.get_argument('project_name', '')
        group_name = self.get_argument('group_name', '')
        project_paw = self.get_argument('project_paw','')
        group_id = self.get_argument('group_id','')

        comment = self.get_argument('comment', '')

        try:
            if group_id:
                group_id = Group.get_or_none(Group._id == group_id).id if group_id else 0
        except Exception as e:
            self.write(dict(status=False, msg='公司选择错误'))
            return
        if id:
            project = Project.get_or_none(Project.id == id)
            if project_paw == project.project_paw: #如果前端获取的密码和数据库中经过md5加密的是一样的，说明前端仍然是md5格式，不需要转换，否则需要变更
                project_paw = project_paw
            else:
                project_paw = password_md5(project_paw)
                project_paw_old = project.project_paw
                projectapps = Projectapp.select().where(Projectapp.project_id == id)
                for projectapp in projectapps:
                    projectapp_id = projectapp.id
                    prod_passed_old = projectapp.prod_passed
                    test_passed_old = projectapp.test_passed
                    prod_passed = decrypt(prod_passed_old, project_paw_old, "0102030405060708") #用旧密码解密
                    test_passed = decrypt(test_passed_old, project_paw_old, "0102030405060708")
                    prod_passed_new = encrypt(prod_passed,project_paw, "0102030405060708") #用新密码加密
                    test_passed_new = encrypt(test_passed, project_paw, "0102030405060708")

                    Projectapp.update(prod_passed = prod_passed_new,test_passed = test_passed_new).where(Projectapp.id == projectapp_id).execute()
            if group_name:
                group_id = Group.get_or_none(Group.name == group_name).id
            doc = dict(project_name=project_name, group_id=group_id, project_paw=project_paw, notes=comment)
            Project.update(**doc).where(Project.id == id).execute()
            self.write(dict(status=True, msg='修改成功'))
        else:
            project_paw = password_md5(project_paw)
            doc = dict(project_name=project_name, group_id=group_id,project_paw=project_paw, notes=comment)
            project = Project(**doc)
            project.save()

            self.write(dict(status=True, msg='添加成功'))

@url(r"/project/copy", category="项目")
class ProjectCopy(LoginedRequestHandler):
    """
        项目复制

        id: 应用id
    """

    def post(self):
        id = self.get_arguments('id')

        # 管理员可以增加
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))

        if u.role_id in [1, 3]:
            if id:
                projects = Project.select().where(Project.id.in_(id))
                for project in projects:
                    project_name = project.project_name +'_copy'
                    group_id = project.group_id
                    project_paw = project.project_paw
                    comment=project.notes
                    doc = dict(project_name=project_name, group_id=group_id, project_paw=project_paw, notes=comment)
                    pro = Project(**doc)
                    pro.save()
                    projectapps = Projectapp.select().where(Projectapp.project_id==project.id)
                    for projectapp in projectapps:
                        doc1 = dict(
                            project_id = pro.id,
                            app_id = projectapp.app_id,
                            content = projectapp.content,
                            asset_address = projectapp.asset_address,
                            asset_address_html = projectapp.asset_address_html,
                            prod_passed = projectapp.prod_passed,
                            test_passed = projectapp.test_passed)
                        proapp = Projectapp(**doc1)
                        proapp.save()
                self.write(dict(status=True, msg='复制成功'))
            else:
                self.write(dict(status=False, msg='复制失败'))
        else:
            self.write(dict(status=False, msg='权限不足，无法操作！'))

@url(r"/project/del", category="项目")
class ProjectDel(LoginedRequestHandler):
    """
        项目删除

        id:项目id
    """
    def post(self):
        id = self.get_arguments('id')

        # 管理员可以删除
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))

        if u.role_id in [1,3]:
            Projectapp.delete().where(Projectapp.project_id.in_(id)).execute()
            Project.delete().where(Project.id.in_(id)).execute()

            self.write(dict(status=True, msg='删除成功'))
        else:
            self.write(dict(status=False, msg='权限不足，无法删除！'))

@url(r"/project/app_add", category="项目")
class ProjectappAdd(LoginedRequestHandler):
    """
        项目应用新增/编辑

        project_id: 项目id
        app_name: 应用名称
        group_name: 测试公司
        app_id：应用id
        prod_passed: 生产口令
        test_passed：测试口令

    """

    def post(self):
        id = self.get_argument('id', '')
        project_id = self.get_argument('project_id', '')
        app_name = self.get_argument('app_name', '')
        app_id = App.get_or_none(App.appname == app_name).id if app_name else 0
        prod_passed = self.get_argument("prod_passed", "")
        test_passed = self.get_argument("test_passed", "")

        project = Project.get_or_none(Project.id == project_id)
        project_paw = project.project_paw
        prod_passed = encrypt(prod_passed,project_paw, "0102030405060708")
        test_passed = encrypt(test_passed,project_paw, "0102030405060708")

        doc = dict(
            project_id=project_id,
            app_id=app_id,
            content=self.get_argument("content", ""),
            asset_address=self.get_argument("asset_address", ""),
            asset_address_html=self.get_argument("asset_address_html", ""),
            prod_passed = prod_passed,
            test_passed = test_passed
        )
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))
        if u.role_id in [1,3]: # 管理员 安全员可以进行应用的编辑
            if id:
                Projectapp.update(**doc).where(Projectapp.id == id).execute()
                self.write(dict(status=True, msg='修改成功'))
            else:
                projectapp = Projectapp(**doc)
                projectapp.save()

                self.write(dict(status=True, msg='添加成功'))
        else:
            self.write(dict(status=False, msg='您无权限操作'))

@url(r"/project/app_del", category="项目")
class ProjectappDel(LoginedRequestHandler):
    """
        项目应用删除

        id:应用id

    """
    def post(self):
        id = self.get_arguments('id')

        # 管理员可以删除
        u = User.get_or_none(User.id == self.uid)
        if not u:
            return self.write(dict(status=False, msg='校验用户失败'))

        if u.role_id in [1,3]:
            Projectapp.delete().where(Projectapp.id.in_(id)).execute()
            self.write(dict(status=True, msg='删除成功'))
        else:
            self.write(dict(status=False, msg='权限不足，无法删除！'))
