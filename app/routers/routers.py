from app.routers import user, project

data = [
    (user.router, '/api/user', ["用户模块"]),
    (project.router, '/api/project', ["项目管理模块"])
]
