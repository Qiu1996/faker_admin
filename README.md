# Faker Admin

前後端分離的假資料 API 服務，供前端開發測試使用。

## 專案簡介
提供假資料 API 端點，使用 Faker 生成隨機資料，用於前端測試和開發使用。

## 技術棧

### 後端
- **Python 3.12**
- **FastAPI** - Web 框架
- **Uvicorn** - ASGI 伺服器
- **Pydantic** - 資料驗證
- **Faker** - 假資料生成
- **uv** - 套件管理

### 前端
- **Vue 3** - 前端框架
- **Vite** - 建置工具

## 專案結構

```
faker_admin/
├── backend/          # FastAPI 後端
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── data_generator.py
│   ├── pyproject.toml
│   └── Makefile
└── frontend/         # Vue 3 前端
    ├── src/
    ├── package.json
    └── vite.config.js
```

## 本地開發

### 後端

```bash
cd backend
uv sync                # 安裝依賴
make reload           # 啟動開發伺服器（自動重載）
```

伺服器會在 `http://localhost:8000` 啟動。

### 前端

```bash
cd frontend
npm install           # 安裝依賴
npm run dev          # 啟動開發伺服器
```

前端會在 `http://localhost:5173` 啟動。

## 部署環境

- **後端**：[Zeabur](https://zeabur.com)
  - 生產網址：https://fakeradmin.zeabur.app/

- **前端**：GitHub Pages
  - 透過 GitHub Actions 自動部署
  - 生產網址：https://qiu1996.github.io/faker_admin/

## API 端點

### GET /

回傳假使用者資料列表。

**回應範例：**
```json
[
  {
    "id": 1,
    "name": "John Doe"
  }
]
```
