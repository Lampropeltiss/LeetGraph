import pandas as pd


# Функция для заполнения пропусков с накоплением (forward fill)
def fill_missing_values(df, columns):
    """
    Заполняет пропущенные значения в указанных колонках:
    1. Сначала forward fill (переносим предыдущие значения)
    2. Оставшиеся NaN в начале заполняем нулями
    """
    for col in columns:
        if col in df.columns:
            # Преобразуем в число
            df[col] = pd.to_numeric(df[col], errors='coerce')
            # Считаем пропуски до и после
            before_count = df[col].isna().sum()

            if before_count > 0:
                # Forward fill - заполняем пропуски предыдущими значениями
                df[col] = df[col].ffill()
                # Оставшиеся NaN в начале заполняем нулями
                df[col] = df[col].fillna(0)
                after_count = df[col].isna().sum()

            # Преобразуем в int
            df[col] = df[col].astype(int)

    return df


def prepare_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'])

    problem_columns = ['easy', 'medium', 'hard', 'total_solved']
    df = fill_missing_values(df, problem_columns)

    df['easy_new'] = df['easy'].diff().fillna(df['easy']).astype(int)
    df['medium_new'] = df['medium'].diff().fillna(df['medium']).astype(int)
    df['hard_new'] = df['hard'].diff().fillna(df['hard']).astype(int)
    return df
