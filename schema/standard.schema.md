# 基準檔格式

## 1 路徑

```
standards/<層級>/<發布者代號>/<文件代號>/<生效日>.yaml
```

- 層級：`central` 中央機關、`local` 地方政府、`private` 民間（工協會、人力銀行等）。
- 發布者代號：該機關或團體之英文簡稱，小寫（例：`dgbas`、`nstc`、`kaohsiung`、`cisa`）。
- 文件代號：文件名稱之英文短名，kebab-case，不含發布者代號（例：`lecture-fee`）。
- 檔名：該版之生效日 `YYYY-MM-DD`。未載生效日者用修正日；只知年度者用 `YYYY`；只知年月者用 `YYYY-MM`。
- 一份文件一個資料夾，一個版本一個檔案；新版公布時新增檔案，舊檔不刪。

## 2 欄位

```yaml
title: 文件名稱（全名）
issuer: 發布機關
kind: 經費基準 | 計畫規定 | 法定下限 | 市場行情
document_no: 發文字號
version_date: YYYY-MM-DD        # 修正（發布）日
effective_date: YYYY-MM-DD      # 生效日；未載明則空白
applies_to: [適用之計畫類型]
source:
  url: https://...
  type: official | repost | news  # 官方原文／轉載／新聞
  retrieved: YYYY-MM-DD           # 查閱日
status: 確認 | 推論 | 待查證
supersedes: 被本版取代之舊版檔名
superseded_by: 取代本版之新版檔名
items:
  - category: 人事費              # 依文件本身之用途別名稱
    item: 項目名稱
    unit: 元/月
    min:                          # 下限
    max:                          # 上限
    value:                        # 定額
    note:
notes: []
```

金額一律新臺幣元、阿拉伯數字、不加千分位；比率以小數表示（10% 寫 0.10）。
