# 项目启动指南

## 1. 快速启动 (推荐)

使用 Docker Compose 启动所有服务：

```bash
# 进入 docker 目录
cd docker

# 启动所有服务
docker compose up -d

# 查看日志
docker compose logs -f
```

### 访问地址：

- **前端**: [http://localhost:3000](http://localhost:3000)
- **后端 API**: [http://localhost:8080/ping](http://localhost:8080/ping)
- **AI 服务**: [http://localhost:8000](http://localhost:8000)

---

## 2. 本地开发启动

如果你需要进行调试或热更新开发，可以分别启动各服务。

### 前置条件

- 已安装 `pnpm`, `go`, `uv` (Python 管理工具)。
- 本地已有运行中的 PostgreSQL (17) 和 Redis。

### 前端 (Next.js)

```bash
cd frontend
pnpm install
pnpm dev
```

### 后端 (Go)

```bash
cd backend
go run cmd/api/main.go
```

### AI 服务 (Python)

```bash
cd ai-service
uv run uvicorn main:app --reload
```

---

## 3. 环境变量配置

- **统一管理**: 所有的环境变量现在都在 `docker/.env` 中进行统一管理。
- **AI 服务**: 在 `docker/.env` 中设置 `OPENAI_API_KEY`。
- **后端**: 数据库连接配置 `docker/.env`。
