# 測試與 CI/CD 流程

本資料夾包含專案的 Python 測試，採用 [pytest](https://pytest.org/) 撰寫。

## 本地執行測試

1. 安裝相依套件：
   ```bash
   pip install -r backend/requirements-dev.txt
   ```
2. 在專案根目錄執行：
   ```bash
   python -m pytest -q
   ```

## CI/CD

專案使用 GitHub Actions 進行 CI。當程式碼推送至 `main` 分支或提出 Pull Request 時，會觸發 `.github/workflows/ci.yml`：

1. **後端流程**
   - 設定 Python 3.11 環境。
   - 安裝 `backend/requirements-dev.txt` 中的套件。
   - 執行 `python -m pytest -q`。
2. **前端流程**
   - 設定 Node 20 環境並快取 npm 依賴。
   - 在 `src` 目錄執行 `npm ci` 安裝依賴並進行建置：
     ```bash
     npm run build
     ```

流程全部成功後即可合併。
