# 基準檔格式

## 1 路徑

```
baselines/<層級>/<發布者代號>/<文件代號>/<生效日>.yaml
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

## 3 解釋函及解釋彙編

主管機關對某基準之函釋、解釋彙編、問答集，放在該基準資料夾下之 `interpretations/`：

```
baselines/<層級>/<發布者代號>/<文件代號>/interpretations/<日期>_<字號或名稱>.yaml
```

- 函釋：檔名 `YYYY-MM-DD_<發文字號>`（例：`2018-05-02_總處給字第10700397081號`）。
- 解釋彙編、問答集：檔名 `YYYY-MM_解釋彙編`；彙編未載日期者用 `retrieved-<查閱日>_解釋彙編`。
- 解釋發函機關與基準發布者不同時（例：工程會函釋講座鐘點費），仍放在被解釋之基準下。

```yaml
title: 解釋之主旨（自行簡述）
type: 函釋 | 解釋彙編 | 問答集 | 主計長信箱
issuer: 發函機關
document_no: 發文字號
date: YYYY-MM-DD
applies_to_version: 所解釋之基準版本檔名（生效日）
validity: 現行 | 部分適用 | 停止適用 | 待確認
source:
  url: https://...
  type: official | repost | news
  retrieved: YYYY-MM-DD
status: 確認 | 推論 | 待查證
key_points:
  - 以自己的話寫出結論要旨，一則一行
note:
```

基準修正後，原依舊條文所作之解釋可能停止適用（主計總處常於彙編中註明「自某日起停止適用」）；收錄時應比對現行版，`validity` 據實標示。

## 4 條文全文及原始檔案

- 條文全文：轉成 Markdown，放在同版本 YAML 旁，檔名相同（例：`2027-01-01.yaml` 旁之 `2027-01-01.md`）。全文照原文逐字轉錄，不改寫、不摘要；表格轉為 Markdown 表格；文首註明文件名稱、字號、生效日及來源網址。
- 原始檔案（PDF、ODT、DOC 等）不放 repo，存放於 Google Drive，路徑結構與 `baselines/` 相同。YAML 之 `source` 增列：

```yaml
source:
  url: https://...
  type: official
  retrieved: YYYY-MM-DD
  archive: <Google Drive 中之相對路徑>     # 例：central/dgbas/domestic-travel/2025-01-01.pdf
  sha256: <原始檔案之 SHA-256>             # 用以確認存檔未經更動
```

- 是否可將全文放入公開 repo，依著作權判斷：法令、公文（著作權法第 9 條）可放；其他著作（含受政府委託完成之報告）須確認權利歸屬或開放授權後再放，未確認前只存連結與摘錄數值，原始檔案仍可存入 Google Drive 供自用。
