---
id: 01-problem-definition
type: problem-definition
step: 1
title: "Problem Definition"
status: draft
addresses: null
entities:
  key_question:
    anchor: "01-problem-definition.md#kq"
    text: "如何让 Instant Retail Co. 在三四线城市实现 3-5 年可持续增长并扭亏为盈？"
  hypotheses:
    - anchor: "01-problem-definition.md#hyp-unit-econ-mismatch"
      label: "单位经济结构性不匹配：城市质量+用户质量+品类结构三维失衡"
    - anchor: "01-problem-definition.md#hyp-city-quality"
      label: "城市质量比城市数量更重要——C8威海和C10赣州履约成本差17%，但AOV差44%"
    - anchor: "01-problem-definition.md#hyp-category-structure"
      label: "品类结构影响毛利率——生鲜15-25%、餐饮30-40%、到家快消40-55%"
  success_criteria:
    - anchor: "01-problem-definition.md#sc-y1"
      label: "第1年末：3城（泉州/惠州/威海）EBIT≥0，年亏损<5,000万"
      measure: "EBIT率≥0%；年亏损额<5,000万"
    - anchor: "01-problem-definition.md#sc-y2"
      label: "第2年末：5个城市EBIT≥0"
      measure: "EBIT≥0城市数≥5"
    - anchor: "01-problem-definition.md#sc-y3"
      label: "第3年末：Portfolio整体EBIT转正"
      measure: "Portfolio EBIT率≥0%"
    - anchor: "01-problem-definition.md#sc-y5"
      label: "第5年末：10城或6个优化后城市EBIT率≥8-10%"
      measure: "EBIT率≥8%"
---

# Step 1: Problem Definition

## Context

Instant Retail Co. 是一家全国性即时购物平台，在中国 10 个三四线城市提供 30-60 分钟配送服务。公司已进入三四线城市多年，但盈利能力低下——9/10 城处于亏损，年合计亏损约 **1.35-1.5 亿元**。

CSO 邀请团队制定 **3-5 年增长与盈利战略**，核心挑战是：在资金约束（每年烧钱 1.35 亿+）和时间压力（5 月 4 日截止）下，找到可复制的三四线盈利模型。

**关键数据**：
- 10 城日均合计约 75-76 万单，年营收规模约 150-160 亿元
- 平均 AOV 54.8 元，履约成本 10.1 元/单，补贴 4.2 元/单
- 单均总可变成本 14.3 元/AOV 占比 26.1%
- 高价值用户占比仅 20%（行业健康值 30-40%）
- 仅 C3 泉州基本盈亏平衡，C8 威海接近平衡

---

## Key Question

> **如何让 Instant Retail Co. 在三四线城市实现 3-5 年可持续增长并扭亏为盈？**

---

## Scope

- **In scope**: 10 个选定三四线城市的增长与盈利战略；3-5 年时间范围；可落地的战略举措
- **Out of scope**: 一二线城市策略；全国网络扩张；并购/融资方案
- **Time horizon**: 3-5 年（2026-2029/2031）
- **Geography**: 10 个选定城市，聚焦优先、不盲目扩张

---

## Success Criteria

| 时间节点 | 目标 | 具体指标 |
|---------|------|---------|
| 第 1 年末 | 3 个城市 EBIT≥0；年亏损 <5,000 万 | C3 泉州、C7 惠州、C8 威海；止血优先 |
| 第 2 年末 | 5 个城市 EBIT≥0 | 徐州、南昌、南宁纳入 |
| 第 3 年末 | Portfolio 整体 EBIT 转正 | 亏损城市收缩或转型轻资产 |
| 第 5 年末 | 优化后城市 EBIT 率 ≥8-10% | 6-10 城健康盈利 |

**量化达标线**：

| 指标 | 当前均值 | 止血目标 | 稳健目标 | 优秀目标 |
|------|---------|---------|---------|---------|
| AOV（元） | 54.8 | 58+ | 62-65 | 65+ |
| 履约成本/单（元） | 10.1 | <10.0 | <9.5 | <9.0 |
| 补贴/单（元） | 4.2 | <4.0 | <3.5 | <3.0 |
| 成本/AOV | 26.1% | <24% | <20% | <18% |
| 高价值用户占比 | ~20% | >24% | >28% | >32% |

---

## Constraints

| 约束类型 | 说明 | 优先级 |
|---------|------|--------|
| 资金 | 年亏损 1.35 亿+，12-18 个月必须证明 2-3 城能造血 | **Critical** |
| 竞争 | 不能贸然停补贴（订单会流失）；需精准化补贴策略 | High |
| 时间 | 5 月 4 日 PPT 截止，15 页限制 | High |
| 数据 | 缺月度/季度数据、用户留存曲线、竞品数据 | Medium |
| 组织 | 不同城市运营成熟度差异大，新城市供应链积累浅 | Medium |
| 监管 | 灵活用工政策收紧可能推高履约成本 | Low |

---

## Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| CSO（首席战略官） | 决策者 | 3-5 年战略方向，EBIT 转正路径 |
| 运营团队 | 执行者 | 可落地的城市级行动方案 |
| 商家（连锁商超/便利店） | 合作伙伴 | 合作模式、佣金/分成比例 |
| 投资者/董事会 | 监督者 | 资金效率、ROI、退出时间线 |

---

## Initial Hypotheses

### Hypothesis 1（核心）：单位经济结构性不匹配
> 三四线盈利困境并非市场本身的问题，而是**"城市质量 + 用户质量 + 品类结构"三维失衡**导致的单位经济结构性不匹配。

**支撑数据**：
- 泉州 vs 赣州：履约成本几乎相同（10.2 vs 10.9 元），但 AOV 差 38%（62 vs 45 元），成本/AOV 差 13pp
- C8 威海 AOV 65 元 + 履约成本 9 元 = 最优组合；C10 赣州 AOV 45 元 + 履约成本 10.9 元 = 最差组合
- 关键变量不是履约成本，是 **AOV 和高价值用户占比**

### Hypothesis 2：城市质量比城市数量更重要
> 订单量增长没有自动改善单位经济——C1 徐州日均 11 万单最大但亏损最高（2,500 万），C10 赣州 3 万单也亏损 1,500 万。

### Hypothesis 3：品类结构影响毛利率
> 生鲜毛利率 15-25%、餐饮 30-40%、到家快消 40-55%；C8 威海品类结构更偏向高毛利品类（到家快消 33%、餐饮仅 20%）。

### Hypothesis 4：补贴效率低下是表层问题
> 80% 的补贴流向非高价值用户；C10 赣州补贴最重（4.9 元）但高价值用户最少（15%）。

---

## Three-Layer Root Cause（Profit Bridge）

| 层次 | 根因 | 现象 | 代表城市 |
|------|------|------|---------|
| **表层** | 补贴效率低下 | 高价值用户仅 20%，80% 补贴浪费 | C9/C10/C4 |
| **中层** | 品类结构偏低端 | 生鲜+餐饮占比 53-65%，拉低毛利 | 多数城市 |
| **深层** | 城市组合质量失衡 | 低 AOV + 高补贴 + 低大超占比集合 | C9/C10/C4 |

---

## Geographic Strategy: 10-City Deep Dive (Not Expansion)

| 阶段 | 时间 | 核心城市 | 策略 |
|------|------|---------|------|
| 止血期 | 第 1 年 | 泉州、惠州、威海（3 城） | 集中资源，验证盈利模型 |
| 增长期 | 第 2-3 年 | +徐州、南昌、南宁（6 城） | 复制成功模型 |
| 选择期 | 第 3-5 年 | 桂林/赣州/洛阳（条件成熟时） | 全覆盖或主动收缩 |

**10 城样本已具多样性，不应再盲目扩张。**

---

*Generated from TEAMMATE_ANSWERS_MERGED.md + 10-city dataset*
*Analysis: Bain Profit Bridge, Market Attractiveness vs. Competitive Position Matrix*
