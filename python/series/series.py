def slices(series, length):
    if not 0 < length <= len(series):
        raise ValueError
    series = [int(d) for d in series]
    series_end = len(series) + 1
    extents = zip(range(series_end), range(length, series_end))
    return [series[start:end] for start, end in extents]
