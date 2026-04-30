#!/usr/bin/env python3
"""Generate Issue Tree SVG for Instant Retail EBIT Turnaround"""

import svgwrite

def create_issue_tree_svg():
    dwg = svgwrite.Drawing(size=("1400", "900"))

    # Styles
    title_style = "font-family: Arial; font-size: 16px; font-weight: bold; fill: #E60000;"
    dim_style = "font-family: Arial; font-size: 13px; font-weight: bold; fill: #333;"
    node_style = "font-family: Arial; font-size: 11px; fill: #555;"
    box_title = "fill=#E60000;stroke=#E60000;stroke-width=1;opacity=0.9"
    box_dim1 = "fill=#fff;stroke=#333;stroke-width=2;rx=5"
    box_dim2 = "fill=#fff;stroke=#666;stroke-width=1.5;rx=5"
    box_dim3 = "fill=#fff;stroke=#666;stroke-width=1.5;rx=5"
    line_style = "stroke=#999;stroke-width=1.5;fill:none"

    # Root node - main question
    dwg.add(dwg.rect(insert=(350, 20), size=(700, 45), rx=8, fill=box_title.replace("opacity=0.9", "")))
    dwg.add(dwg.text("如何在 3 年内实现核心城市 EBIT 转正？", insert=(700, 48),
                     text_anchor="middle", style=title_style.replace("fill: #E60000;", "fill: #fff;")))

    # Lines from root to dimensions
    # to Dim 1
    dwg.add(dwg.path(d="M 500 65 L 500 100 L 250 100 L 250 130", style=line_style))
    # to Dim 2
    dwg.add(dwg.path(d="M 700 65 L 700 100 L 700 130", style=line_style))
    # to Dim 3
    dwg.add(dwg.path(d="M 900 65 L 900 100 L 1150 100 L 1150 130", style=line_style))

    # === DIMENSION 1: 城市选择 ===
    dwg.add(dwg.rect(insert=(120, 130), size=(260, 35), rx=5, fill="none", stroke="#E60000", stroke_width=2))
    dwg.add(dwg.text("维度 1：城市选择与资源配置", insert=(250, 152), text_anchor="middle", style=dim_style))

    # Sub-branches for Dim 1
    y_start = 180
    dim1_items = [
        ("止血（优先投资）", "#2E7D32", [
            ("C3 泉州 — 已盈亏平衡",
             "C7 惠州 — 体量大，已接近盈利",
             "C8 威海 — 成本结构最优"),
        ]),
        ("优化（精细化运营）", "#1565C0", [
            ("C1 徐州 — 体量最大但亏损最大",
             "C2 南昌 — 中等体量",
             "C6 南宁 — 体量较大"),
        ]),
        ("评估（选择性收缩）", "#C62828", [
            ("C9 桂林 — 新开城，亏损严重",
             "C10 赣州 — AOV 最低",
             "C4/C5 洛阳/宜昌 — 待观察"),
        ]),
    ]

    y = y_start
    for label, color, items in dim1_items:
        # Category label
        dwg.add(dwg.rect(insert=(130, y), size=(240, 20), rx=3, fill=color, opacity=0.15))
        dwg.add(dwg.text(label, insert=(250, y+15), text_anchor="middle",
                         style=f"font-family: Arial; font-size: 11px; font-weight: bold; fill: {color}"))
        y += 28
        for item in items:
            dwg.add(dwg.text(f"• {item}", insert=(145, y+12), style=node_style))
            y += 18
        y += 10

    # === DIMENSION 2: 用户质量 ===
    dwg.add(dwg.rect(insert=(500, 130), size=(400, 35), rx=5, fill="none", stroke="#1565C0", stroke_width=2))
    dwg.add(dwg.text("维度 2：用户质量提升", insert=(700, 152), text_anchor="middle", style=dim_style))

    # Sub-branches for Dim 2
    y = 180
    dwg.add(dwg.rect(insert=(510, y), size=(380, 20), rx=3, fill="#2E7D32", opacity=0.15))
    dwg.add(dwg.text("提升高价值用户占比（20% → 30%）", insert=(520, y+15), style="font-family: Arial; font-size: 11px; font-weight: bold; fill: #2E7D32;"))
    y += 28
    user_items = [
        '• 补贴精准化：从"补单量"转向"补留存"',
        "• 识别高潜力用户（参考 C8 威海 26% 画像）",
        "• 会员体系：复购激励 + 等级权益",
        "• LTV 提升替代单均补贴",
    ]
    for item in user_items:
        dwg.add(dwg.text(item, insert=(525, y+12), style=node_style))
        y += 18

    y += 18
    dwg.add(dwg.rect(insert=(510, y), size=(380, 20), rx=3, fill="#C62828", opacity=0.15))
    dwg.add(dwg.text("削减低价值用户补贴浪费", insert=(520, y+15), style="font-family: Arial; font-size: 11px; font-weight: bold; fill: #C62828;"))
    y += 28
    dwg.add(dwg.text("• 80% 补贴流向非高价值用户 → 重新分配", insert=(525, y+12), style=node_style))

    # === DIMENSION 3: 品类结构 ===
    dwg.add(dwg.rect(insert=(930, 130), size=(420, 35), rx=5, fill="none", stroke="#6A1B9A", stroke_width=2))
    dwg.add(dwg.text("维度 3：品类结构优化", insert=(1140, 152), text_anchor="middle", style=dim_style))

    y = 180
    dwg.add(dwg.rect(insert=(940, y), size=(400, 20), rx=3, fill="#2E7D32", opacity=0.15))
    dwg.add(dwg.text("提升高毛利品类占比", insert=(950, y+15), style="font-family: Arial; font-size: 11px; font-weight: bold; fill: #2E7D32;"))
    y += 28
    category_items = [
        "• 大超合作深化（泉州 23% vs 赣州 12%）",
        "• 降低拣货成本 + 稳定供应链",
        "• 到家快消（毛利率 40-55%）占比提升",
    ]
    for item in category_items:
        dwg.add(dwg.text(item, insert=(955, y+12), style=node_style))
        y += 18

    y += 18
    dwg.add(dwg.rect(insert=(940, y), size=(400, 20), rx=3, fill="#C62828", opacity=0.15))
    dwg.add(dwg.text("控制低毛利品类", insert=(950, y+15), style="font-family: Arial; font-size: 11px; font-weight: bold; fill: #C62828;"))
    y += 28
    control_items = [
        "• 生鲜（毛利率 15-25%）— 控制损耗",
        "• 餐饮（毛利率 30-40%）— 避免补贴战",
    ]
    for item in control_items:
        dwg.add(dwg.text(item, insert=(955, y+12), style=node_style))
        y += 18

    # === HYPOTHESES BOX ===
    y += 30
    dwg.add(dwg.rect(insert=(120, y), size=(1260, 85), rx=8, fill="#f5f5f5", stroke="#E60000", stroke_width=1.5))
    dwg.add(dwg.text("核心假设 (Hypotheses)", insert=(750, y+22), text_anchor="middle",
                     style="font-family: Arial; font-size: 12px; font-weight: bold; fill: #E60000;"))

    hypotheses = [
        "H1 城市：泉州/惠州/威海集中资源，12-18 个月验证盈利模型",
        "H2 用户：补贴精准化 → 高价值用户 20%→30%，同时降低总补贴",
        "H3 品类：大超合作 +10pp → 履约成本降低 0.5-1 元/单",
    ]
    for i, h in enumerate(hypotheses):
        dwg.add(dwg.text(h, insert=(140, y+45+i*18), style=node_style))

    # Footer
    dwg.add(dwg.text("来源：Bainsight 分析 | Step 2: Issue Tree | 2026-04-30",
                     insert=(700, 870), text_anchor="middle",
                     style="font-family: Arial; font-size: 10px; fill: #999;"))

    # Save
    output_path = "/Users/minimx/Library/Mobile Documents/com~apple~CloudDocs/Bainsight/Drafts/02-issue-tree.svg"
    dwg.saveas(output_path)
    print(f"Saved to {output_path}")
    return output_path

if __name__ == "__main__":
    create_issue_tree_svg()
