
def extract_column(col_name: str, array: list[dict]) -> list:
    if not array:
        raise ValueError("array must be a list of dictionaries")

    print(array)
    try:
        return [
            row[col_name]
            for row in array
            if row[col_name] is not None
        ]
    except Exception as e:
        print(f"There was an exception when parsing list: {e}")
        return []
