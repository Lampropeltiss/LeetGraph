import os
import pandas as pd

def log_last(df, output_dir, date_format='%d %b', filename='stat_log'):
    file_path = os.path.join(output_dir, f"{filename}.txt")
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("\n" + "=" * 55 + "\n")
        f.write("📊 Прогресс за последние 14 дней".center(55) + "\n")
        f.write("=" * 55 + "\n")

        selected_columns = ['date', 'rank', 'easy_new', 'medium_new', 'hard_new']
        subset_15 = df[selected_columns].tail(15).copy()
        subset_15['rank_up'] = -(subset_15['rank'].diff().fillna(0).astype(int))
        subset_14 = subset_15.iloc[1:].copy()
        subset_14 = subset_14[['date', 'rank_up', 'easy_new', 'medium_new', 'hard_new']]

        # Форматируем столбец date с днём недели, если он существует и имеет тип datetime
        if 'date' in subset_14.columns:
            if pd.api.types.is_datetime64_any_dtype(subset_14['date']):
                days_of_week = subset_14['date'].dt.day_name().str[:3]
                formatted_date = subset_14['date'].dt.strftime(date_format)
                subset_14['date'] = formatted_date + ' (' + days_of_week + ')'

        # Заменяем нулевые значения на '-' в указанных колонках
        columns_to_replace = ['easy_new', 'medium_new', 'hard_new']
        for col in columns_to_replace:
            if col in subset_14.columns:
                subset_14[col] = subset_14[col].astype('object')
                mask = subset_14[col] == 0
                subset_14.loc[mask, col] = '-'

        # Записываем в файл без индекса (номеров строк)
        f.write(subset_14.to_string(index=False) + "\n")
        f.write("=" * 55 + "\n")

        print(f"📄 Статистика успешно сохранена в файл: {file_path}")

        # Вывод последних 3 строк
        print(f"📄 Последние 3 строки:")
        print("   " + "-" * 55)
        for _, row in subset_14.tail(3).iterrows():
            print(
                f"      {row['date']:<20} {row['rank_up']:>8} {row['easy_new']:>8} {row['medium_new']:>10} {row['hard_new']:>8}")
        print("   " + "-" * 55)

        return file_path
