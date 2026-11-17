#!/usr/bin/env python3
"""產生 INDEX.md：各基準之現行版、已公布未生效版，以及依用途別之項目總表。

用法：python3 tools/build_index.py [基準日 YYYY-MM-DD]（預設今天）
"""
import datetime
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / "baselines"


def fmt_amount(it):
    unit = it.get("unit") or ""
    if it.get("value") is not None:
        s = f"{it['value']}"
    elif it.get("min") is not None and it.get("max") is not None:
        s = f"{it['min']}–{it['max']}"
    elif it.get("min") is not None:
        s = f"≥ {it['min']}"
    elif it.get("max") is not None:
        s = f"≤ {it['max']}"
    else:
        s = "—"
    return f"{s} {unit}".strip()


def main():
    today = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    docs = {}
    for f in sorted(BASE.rglob("*.yaml")):
        doc_dir = f.parent.relative_to(BASE).as_posix()
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        data["_version"] = f.stem
        docs.setdefault(doc_dir, []).append(data)

    current, upcoming = [], []
    for doc_dir, versions in docs.items():
        versions.sort(key=lambda d: d["_version"])
        past = [v for v in versions if v["_version"] <= today]
        future = [v for v in versions if v["_version"] > today]
        if past:
            current.append((doc_dir, past[-1]))
        for v in future:
            upcoming.append((doc_dir, v))

    out = [
        "# INDEX",
        "",
        f"本檔由 `tools/build_index.py` 產生，基準日 {today}。請勿手改。",
        "",
        "## 1 現行版",
        "",
        "| 路徑 | 文件 | 字號 | 版本 | 狀態 |",
        "|---|---|---|---|---|",
    ]
    for doc_dir, d in current:
        out.append(f"| `{doc_dir}` | {d['title']} | {d.get('document_no') or '—'} | {d['_version']} | {d['status']} |")

    out += ["", "## 2 已公布、未生效", "", "| 路徑 | 文件 | 字號 | 生效 |", "|---|---|---|---|"]
    for doc_dir, d in upcoming:
        out.append(f"| `{doc_dir}` | {d['title']} | {d.get('document_no') or '—'} | {d['_version']} |")
    if not upcoming:
        out.append("| — | — | — | — |")

    out += ["", "## 3 依用途別（現行版及未生效版）", ""]
    by_cat = {}
    for doc_dir, d in current + upcoming:
        for it in d.get("items") or []:
            by_cat.setdefault(it["category"], []).append((doc_dir, d, it))
    for cat in sorted(by_cat):
        out += [f"### {cat}", "", "| 項目 | 金額 | 文件 | 版本 |", "|---|---|---|---|"]
        for doc_dir, d, it in by_cat[cat]:
            out.append(f"| {it['item']} | {fmt_amount(it)} | `{doc_dir}` | {d['_version']} |")
        out.append("")

    (ROOT / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"[OK] INDEX.md：{len(current)} 份現行、{len(upcoming)} 份未生效")


if __name__ == "__main__":
    main()
