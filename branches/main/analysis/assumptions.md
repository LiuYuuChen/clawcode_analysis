
## T-10 Assumptions

- [T-10-A01] render-to-screen.ts 使用 LegacyRoot reconciler，可能是旧版遗留或测试用入口；ink.tsx 使用 ConcurrentRoot 是生产入口。需 T-11 验证具体使用场景。
- [T-10-A02] diffScreens() 同步阻塞在正常交互场景下可接受（throttle 限制约 16fps），但在极端消息量（>10000 行）下可能有性能问题，未验证。
- [T-10-A03] VirtualMessageList 的虚拟化在 DOMElement 层实现（不渲染视口外的 DOM 节点），但具体截断策略和 Yoga 布局交互方式需 T-11 深入确认。
- [T-10-A04] termio/parser.ts 的 paste 模式（bracketed paste）处理基于 CSI 2024h/l 序列，假设终端支持该扩展。不支持时 paste 会被拆分为逐字符 keypress 事件。
- [T-10-A05] AlternateScreen 组件通过 requestAltScreen()/exitAltScreen() 控制终端 alt screen 缓冲区切换，假设终端支持 xterm alt screen (CSI ?1049h/l)。
- [T-10-A06] StylePool 的 5 分钟周期重置(charPool/hyperlinkPool)足以防止长会话内存泄漏，但未验证极端长会话（>24h）的内存表现。
- [T-10-A07] ink.tsx 的 scheduleRender 使用 lodash throttle + queueMicrotask，假设 Node.js 的 microtask 调度在终端场景下足够及时（<16ms 延迟）。
- [T-10-A08] output.ts 的 Unicode 处理（stringWidth, wrapText）假设输入为有效 UTF-8。无效编码可能导致列宽计算错误但不影响系统稳定性。

