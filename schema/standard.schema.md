# 基準檔格式

```yaml
id: nstc-research-personnel-hiring          # 檔名同 id
title: 國家科學及技術委員會補助專題研究計畫研究人力約用注意事項
issuer: 國家科學及技術委員會
document_no: 科會綜字第1130073511號          # 最近一次修正之發文字號
version_date: 2024-10-22                     # 最近一次修正日期（西元）
effective_date:                              # 生效日，與修正日不同時填
applies_to: [國科會補助專題研究計畫]          # 適用之計畫類型
source:
  url: https://...
  type: official | repost | news             # 官方原文／轉載／新聞
  retrieved: 2026-11-17                      # 查閱日期
status: 確認 | 推論 | 待查證
supersedes:                                  # 被本版取代之舊檔 id
superseded_by:                               # 取代本版之新檔 id
items:
  - category: 人事費                          # 一級用途別
    item: 專任人員月支酬金（學士級）
    unit: 元/月
    min: 36300                               # 下限（無則省略）
    max:                                     # 上限（無則省略）
    value:                                   # 定額時用
    note:
notes: []
```

金額一律新臺幣元、阿拉伯數字、不加千分位。日期一律 YYYY-MM-DD。
