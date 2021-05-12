def transform(legacy_data: dict):
    try:
        return {value.lower(): key for key, value_list in legacy_data.items() for value in value_list}
    except AttributeError:
        raise AttributeError("Inserted data must be a dictionary")
