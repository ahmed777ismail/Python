# 🚀 Python Basics Learning Path (Week 1)

A structured 7-day plan to build strong Python fundamentals with daily practice + daily GitHub commits.

---

## 📚 Mastering Python (Basics) — Week 1

### 🟢 Week 1 Plan (Day 1 → Day 7)

| #    | Day | Topic | 🟢 Recommended Time | 🟡 Goal | 🔴 Prerequisites | 📦 Deliverables |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P01  | D1  | Setup Python + VS Code + Run Script | 30–60 min | تجهيز البيئة وتشغيل أول ملف `.py` | Basic computer literacy | `day1/notes.md`, `day1/hello.py` |
| P02  | D1  | Basic Syntax + Indentation + Comments | 60–90 min | تفهم شكل الكود في بايثون وقواعد الـ indentation | P01 | `day1/syntax_basics.py` |
| P03  | D1  | Variables + Naming + Input/Output | 60–90 min | تتعامل مع المتغيرات و `input()` و `print()` | P02 | `day1/tasks.py` |
| P04  | D1  | Mini Task: Greeting Script | 30–45 min | أول سكريبت فعلي (اسم + سن + رسالة) | P03 | `day1/mini_task_greeting.py` |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P05  | D2  | Data Types: int/float/str/bool | 60–90 min | تعرف الأنواع الأساسية وتفهم `type()` | P03 | `day2/types.py` |
| P06  | D2  | Type Casting: int()/float()/str() | 45–75 min | تحول البيانات صح من input (string) لأرقام | P05 | `day2/casting.py` |
| P07  | D2  | Operators: + - * / // % ** | 60–90 min | تتعامل مع العمليات والحسابات بدون لخبطه | P06 | `day2/operators_tasks.py` |
| P08  | D2  | Mini Project: CLI Calculator v1 | 60–90 min | تعمل آلة حاسبة بسيطة (جمع/طرح/ضرب/قسمة) | P07 | `day2/calculator_v1.py` |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P09  | D3  | Conditionals: if/elif/else | 60–90 min | تتحكم في مسار البرنامج بناءً على شروط | P07 | `day3/conditions.py` |
| P10  | D3  | Comparisons + Logical ops (and/or/not) | 45–75 min | تكتب شروط مركبة بشكل صحيح | P09 | `day3/logic_tasks.py` |
| P11  | D3  | Mini Task: Grade Checker | 45–75 min | برنامج درجات (A/B/C/D/F) | P10 | `day3/grade_checker.py` |
| P12  | D3  | Mini Task: Simple Login Check | 45–75 min | تحقق يوزر/باسورد بسيط | P10 | `day3/simple_login.py` |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P13  | D4  | Loops: for + range() | 60–90 min | تكرار وتنفيذ مهام على أرقام/قوائم | P09 | `day4/for_loop_tasks.py` |
| P14  | D4  | while loop + loop control | 60–90 min | تكرار بشرط + تفهم الـ infinite loop | P13 | `day4/while_loop_tasks.py` |
| P15  | D4  | break/continue | 30–45 min | تتحكم في مسار اللوب | P14 | `day4/break_continue.py` |
| P16  | D4  | Mini Project: Guess The Number | 75–120 min | لعبة تخمين رقم + count attempts | P15 | `day4/guess_game.py` |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P17  | D5  | Lists (create/index/slice/append/pop) | 75–120 min | تتعامل مع list كأداة يومية | P13 | `day5/lists.py` |
| P18  | D5  | Tuples (immutability) | 30–45 min | تعرف إمتى تستخدم tuple | P17 | `day5/tuples.py` |
| P19  | D5  | Sets (unique values) | 45–60 min | إزالة التكرارات + عمليات set | P17 | `day5/sets.py` |
| P20  | D5  | Dictionaries (key/value) | 75–120 min | تخزين بيانات بشكل mapping | P17 | `day5/dicts.py` |
| P21  | D5  | Mini Project: Students Grades Tracker v1 | 90–150 min | Menu بسيط لإضافة/تعديل/عرض درجات | P20 | `day5/students_tracker_v1.py` |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P22  | D6  | Functions: def/params/return | 75–120 min | تفصل المنطق وتعيد استخدامه | P13 | `day6/functions_basics.py` |
| P23  | D6  | Default args + simple scope | 45–75 min | تتحكم في الـ parameters وتفهم local/global | P22 | `day6/scope_defaults.py` |
| P24  | D6  | Practice Functions: prime/factorial/even | 90–150 min | تبني مكتبة دوال صغيرة | P22 | `day6/math_utils.py` |
| P25  | D6  | Refactor: Calculator & Tracker using functions | 90–150 min | تحول مشاريع سابقة لكود منظم | P24 | `day6/refactor_calculator.py`, `day6/refactor_tracker.py` |
|------|-----|-------|---------------------|--------|------------------|----------------|
| P26  | D7  | Exceptions: try/except + ValueError | 60–90 min | تمنع البرنامج يقع بسبب input غلط | P06, P22 | `day7/exceptions_basics.py` |
| P27  | D7  | Input Validation patterns | 60–90 min | تتحقق من القيم قبل ما تستخدمها | P26 | `day7/validation_helpers.py` |
| P28  | D7  | Final Project: CLI Menu App | 120–240 min | مشروع يجمع (Loops + Dict + Functions + Exceptions) | P21, P25, P27 | `day7/final_project.py`, `day7/README.md` |

---

## 📂 Repo Structure

```txt
python-basics-week1/
│
├── README.md
├── day1/
├── day2/
├── day3/
├── day4/
├── day5/
├── day6/
└── day7/
