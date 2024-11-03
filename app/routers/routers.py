from app.routers import user, project, cases


data = [
    (user.router, '/api/user', ["用户模块"]),
    (project.router, '/api/project', ["项目管理模块"]),
    (cases.router, '/api/cases', ["用例模块"])
]
