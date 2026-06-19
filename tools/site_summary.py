import json
from typing import Dict, List, Any

# 站点资料配置
SITES_CONFIG = {
    "zhcn_zjh": {
        "url": "https://zhcn-zjh.com",
        "keywords": ["炸金花", "扑克游戏", "休闲娱乐"],
        "tags": ["棋牌", "休闲", "竞技"],
        "description": "炸金花主题娱乐站点，提供经典扑克玩法与社区互动。"
    }
}

def generate_summary_entry(site_data: Dict[str, Any]) -> str:
    url = site_data.get("url", "")
    keywords = site_data.get("keywords", [])
    tags = site_data.get("tags", [])
    desc = site_data.get("description", "")

    kw_str = ", ".join(keywords)
    tag_str = ", ".join(tags)

    summary = (
        f"站点摘要\n"
        f"URL: {url}\n"
        f"关键词: {kw_str}\n"
        f"标签: {tag_str}\n"
        f"说明: {desc}\n"
    )
    return summary

def format_markdown_summary(entries: List[str]) -> str:
    lines = ["# 站点资料摘要\n"]
    for i, entry in enumerate(entries, 1):
        lines.append(f"## 站点 {i}\n")
        lines.append(entry)
        lines.append("\n---\n")
    return "".join(lines)

def format_json_summary(site_data_map: Dict[str, Any]) -> str:
    output = []
    for key, data in site_data_map.items():
        entry = {
            "id": key,
            "url": data.get("url"),
            "keywords": data.get("keywords"),
            "tags": data.get("tags"),
            "description": data.get("description")
        }
        output.append(entry)
    return json.dumps(output, ensure_ascii=False, indent=2)

def main():
    # 生成文本摘要列表
    text_entries = []
    for key, data in SITES_CONFIG.items():
        summary = generate_summary_entry(data)
        text_entries.append(summary)

    # 输出 Markdown 格式摘要
    md_output = format_markdown_summary(text_entries)
    print("=== Markdown 摘要 ===")
    print(md_output)

    # 输出 JSON 格式摘要
    json_output = format_json_summary(SITES_CONFIG)
    print("=== JSON 摘要 ===")
    print(json_output)

    # 简单统计
    site_count = len(SITES_CONFIG)
    all_keywords = set()
    for data in SITES_CONFIG.values():
        all_keywords.update(data.get("keywords", []))
    all_tags = set()
    for data in SITES_CONFIG.values():
        all_tags.update(data.get("tags", []))

    print("\n=== 统计信息 ===")
    print(f"站点数量: {site_count}")
    print(f"关键词总数: {len(all_keywords)}")
    print(f"标签总数: {len(all_tags)}")

if __name__ == "__main__":
    main()