# codexPlayground
play with codex lol

## 部署流程

以下步驟將透過 `docker-compose` 建立並啟動整個開發環境。

1. 確保已安裝 [Docker](https://www.docker.com/) 與 [Docker Compose](https://docs.docker.com/compose/).
2. 在專案根目錄執行下列指令以背景模式啟動容器：
   ```bash
   docker-compose up --build -d
   ```
3. 成功後，服務會依序啟動：
   - 前端：<http://localhost:5173>
   - FastAPI 後端：<http://localhost:8000>
   - 資料庫（MariaDB）：`localhost:3306`
   - Ollama：`localhost:11434`

若需要停止服務，可在相同目錄執行 `Ctrl+C` 或另開終端機執行：
```bash
docker-compose down
```
