import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from collections import deque

# ── 数字映射 ──────────────────────────────────────────
TO_ROMAN = {1: 'Ⅰ', 2: 'Ⅱ', 3: 'Ⅲ', 4: 'Ⅳ', 5: 'Ⅴ',
            6: 'Ⅵ', 7: 'Ⅶ', 8: 'Ⅷ', 9: 'Ⅸ', 10: 'Ⅹ'}
TO_NUM = {v: k for k, v in TO_ROMAN.items()}

MAX = 10

# ── 配色 ──────────────────────────────────────────────
LIGHT = {
    'bg': '#f8f9fa', 'frame': '#ffffff', 'accent': '#2d8bfd',
    'warn': '#fd7e14', 'grid': '#dee2e6', 'box': ['#f1f3f5', '#ffffff'],
    'fg': '#212529', 'sub_fg': '#495057', 'status_fg': '#212529',
}
DARK = {
    'bg': '#212529', 'frame': '#343a40', 'accent': '#6ea8fe',
    'warn': '#ffca2c', 'grid': '#495057', 'box': ['#3b3e43', '#343a40'],
    'fg': '#f8f9fa', 'sub_fg': '#ced4da', 'status_fg': '#f8f9fa',
}

# ── 求解器（纯函数）──────────────────────────────────
def _box_range(sz, r, c):
    if sz == 4:
        return r // 2 * 2, c // 2 * 2, 2, 2
    elif sz == 6:
        return r // 2 * 2, c // 3 * 3, 2, 3
    elif sz == 10:
        return r // 2 * 2, c // 5 * 5, 2, 5
    else:
        return r // 3 * 3, c // 3 * 3, 3, 3

def is_safe(grid, sz, r, c, val):
    for j in range(sz):
        if grid[r][j] == val:
            return False
    for i in range(sz):
        if grid[i][c] == val:
            return False
    sr, sc, rh, ch = _box_range(sz, r, c)
    for i in range(rh):
        for j in range(ch):
            if grid[sr + i][sc + j] == val:
                return False
    return True

def solve(grid, sz):
    """MRV 回溯求解，返回 True/False，结果直接写入 grid"""
    best_r = best_c = -1
    best_cands = None
    for r in range(sz):
        for c in range(sz):
            if grid[r][c] == 0:
                cands = [v for v in range(1, sz + 1) if is_safe(grid, sz, r, c, v)]
                if not cands:
                    return False
                if best_cands is None or len(cands) < len(best_cands):
                    best_r, best_c = r, c
                    best_cands = cands
                    if len(cands) == 1:
                        break
        if best_cands and len(best_cands) == 1:
            break
    if best_cands is None:
        return True
    r, c = best_r, best_c
    random.shuffle(best_cands)
    for v in best_cands:
        grid[r][c] = v
        if solve(grid, sz):
            return True
        grid[r][c] = 0
    return False


# ── 主应用类 ──────────────────────────────────────────
class SudokuApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("罗马数独 - 终极版")
        self.root.geometry("860x800")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self._setup_styles()

        # 游戏设置
        self.dark_mode = False
        self.use_roman = False
        self.colors = LIGHT

        # 游戏状态
        self.size = 9
        self.board = [[0] * MAX for _ in range(MAX)]
        self.init_board = [[0] * MAX for _ in range(MAX)]
        self.solution = [[0] * MAX for _ in range(MAX)]
        self.user_marks = [[[0] * (MAX + 1) for _ in range(MAX)] for _ in range(MAX)]
        self.history = deque()
        self.selected = (-1, -1)

        # 统计
        self.step_cnt = 0
        self.hint_cnt = 0
        self.err_cnt = 0
        self.err_log = []
        self.play_total = 0
        self.play_win = 0
        self.play_fail = 0
        self.play_giveup = 0
        self.best_time = {sz: 0 for sz in [4, 6, 9, 10]}

        # 计时
        self.timer_running = False
        self.start_time = 0
        self.limit_sec = 0
        self._timer_job = None

        # 专业模式
        self.is_pro = False
        self.pro_change_cnt = 0
        self.pro_last_change = 0
        self._pro_check_job = None

        # UI 控件引用
        self.cells = [[None] * MAX for _ in range(MAX)]
        self.frame_board = None
        self.lbl_info = None
        self.lbl_timer = None
        self.entry_val = None

        self._apply_theme()
        self.root.after(100, self._show_menu)

    # ── 音效 ──────────────────────────────────────────
    def _beep(self, freq, duration):
        try:
            import winsound
            winsound.Beep(freq, duration)
        except Exception:
            pass

    def _sfx_click(self):
        self.root.after(10, lambda: self._beep(1600, 60))

    def _sfx_ok(self):
        self.root.after(10, lambda: self._beep(2200, 120))

    def _sfx_err(self):
        self.root.after(10, lambda: self._beep(800, 120))

    # ── 样式 ──────────────────────────────────────────
    def _setup_styles(self):
        s = self.style
        s.configure('Card.TFrame', relief='flat')
        s.configure('Title.TLabel', font=('微软雅黑', 28, 'bold'))
        s.configure('Subtitle.TLabel', font=('微软雅黑', 12))
        s.configure('Status.TLabel', font=('Consolas', 11, 'bold'))
        s.configure('GameBtn.TButton', font=('微软雅黑', 10, 'bold'), padding=8)
        s.configure('Action.TButton', font=('微软雅黑', 9, 'bold'), padding=6)

    def _apply_theme(self):
        c = self.colors
        self.root.configure(bg=c['bg'])
        self.style.configure('Card.TFrame', background=c['frame'])
        self.style.configure('Title.TLabel', background=c['bg'], foreground=c['fg'])
        self.style.configure('Subtitle.TLabel', background=c['bg'], foreground=c['sub_fg'])
        self.style.configure('Status.TLabel', background=c['frame'], foreground=c['status_fg'])

    def _toggle_dark(self):
        self.dark_mode = not self.dark_mode
        self.colors = DARK if self.dark_mode else LIGHT
        self._apply_theme()
        self._back_to_menu()

    # ── 清理 ──────────────────────────────────────────
    def _clear_widgets(self):
        for w in list(self.root.winfo_children()):
            w.destroy()
        self.cells = [[None] * MAX for _ in range(MAX)]
        self.frame_board = None
        self.lbl_info = None
        self.lbl_timer = None
        self.entry_val = None

    def _cancel_timers(self):
        if self._timer_job:
            self.root.after_cancel(self._timer_job)
            self._timer_job = None
        if self._pro_check_job:
            self.root.after_cancel(self._pro_check_job)
            self._pro_check_job = None
        self.timer_running = False

    # ── 游戏逻辑 ──────────────────────────────────────
    def _new_board(self):
        self.board = [[0] * MAX for _ in range(MAX)]
        self.init_board = [[0] * MAX for _ in range(MAX)]
        self.solution = [[0] * MAX for _ in range(MAX)]
        self.user_marks = [[[0] * (MAX + 1) for _ in range(MAX)] for _ in range(MAX)]
        self.history.clear()
        self.step_cnt = self.hint_cnt = self.err_cnt = 0
        self.selected = (-1, -1)

    def _generate(self, sz):
        self._new_board()
        # 随机种子
        for _ in range(sz // 2):
            r, c = random.randint(0, sz - 1), random.randint(0, sz - 1)
            v = random.randint(1, sz)
            if self.board[r][c] == 0 and is_safe(self.board, sz, r, c, v):
                self.board[r][c] = v
        # 填到 solution 并求解
        for i in range(sz):
            for j in range(sz):
                self.solution[i][j] = self.board[i][j]
        if not solve(self.solution, sz):
            # 种子导致无解，重试
            return self._generate(sz)
        # 挖洞
        holes = {4: 6, 6: 14, 9: 42, 10: 50}.get(sz, 42)
        cnt = 0
        while cnt < holes:
            r, c = random.randint(0, sz - 1), random.randint(0, sz - 1)
            if self.board[r][c] != 0:
                self.board[r][c] = 0
                cnt += 1
        for i in range(sz):
            for j in range(sz):
                self.init_board[i][j] = self.board[i][j]

    def _refresh_pro_solution(self):
        for i in range(10):
            for j in range(10):
                self.solution[i][j] = self.board[i][j]
        solve(self.solution, 10)
        self.pro_change_cnt += 1
        self.pro_last_change = time.time()
        messagebox.showinfo("专业模式", f"答案已刷新！(第 {self.pro_change_cnt} 次)")
        if self.pro_change_cnt == 2:
            for i in range(10):
                for j in range(10):
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.solution[i][j]
                        self._render_cell(i, j)
                        messagebox.showinfo("提示", "已变化2次，自动提示一格")
                        return
        if self.pro_change_cnt >= 3:
            self.play_fail += 1
            self._sfx_err()
            messagebox.showerror("失败", "变化3次未完成，挑战失败！")
            self._back_to_menu()

    def _check_pro_refresh(self):
        if not self.is_pro:
            return
        if time.time() - self.pro_last_change >= 900:
            self._refresh_pro_solution()
        self._pro_check_job = self.root.after(1000, self._check_pro_refresh)

    def start_game(self, sz, pro=False):
        self._sfx_click()
        self._cancel_timers()
        self.size = sz
        self.is_pro = pro
        self.play_total += 1

        if pro:
            self._generate(10)
            self.pro_change_cnt = 0
            self.pro_last_change = time.time()
        else:
            self._generate(sz)
            self.limit_sec = {4: 600, 6: 420, 9: 300}.get(sz, 300)

        self.timer_running = True
        self.start_time = time.time()
        self._build_game_ui()
        if pro:
            self._check_pro_refresh()
        self._tick_timer()

    def _restart(self):
        self._sfx_click()
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = self.init_board[i][j]
        self.history.clear()
        self.step_cnt = self.hint_cnt = self.err_cnt = 0
        self.selected = (-1, -1)
        self._refresh_all_cells()
        self._update_info()

    # ── 棋盘绘制 ──────────────────────────────────────
    def _build_game_ui(self):
        self._clear_widgets()
        c = self.colors

        # 顶栏
        top = ttk.Frame(self.root, style='Card.TFrame', padding=12)
        top.pack(fill='x', padx=20, pady=10)
        self.lbl_info = ttk.Label(top, style='Status.TLabel')
        self.lbl_info.pack(side='left')
        self.lbl_timer = ttk.Label(top, style='Status.TLabel',
                                   foreground=c['accent'])
        self.lbl_timer.pack(side='right')
        self._update_info()

        # 棋盘
        self.frame_board = ttk.Frame(self.root, style='Card.TFrame', padding=12)
        self.frame_board.pack(pady=10)
        self._build_cells()

        # 按钮行
        ctrl = ttk.Frame(self.root, padding=8)
        ctrl.pack(pady=6)
        btns = [
            ("填写", self._set_cell), ("标记", self._mark_cell),
            ("撤销", self._undo), ("提示", self._hint),
            ("重开", self._restart), ("菜单", self._back_to_menu),
        ]
        for idx, (txt, cmd) in enumerate(btns):
            ttk.Button(ctrl, text=txt, command=cmd,
                       style='Action.TButton', width=11).grid(
                row=0, column=idx, padx=4, pady=4)

        # 输入框
        inp = ttk.Frame(self.root, padding=8)
        inp.pack(pady=8)
        ttk.Label(inp, text="数字:", background=c['bg'],
                  font=('微软雅黑', 11, 'bold')).grid(row=0, column=0)
        self.entry_val = ttk.Entry(inp, width=6, font=('Consolas', 14, 'bold'))
        self.entry_val.grid(row=0, column=1, padx=6)
        self.entry_val.focus()

    def _build_cells(self):
        self.cells = [[None] * MAX for _ in range(MAX)]
        pad = 1
        fs = {4: 56, 6: 46, 9: 36, 10: 30}[self.size]
        for i in range(self.size):
            for j in range(self.size):
                _, _, rh, ch = _box_range(self.size, i, j)
                box_idx = (i // rh) * (self.size // ch) + (j // ch)
                bg = self.colors['box'][box_idx % 2]
                e = tk.Entry(self.frame_board, width=4,
                             font=('Segoe UI', fs, 'bold'),
                             justify='center', bg=bg, relief='flat')
                e.grid(row=i, column=j, padx=pad, pady=pad)
                e.bind('<Button-1>', lambda ev, x=i, y=j: self._on_cell_click(x, y))
                self.cells[i][j] = e
        self._refresh_selection()
        self._refresh_all_cells()

    def _render_cell(self, i, j):
        e = self.cells[i][j]
        if e is None:
            return
        v = self.board[i][j]
        e.config(state='normal')
        e.delete(0, tk.END)
        if v != 0:
            txt = TO_ROMAN[v] if self.use_roman else str(v)
            e.insert(0, txt)
            e.config(state='readonly',
                     fg=self.colors['fg'])
        else:
            has_mark = any(self.user_marks[i][j][1:self.size + 1])
            e.config(fg=self.colors['warn'] if has_mark else self.colors['accent'])

    def _refresh_all_cells(self):
        for i in range(self.size):
            for j in range(self.size):
                self._render_cell(i, j)

    def _refresh_selection(self):
        for i in range(self.size):
            for j in range(self.size):
                e = self.cells[i][j]
                if e is None:
                    continue
                sel = (i == self.selected[0] and j == self.selected[1])
                e.config(highlightthickness=2 if sel else 1,
                         highlightbackground=self.colors['accent'] if sel else self.colors['grid'])

    def _update_info(self):
        if self.lbl_info is None:
            return
        mode = "罗马" if self.use_roman else "阿拉伯"
        self.lbl_info.config(
            text=f"步数:{self.step_cnt:2d} | 错题:{self.err_cnt:2d} | 提示:{self.hint_cnt:2d} | 显示:{mode}")

    # ── 计时 ──────────────────────────────────────────
    def _tick_timer(self):
        if not self.timer_running:
            if self.lbl_timer:
                self.lbl_timer.config(text="计时未开始")
            return
        used = int(time.time() - self.start_time)
        m, s = divmod(used, 60)
        if self.lbl_timer:
            self.lbl_timer.config(text=f"用时 {m:02d}:{s:02d}")
        if not self.is_pro and self.limit_sec > 0 and used > self.limit_sec:
            self.play_fail += 1
            self._sfx_err()
            messagebox.showerror("超时", "时间到，挑战失败")
            self._back_to_menu()
            return
        self._timer_job = self.root.after(1000, self._tick_timer)

    # ── 玩家操作 ──────────────────────────────────────
    def _on_cell_click(self, i, j):
        if self.board[i][j] != 0:
            return
        self._sfx_click()
        self.selected = (i, j)
        self._refresh_selection()

    def _set_cell(self):
        r, c = self.selected
        if r == -1:
            messagebox.showwarning("提示", "请先点击格子")
            return
        try:
            v = int(self.entry_val.get())
        except ValueError:
            messagebox.showwarning("提示", "请输入数字")
            return
        if v < 1 or v > self.size:
            self._sfx_err()
            messagebox.showwarning("提示", "数字超出范围")
            return
        if self.board[r][c] != 0:
            self._sfx_err()
            messagebox.showwarning("提示", "该格已有数字")
            return

        self.step_cnt += 1
        if not is_safe(self.board, self.size, r, c, v):
            self._sfx_err()
            messagebox.showerror("错误", "行/列/宫重复")
            self._update_info()
            return
        if v != self.solution[r][c]:
            u = TO_ROMAN[v] if self.use_roman else str(v)
            rt = TO_ROMAN[self.solution[r][c]] if self.use_roman else str(self.solution[r][c])
            self.err_log.append((r + 1, c + 1, u, rt))
            self.err_cnt += 1
            self._sfx_err()
            messagebox.showwarning("错误", "答案不正确")
            self._update_info()
            return

        self.history.append((r, c, self.board[r][c]))
        self.board[r][c] = v
        self._render_cell(r, c)
        self._sfx_ok()
        self._update_info()
        if self._check_win():
            self._win()

    def _mark_cell(self):
        r, c = self.selected
        if r == -1:
            return
        try:
            v = int(self.entry_val.get())
        except ValueError:
            return
        if 1 <= v <= self.size:
            self.user_marks[r][c][v] = not self.user_marks[r][c][v]
            self._render_cell(r, c)

    def _undo(self):
        self._sfx_click()
        if not self.history:
            messagebox.showinfo("提示", "无操作可撤销")
            return
        r, c, old = self.history.pop()
        self.board[r][c] = old
        self._render_cell(r, c)
        self.step_cnt += 1
        self._update_info()

    def _hint(self):
        self._sfx_click()
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    self.history.append((i, j, 0))
                    self.board[i][j] = self.solution[i][j]
                    self._render_cell(i, j)
                    self.hint_cnt += 1
                    self.step_cnt += 1
                    self._update_info()
                    return

    def _check_win(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != self.solution[i][j]:
                    return False
        return True

    def _win(self):
        self.play_win += 1
        used = int(time.time() - self.start_time)
        if self.best_time[self.size] == 0 or used < self.best_time[self.size]:
            self.best_time[self.size] = used
        self._sfx_ok()
        messagebox.showinfo("恭喜通关！", "挑战成功！")
        self._back_to_menu()

    # ── 菜单 ──────────────────────────────────────────
    def _back_to_menu(self):
        self._cancel_timers()
        self._show_menu()

    def _show_menu(self):
        self._clear_widgets()
        self._apply_theme()

        ttk.Label(self.root, text="罗马数独 - 完整版",
                  style='Title.TLabel').pack(pady=16)
        ttk.Label(self.root, text="点击格子输入 · 双显示模式 · 深浅主题 · 音效",
                  style='Subtitle.TLabel').pack(pady=2)

        # 切换按钮
        tf = ttk.Frame(self.root, style='Card.TFrame', padding=8)
        tf.pack(pady=6)
        ttk.Button(tf, text="深色模式" if not self.dark_mode else "浅色模式",
                   command=self._toggle_dark, style='GameBtn.TButton',
                   width=16).grid(row=0, column=0, padx=4, pady=4)
        ttk.Button(tf, text="罗马/阿拉伯切换",
                   command=self._toggle_display, style='GameBtn.TButton',
                   width=16).grid(row=0, column=1, padx=4, pady=4)

        # 难度按钮
        card = ttk.Frame(self.root, style='Card.TFrame', padding=20)
        card.pack(pady=10)
        opts = [
            ("4×4 简单", 4, False), ("6×6 中等", 6, False),
            ("9×9 困难", 9, False), ("噩梦随机", random.choice([4, 6, 9]), False),
            ("专业10×10", 10, True),
        ]
        for idx, (txt, sz, pro) in enumerate(opts):
            row, col = divmod(idx, 3)
            ttk.Button(card, text=txt,
                       command=lambda s=sz, p=pro: self.start_game(s, p),
                       style='GameBtn.TButton', width=14).grid(
                row=row, column=col, padx=8, pady=8)
        ttk.Button(card, text="退出游戏", command=self.root.quit,
                   style='GameBtn.TButton', width=14).grid(
            row=1, column=2, padx=8, pady=8)

        # 工具按钮
        bar = ttk.Frame(self.root, padding=10)
        bar.pack(pady=6)
        ttk.Button(bar, text="规则说明", command=self._show_rules,
                   style='Action.TButton', width=14).grid(row=0, column=0, padx=4, pady=4)
        ttk.Button(bar, text="错题", command=self._show_errors,
                   style='Action.TButton', width=10).grid(row=0, column=1, padx=4, pady=4)
        ttk.Button(bar, text="清空错题",
                   command=lambda: self.err_log.clear(),
                   style='Action.TButton', width=12).grid(row=0, column=2, padx=4, pady=4)
        ttk.Button(bar, text="统计", command=self._show_stats,
                   style='Action.TButton', width=10).grid(row=0, column=3, padx=4, pady=4)
        ttk.Button(bar, text="记录", command=self._show_best,
                   style='Action.TButton', width=10).grid(row=0, column=4, padx=4, pady=4)

    def _toggle_display(self):
        self._sfx_click()
        self.use_roman = not self.use_roman
        if self.frame_board is not None:
            self._refresh_all_cells()
            self._update_info()

    # ── 信息弹窗 ──────────────────────────────────────
    def _show_rules(self):
        self._sfx_click()
        msg = (
            "游戏规则\n\n"
            "1. 每行、每列、每个宫内数字不可重复\n"
            "2. 点击格子选中 → 输入数字 → 填写/标记\n\n"
            "难度说明\n"
            "4×4 简单 · 6×6 中等 · 9×9 困难 · 噩梦随机\n"
            "专业10×10：每15分钟刷新答案，3次未完成则失败"
        )
        messagebox.showinfo("规则说明", msg)

    def _show_errors(self):
        self._sfx_click()
        if not self.err_log:
            messagebox.showinfo("错题", "暂无错题")
            return
        lines = ["错题记录："]
        for idx, (r, c, u, rt) in enumerate(self.err_log, 1):
            lines.append(f"{idx:2d}. ({r},{c}) 你的:{u}  正确:{rt}")
        messagebox.showinfo("错题", "\n".join(lines))

    def _show_stats(self):
        self._sfx_click()
        total = self.play_total
        rate = (self.play_win / total * 100) if total > 0 else 0
        msg = (f"总游玩：{total}\n成功：{self.play_win}\n"
               f"失败：{self.play_fail}\n放弃：{self.play_giveup}\n"
               f"胜率：{rate:.1f}%")
        messagebox.showinfo("统计", msg)

    def _show_best(self):
        self._sfx_click()
        lines = ["最快记录："]
        for sz in [4, 6, 9, 10]:
            t = self.best_time[sz]
            if t:
                m, s = divmod(t, 60)
                lines.append(f"{sz}×{sz}  {m:02d}:{s:02d}")
        messagebox.showinfo("记录", "\n".join(lines))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SudokuApp()
    app.run()
