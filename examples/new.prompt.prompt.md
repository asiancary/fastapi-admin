---
description: New prompt created from chat session
mode: ask
model: GPT-4.1 (copilot)
---
<user>
分析项目架构
</user>
<assistant>
该项目采用分层结构，主要分为如下几个部分：

- **核心包 `fastapi_admin`**：  
  实现了 FastAPI Admin 的主要功能，包括：
  - app.py：主应用对象和配置入口。
  - resources.py：资源（模型、链接、下拉菜单等）和字段定义。
  - `widgets/`：表单控件、显示控件、过滤器等组件。
  - `routes/`：API 路由，主要是资源的增删改查。
  - depends.py：依赖注入相关方法。
  - template.py：Jinja2 模板环境和全局变量。
  - i18n.py：多语言支持。
  - constants.py、enums.py 等：常量和枚举类型。
  - `locales/`：多语言翻译文件。
  - `templates/`：Tabler UI 风格的 Jinja2 模板。

- **示例包 `examples`**：  
  提供了实际业务模型、资源、枚举、配置和自定义页面，演示如何集成和扩展 FastAPI Admin。

- **静态资源 [`static/`] 和模板 [`templates/`]**：  
  存放静态文件（如上传图片）和自定义模板。

- **配置与元数据文件**：  
  包括 pyproject.toml、Makefile、docker-compose.yml、Dockerfile 等，便于开发、测试和部署。

- **测试 [`tests/`]**：  
  用于自动化测试。

- **CI/CD 配置**：  
  .github 目录下包含 GitHub Actions 工作流。

**架构特点：**
- 采用 FastAPI + Tortoise-ORM 实现后端，Jinja2 渲染前端页面。
- 资源（Resource）为核心抽象，支持模型、链接、下拉菜单等多种类型。
- 支持多语言、权限、可插拔 Provider、可扩展表单控件和显示控件。
- 前后端一体化，适合快速开发后台管理系统。

你可以根据自己的业务需求，在 examples 目录下扩展模型和资源，或自定义模板和控件。
</assistant>
<user>
能帮我画出项目架构图吗
</user>
<assistant>
当然可以！以下是该 FastAPI Admin 项目的简化架构图（文本版，适合 Markdown 展示）：

```
FastAPI Admin 项目架构
┌────────────────────────────┐
│        入口 (main.py)      │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│      fastapi_admin/        │
│ ┌────────────────────────┐ │
│ │ app.py (应用初始化)     │ │
│ │ depends.py (依赖注入)   │ │
│ │ template.py (模板环境)  │ │
│ │ i18n.py (多语言)        │ │
│ └────────────────────────┘ │
│        │         │         │
│        ▼         ▼         ▼
│   routes/   widgets/   locales/│
│ (路由)   (控件)   (翻译)      │
└─────────────┬────────────────┘
              │
              ▼
┌────────────────────────────┐
│        examples/           │
│ ┌────────────────────────┐ │
│ │ models.py (业务模型)    │ │
│ │ resources.py (资源)     │ │
│ │ enums.py/constants.py   │ │
│ └────────────────────────┘ │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│   templates/ & static/     │
│ (Jinja2模板 & 静态资源)    │
└────────────────────────────┘
```

**说明：**
- fastapi_admin 为核心功能模块，负责应用初始化、依赖、模板、多语言等。
- examples 为业务扩展示例，包含模型、资源、枚举等。
- `templates/` 和 `static/` 存放前端模板和静态文件。
- 入口文件（如 `main.py` 或 `app.py`）负责启动应用。

如需更详细的图（如 Mermaid、draw.io 等格式），请告知你需要的格式！
</assistant>
<user>
画出调用关系图
</user>
<assistant>
下面是该项目的主要调用关系图（文本版，适合 Markdown 展示）：

```
调用关系图
┌──────────────┐
│   main.py    │
└──────┬───────┘
       │
       ▼
┌─────────────────────────────┐
│   fastapi_admin.app         │
│ (初始化FastAPI Admin应用)   │
└──────┬─────────────┬────────┘
       │             │
       ▼             ▼
fastapi_admin.depends   fastapi_admin.template
(依赖注入)              (模板环境)
       │             │
       ▼             ▼
fastapi_admin.routes   fastapi_admin.i18n
(API路由)              (多语言)
       │
       ▼
widgets/
(表单控件、显示控件)
       │
       ▼
examples.resources
(资源注册与管理)
       │
       ▼
examples.models
(业务模型)
```

**说明：**
- `main.py` 启动应用，调用 `fastapi_admin.app` 初始化后台管理。
- `app` 依赖 `depends`（依赖注入）、`template`（模板）、`i18n`（多语言）。
- `routes` 负责 API 路由，调用 `widgets`（控件）和 `examples.resources`（资源）。
- `resources` 进一步调用 `models`（业务数据模型）。

如需 Mermaid 或其他格式，请告知！
</assistant>
<user>
帮我增加一个藏族语的README-tb.md
</user>
<assistant>
````markdown
// filepath: vscode-vfs://github/fastapi-admin/fastapi-admin/README-tb.md
# FastAPI ADMIN

[![image](https://img.shields.io/pypi/v/fastapi-admin.svg?style=flat)](https://pypi.python.org/pypi/fastapi-admin)
[![image](https://img.shields.io/github/license/fastapi-admin/fastapi-admin)](https://github.com/fastapi-admin/fastapi-admin)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/gh-pages/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:gh-pages)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/pypi/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:pypi)

[中文文档](./README-zh.md)
[한국어 문서](./README-ko.md)
[日本語ドキュメント](./README-ja.md)
[བོད་ཡིག་ཡིག་ཆ་](./README-tb.md)

## ངོ་སྤྲོད།

`fastapi-admin` ནི་ [FastAPI](https://github.com/tiangolo/fastapi) དང་ [TortoiseORM](https://github.com/tortoise/tortoise-orm/) དང་ [tabler](https://github.com/tabler/tabler) UI སྒྲི// filepath: vscode-vfs://github/fastapi-admin/fastapi-admin/README-tb.md
# FastAPI ADMIN

[![image](https://img.shields.io/pypi/v/fastapi-admin.svg?style=flat)](https://pypi.python.org/pypi/fastapi-admin)
[![image](https://img.shields.io/github/license/fastapi-admin/fastapi-admin)](https://github.com/fastapi-admin/fastapi-admin)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/gh-pages/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:gh-pages)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/pypi/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:pypi)

[中文文档](./README-zh.md)
[한국어 문서](./README-ko.md)
[日本語ドキュメント](./README-ja.md)
[བོད་ཡིག་ཡིག་ཆ་](./README-tb.md)

## ངོ་སྤྲོད།

`fastapi-admin` ནི་ [FastAPI](https://github.com/tiangolo/fastapi) དང་ [TortoiseORM](https://github.com/tortoise/tortoise-orm/) དང་ [tabler](https://github.com/tabler/tabler) UI སྒྲི
</assistant>
<user>
帮我增加一个西班牙语的readme
</user>
<assistant>
````markdown
// filepath: README-tb.md
# FastAPI ADMIN

[![image](https://img.shields.io/pypi/v/fastapi-admin.svg?style=flat)](https://pypi.python.org/pypi/fastapi-admin)
[![image](https://img.shields.io/github/license/fastapi-admin/fastapi-admin)](https://github.com/fastapi-admin/fastapi-admin)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/gh-pages/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:gh-pages)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/pypi/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:pypi)

[བོད་ཡིག](./README-tb.md)
[中文](./README-zh.md)
[한국어](./README-ko.md)
[日本語](./README-ja.md)

## ངོ་སྤྲོད།

`fastapi-admin` ནི་ [FastAPI](https://github.com/tiangolo/fastapi) དང་ [TortoiseORM](https://github.com/tortoise/tortoise-orm/) དང་ [tabler](https://github.com/tabler/tabler) UI ལ་གཞི་བཞག་པའི་སྒྲིག་འཛུགས་སྒོ་ཡིན། Django admin ནས་བརྗེ་བ་ཡིན།

## དཔེ་མ// filepath: README-tb.md
# FastAPI ADMIN

[![image](https://img.shields.io/pypi/v/fastapi-admin.svg?style=flat)](https://pypi.python.org/pypi/fastapi-admin)
[![image](https://img.shields.io/github/license/fastapi-admin/fastapi-admin)](https://github.com/fastapi-admin/fastapi-admin)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/gh-pages/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:gh-pages)
[![image](https://github.com/fastapi-admin/fastapi-admin/workflows/pypi/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:pypi)

[བོད་ཡིག](./README-tb.md)
[中文](./README-zh.md)
[한국어](./README-ko.md)
[日本語](./README-ja.md)

## ངོ་སྤྲོད།

`fastapi-admin` ནི་ [FastAPI](https://github.com/tiangolo/fastapi) དང་ [TortoiseORM](https://github.com/tortoise/tortoise-orm/) དང་ [tabler](https://github.com/tabler/tabler) UI ལ་གཞི་བཞག་པའི་སྒྲིག་འཛུགས་སྒོ་ཡིན། Django admin ནས་བརྗེ་བ་ཡིན།

## དཔེ་མ
</assistant>
<user>
@vscode /search  admin_app
</user>
<assistant>
To search for occurrences of "admin_app" in your C++ project (which may include source files and your Makefile), use the following parameters. This will search across all files for the term "admin_app".


</assistant>
<user>
@vscode /startDebugging 
</user>
<assistant>
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "debugpy",
      "request": "launch",
      "name": "Launch FastAPI Admin Example",
      "program": "${workspaceFolder}/examples/main.py",
      "args": [],
      "envFile": "${workspaceFolder}/.env"
    }
  ]
}
```
This configuration will launch your FastAPI Admin example app using the main.py file in the examples directory, and load environment variables from your .env file.
Debugging can be started in the [Debug View](command:workbench.view.debug) or by using the [Start Debugging Command](command:workbench.action.debug.run).
</assistant>
<user>
go ahad
</user>
<assistant>
````markdown
// filepath: README-es.md

# FastAPI ADMIN

[![Versión en PyPI](https://img.shields.io/pypi/v/fastapi-admin.svg?style=flat)](https://pypi.python.org/pypi/fastapi-admin)
[![Licencia](https://img.shields.io/github/license/fastapi-admin/fastapi-admin)](https://github.com/fastapi-admin/fastapi-admin)
[![Estado de gh-pages](https://github.com/fastapi-admin/fastapi-admin/workflows/gh-pages/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:gh-pages)
[![Publicación en PyPI](https://github.com/fastapi-admin/fastapi-admin/workflows/pypi/badge.svg)](https://github.com/fastapi-admin/fastapi-admin/actions?query=workflow:pypi)

[Documentación en chino](./README-zh.md)
[Documentación en coreano](./README-ko.md)
[Documentación en japonés](./README-ja.md)

## Descripción

`fastapi-admin` es un sistema de administración construido sobre [FastAPI](https://github.com/tiangolo/fastapi), [TortoiseORM](https://github.com/tortoise/tortoise-orm/) y la interfaz de usuario de [Tabler](https://github.com/tabler/tabler). Su diseño está inspirado en el panel de administración de Django.

## Demo en línea

Puedes probar una demostración en [este enlace](https://fastapi-admin.long2ice.io/admin/login):

- Usuario: `admin`
- Contraseña: `123456`

También puedes ver la versión Pro en [este enlace](https://fastapi-admin-pro.long2ice.io/admin/login):

- Usuario: `admin`
- Contraseña: `123456`

## Capturas de pantalla

![Pantalla de inicio de sesión](https://raw.githubusercontent.com/fastapi-admin/fastapi-admin/dev/images/login.png)

![Panel principal](https://raw.githubusercontent.com/fastapi-admin/fastapi-admin/dev/images/dashboard.png)

## Ejecución local

1. Clona este repositorio.
2. Crea un archivo `.env` con el siguiente contenido:

   ```dotenv
   DATABASE_URL=mysql://root:123456@127.0.0.1:3306/fastapi-admin
   REDIS_URL=redis://localhost:6379/0
   ```

3. Ejecuta `docker-compose up -d --build`.
4. Accede a <http://localhost:8000/admin/init> para crear el primer usuario administrador.

## Documentación

La documentación completa está disponible en <https://fastapi-admin.github.io>.

## Licencia

Este proyecto se distribuye bajo la licencia [Apache-2.0](https://github.com/fastapi-admin/fastapi-admin/blob/master/LICENSE).

## Agradecimientos

[![yxvm](./images/yxvm.png)](https://yxvm.com/)

Agradecimientos a [NodeSupport](https://github.com/NodeSeekDev/NodeSupport) por su patrocinio.
````
</assistant>
<user>
@workspace /fix 
</user>
<assistant>
````python
# filepath: vscode-vfs://github/fastapi-admin/fastapi-admin/examples/main.py
# ...existing code...

def create_app():
    app = FastAPI(lifespan=lifespan)
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(BASE_DIR, "static")),
        name="static",
    )

    @app.get("/")
    async def index():
        return RedirectResponse(url="/admin")

    # 修正：去掉多余的空格，正确调用 admin_app
    admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
    admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
    admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
    admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)

    app.mount("/admin", admin_app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    register_tortoise(
        app,
        config={
            "connections": {"default": settings.DATABASE_URL},
            "apps": {
                "models": {
                    "models": ["examples.models"],
                    "default_connection": "default",
                }
            },
        },
        generate_schemas=True,
    )
    return app

## filepath: vscode-vfs://github/fastapi-admin/fastapi-admin/examples/main.py
# ...existing code...

def create_app():
    app = FastAPI(lifespan=lifespan)
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(BASE_DIR, "static")),
        name="static",
    )

    @app.get("/")
    async def index():
        return RedirectResponse(url="/admin")

    # 修正：去掉多余的空格，正确调用 admin_app
    admin_app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
    admin_app.add_exception_handler(HTTP_404_NOT_FOUND, not_found_error_exception)
    admin_app.add_exception_handler(HTTP_403_FORBIDDEN, forbidden_error_exception)
    admin_app.add_exception_handler(HTTP_401_UNAUTHORIZED, unauthorized_error_exception)

    app.mount("/admin", admin_app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    register_tortoise(
        app,
        config={
            "connections": {"default": settings.DATABASE_URL},
            "apps": {
                "models": {
                    "models": ["examples.models"],
                    "default_connection": "default",
                }
            },
        },
        generate_schemas=True,
    )
    return app

#
</assistant>