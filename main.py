from matplotlib import pyplot as plt
import os
import sys

from process_data.data_prepare import prepare_data
from process_data.log_last_data import print_stat
from process_data.data_parser import LeetCodeClient
from process_data.data_saver import append_to_csv
from theme import plt_settings, date_formats
from process_data.create_graph import build_graphic

if __name__ == '__main__':
    # Параметры
    leetcode_username = "lampropeltiss"
    data_filepath = 'data/leetcode_ranking.csv'
    output_dir = 'output'

    print("=" * 60)
    print("🚀 STARTING LEETCODE STATS UPDATE")
    print("=" * 60)

    print(f"\n📁 Configuration:")
    print(f"   Username: {leetcode_username}")
    print(f"   Data file: {data_filepath}")
    print(f"   Output dir: {output_dir}")
    print(f"   Python version: {sys.version}")
    print(f"   Working directory: {os.getcwd()}")

    # Шаг 1: Подготовка данных
    print("\n" + "=" * 60)
    print("📊 STEP 1: Preparing existing data")
    print("=" * 60)

    # Проверяем существование файла
    if os.path.exists(data_filepath):
        print(f"✅ Data file exists: {data_filepath}")
        file_size = os.path.getsize(data_filepath)
        print(f"   File size: {file_size} bytes")
    else:
        print(f"⚠️ Data file does not exist yet: {data_filepath}")

    df = prepare_data(data_filepath)
    print(f"✅ Data prepared successfully")
    print(f"   DataFrame shape: {df.shape}")
    print(f"   Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"   Last date: {df['date'].max()}")

    # Шаг 2: Получение новых данных с LeetCode
    print("\n" + "=" * 60)
    print("🌐 STEP 3: Fetching data from LeetCode API")
    print("=" * 60)

    print(f"   Connecting to LeetCode API for user: {leetcode_username}")
    client = LeetCodeClient(leetcode_username)

    try:
        stats = client.get_stats()
        print(f"✅ Data fetched successfully:")
        print(f"   Date: {stats['date']}")
        print(f"   Rank: {stats['rank']:,}")
        print(f"   Easy: {stats['easy']}")
        print(f"   Medium: {stats['medium']}")
        print(f"   Hard: {stats['hard']}")
        print(f"   Total solved: {stats['total_solved']}")
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        sys.exit(1)

    # Шаг 3: Сохранение статистики в текстовый файл
    print("\n" + "=" * 60)
    print("📝 STEP 2: Saving statistics log")
    print("=" * 60)

    print_stat(df, output_dir, date_formats['table'])
    print(f"✅ Statistics log saved to {output_dir}/stat_log.txt")

    # Шаг 4: Сохранение данных в CSV
    print("\n" + "=" * 60)
    print("💾 STEP 4: Saving data to CSV")
    print("=" * 60)

    result = append_to_csv(stats, data_filepath)
    print(f"   Result: {result}")

    if result == 'added':
        print(f"✅ New record added for {stats['date']}")
    elif result == 'updated':
        print(f"🔄 Existing record updated for {stats['date']}")
    elif result == 'skipped':
        print(f"⏭️ No changes for {stats['date']}")

    # Проверяем, изменился ли CSV после записи
    if os.path.exists(data_filepath):
        new_size = os.path.getsize(data_filepath)
        print(f"   CSV file size: {new_size} bytes")

    # Шаг 5: Обновляем DataFrame с новыми данными
    print("\n" + "=" * 60)
    print("🔄 STEP 5: Reloading data for graph")
    print("=" * 60)

    df = prepare_data(data_filepath)
    print(f"✅ Data reloaded: {df.shape[0]} records")
    print(f"   Last record: {df.iloc[-1]['date'].strftime('%Y-%m-%d') if not df.empty else 'None'}")

    # Шаг 6: Создание графика
    print("\n" + "=" * 60)
    print("📈 STEP 6: Generating graph")
    print("=" * 60)

    print(f"   Applying matplotlib settings...")
    plt.rcParams.update(plt_settings)
    print(f"   Matplotlib backend: {plt.get_backend()}")

    print(f"   Building graphic...")
    fig = build_graphic(plt, df, leetcode_username, date_formats['graph'])

    # Сохраняем график
    output_path = f"{output_dir}/leetcode_stat_graph.png"
    print(f"   Saving graph to: {output_path}")
    fig.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    # Проверяем, создался ли файл
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path)
        print(f"✅ Graph saved successfully: {output_path}")
        print(f"   File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
    else:
        print(f"❌ Failed to save graph!")
        sys.exit(1)

    # Шаг 7: Финальная проверка
    print("\n" + "=" * 60)
    print("✅ FINAL CHECK")
    print("=" * 60)

    # Проверяем все выходные файлы
    files_to_check = [
        data_filepath,
        f"{output_dir}/stat_log.txt",
        f"{output_dir}/leetcode_stat_graph.png"
    ]

    for file_path in files_to_check:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"   ✓ {file_path} ({size} bytes)")
        else:
            print(f"   ✗ {file_path} (MISSING)")

    print("\n" + "=" * 60)
    print("🎉 LEETCODE STATS UPDATE COMPLETED SUCCESSFULLY!")
    print("=" * 60)
