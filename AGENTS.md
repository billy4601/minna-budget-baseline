# AGENTS.md

給 Claude 及其他代理之規則。

1. 只收公開來源。不寫入客戶名稱、計畫內容、個人資料。
2. 一律以最新版為準。收錄或引用前，先到主管機關之主管法規系統（例：law.nstc.gov.tw、law.dgbas.gov.tw、edu.law.moe.gov.tw、全國法規資料庫）確認最新修正日期及字號；查不到主管法規系統時，以行政院公報或機關網站為準，並在 `status` 註明未能確認。
3. 路徑與格式依 `schema/baseline.schema.md`：`baselines/<層級>/<發布者代號>/<文件代號>/<生效日>.yaml`。
4. 新版公布時新增檔案，舊檔不刪；新檔填 `supersedes`、舊檔填 `superseded_by`。
5. 數值只寫實際在來源中讀到者；轉引或推算者 `status` 標 `推論`，並於 `note` 說明依據。
6. 優先官方原文；只找到學校或機關轉載時，`source.type` 標 `repost`；新聞只作線索，不作數值來源。
7. 法令、公文以外之著作（含民間報告及受政府委託完成之報告）：確認權利歸屬或開放授權前，只摘錄所需數值並註明出處，不在本 repo 轉載全文或表格。
8. 不在 repo 存放絕對路徑或個人／機器專屬名稱。
9. 修改資料後執行 `python3 tools/build_index.py` 更新 `INDEX.md`，再 commit 並推送 main。
10. 解釋函、解釋彙編、問答集一併收錄，格式依 `schema/baseline.schema.md` 第 3 節；收錄時比對現行版基準，標示 `validity`。
11. 收錄新版時一併轉錄條文全文為 Markdown，並將原始檔案存入 Google Drive、記下 `archive` 與 `sha256`，格式依 `schema/baseline.schema.md` 第 4 節；全文是否放入公開 repo，依該節之著作權判斷。
12. 存放原始檔案時，逐檔確認已存在於 Google Drive 且大小正確，並以實際檔案計算 `sha256` 後才寫入 YAML；以瀏覽器下載者，每份檔案用一個新分頁下載，下載後即確認檔案存在。
13. `BACKLOG.md` 記錄待收集項目；收錄完成即移除該項。
