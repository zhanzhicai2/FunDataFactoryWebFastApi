from app.routers.project import project
from app.routers.user import user

data = [
    (user.router, '/api/user', ["用户模块"]),
    (project.router, '/api/project', ["项目管理模块"])
]
