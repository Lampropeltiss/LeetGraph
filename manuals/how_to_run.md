## 🚀 Быстрый старт

### Локальный запуск

1. **Клонирование репозитория**
```bash
git clone https://github.com/your-username/leetcode-stats-tracker.git
cd leetcode-stats-tracker
```

2. **Установка зависимостей**
```bash
pip install -r requirements.txt
```

3. **Запуск скрипта**
```bash
python main.py
```

### GitHub Actions (автоматический режим)

Просто запушьте код в репозиторий — workflow запустится автоматически каждый день в 00:00 UTC.

**Ручной запуск**:
- Перейдите в раздел Actions → Daily LeetCode Stats Update → Run workflow


## 🎨 Настройка темы

Все визуальные настройки в `theme.py`:

```python
leetcode_palette = {
    "background": "#1a1a1a",  # Фон графика
    "canvas": "#282828",      # Фон области графика
    "easy": "#1cbaba",        # Цвет легких задач
    "medium": "#ffb700",      # Цвет средних задач
    "hard": "#f63737",        # Цвет сложных задач
    # ... и другие настройки
}
```

## 🔧 Настройка под другого пользователя

Измените в `main.py`:
```python
leetcode_username = "your_username"  # Замените на нужный username
```