# AGENTS.md

給 Claude 及其他代理之規則。

1. 只收公開來源。不寫入客戶名稱、計畫內容、個人資料。
2. 一律以最新版為準。收錄或引用前，先到主管機關之主管法規系統（例：law.nstc.gov.tw、law.dgbas.gov.tw、edu.law.moe.gov.tw、全國法規資料庫）確認最新修正日期及字號；查不到主管法規系統時，以行政院公報或機關網站為準，並在 `status` 註明未能確認。
3. 路徑與格式依 `schema/standard.schema.md`：`standards/<層級>/<發布者代號>/<文件代號>/<生效日>.yaml`。
4. 新版公布時新增檔案，舊檔不刪；新檔填 `supersedes`、舊檔填 `superseded_by`。
5. 數值只寫實際在來源中讀到者；轉引或推算者 `status` 標 `推論`，並於 `note` 說明依據。
6. 優先官方原文；只找到學校或機關轉載時，`source.type` 標 `repost`；新聞只作線索，不作數值來源。
7. 民間薪資報告受著作權保護：只摘錄所需數值並註明出處，不轉載全文或表格。
8. 不在 repo 存放絕對路徑或個人／機器專屬名稱。
9. 修改資料後執行 `python3 tools/build_index.py` 更新 `INDEX.md`，再 commit 並推送 main。
10. `BACKLOG.md` 記錄待收集項目；收錄完成即移除該項。
