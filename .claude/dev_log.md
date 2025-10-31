# 開發日誌

## 2025-10-30

### 完成項目

#### 專案初始化
- 使用 uv 建立 Python 專案（Python 3.12）
- 安裝依賴：FastAPI、Uvicorn、Pydantic、Faker
- 建立基本專案結構：
  - `app/main.py` - FastAPI 應用主程式
  - `app/schemas.py` - Pydantic 資料模型
  - `app/data_generator.py` - Faker 資料生成器
  - `app/__init__.py` - Python 套件標記檔案

#### FastAPI 應用開發
- 建立 FastAPI 應用實例
- 定義 User schema（id, name）
- 實作 `generate_users()` 函數使用 Faker 生成假資料
- 設定 startup 事件自動生成 10 筆使用者資料
- 建立 `/` 端點回傳使用者列表

#### 本地開發環境
- 建立 Makefile 定義 `runserver` 命令
- 啟動命令：`uv run uvicorn app.main:app --reload`
- 本地測試成功

#### 部署至 Zeabur
- 建立 GitHub repository（私有）
- 連接 Zeabur 部署平台
- 解決部署問題：
  - 修正啟動命令（從錯誤的 `python app/__init__.py` 改為 `uvicorn app.main:app`）
  - 加入 `app/__init__.py` 使其成為正式 Python 套件
- 綁定 Zeabur 免費子網域
- 部署成功，取得公開 API 網址

### 學習重點

- **Uvicorn**：ASGI Web 伺服器，用於執行 FastAPI 應用
- **Faker**：使用內建資料集 + 隨機組合生成假資料，非資料庫
- **Pydantic**：提供資料驗證和型別檢查
- **部署平台**：Zeabur 自動偵測 Python 專案並處理建置
- **相對導入 vs 絕對導入**：使用 `from app.schemas import User` 需要 `__init__.py`

### 遇到的問題與解決

1. **模組導入問題**：`ModuleNotFoundError: No module named 'schemas'`
   - 解決：改用絕對導入 `from app.schemas import User`

2. **Pydantic 類別屬性存取錯誤**：直接存取 `User.id` 導致 AttributeError
   - 解決：需先建立實例 `user = User(id=1, name="John")`

3. **Zeabur 部署啟動失敗**：容器持續重啟
   - 解決：修正啟動命令為 `uvicorn app.main:app --host 0.0.0.0 --port ${PORT}`
   - 加入 `app/__init__.py` 使 app 成為正式套件

4. **Makefile 語法錯誤**：`Nothing to be done for 'runserver'`
   - 解決：命令前必須使用 Tab 縮排，不能用空格

### 技術決策

- **保留 Pydantic schema**：雖然可以直接用 dict，但 schema 提供型別檢查、自動 API 文件、擴充性
- **部署平台選擇**：選用 Zeabur（中文介面、簡單易用、有免費額度）
- **不使用 Docker + nginx + VPS**：專案規模小，託管服務更適合

---

## 明天開發方向

### 主要任務
使用 Faker 建立大量測試資料，供前端效能測試使用

### 待辦項目
- [ ] 設定 CORS（讓 GitHub Pages 前端能呼叫 API）
- [ ] 擴充 User schema 增加更多欄位（email、phone、address 等）
- [ ] 調整資料生成數量（可能需要數百至數千筆）
- [ ] 新增分頁功能（避免一次回傳過多資料）
- [ ] 測試 API 效能（大量資料下的回應時間）
- [ ] 前端整合測試

### 技術考量
- 大量資料是否需要持久化？（目前存在記憶體，重啟會消失）
- 是否需要提供篩選、排序功能？
- API 回應格式是否需要調整？
