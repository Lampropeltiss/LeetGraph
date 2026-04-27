import csv
import os


def append_to_csv(stats, csv_file):
    """
    Добавляет новую строку в CSV или обновляет последнюю строку с той же датой

    Args:
        stats: dict с данными для добавления
        csv_file: путь к CSV файлу

    Returns:
        str: статус операции ('added', 'updated', 'skipped')
    """
    file_exists = os.path.exists(csv_file)

    # Если файл не существует, создаем новый
    if not file_exists:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=stats.keys())
            writer.writeheader()
            writer.writerow(stats)
        print(f"✅ Создан новый файл и добавлена строка: {stats['date']}")
        return 'added'

    # Читаем все строки файла
    rows = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Проверяем последнюю строку
    if rows:
        last_row = rows[-1]

        # Если дата совпадает с последней строкой
        if last_row.get('date') == stats.get('date'):
            # Сравниваем все поля
            is_identical = all(str(last_row.get(key)) == str(stats.get(key)) for key in fieldnames)

            if is_identical:
                print(f"⏭️ Строка с датой {stats['date']} уже существует и не изменилась. Пропущено.")
                return 'skipped'
            else:
                # Обновляем последнюю строку
                rows[-1] = stats
                # Перезаписываем весь файл
                with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                print(f"🔄 Обновлена строка с датой: {stats['date']}")
                print(f"   Было: {dict(last_row)}")
                print(f"   Стало: {stats}")
                return 'updated'

    # Если дата новая, просто добавляем в конец
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=stats.keys())
        writer.writerow(stats)

    print(f"✅ Добавлена новая строка: {stats['date']}")
    return 'added'
