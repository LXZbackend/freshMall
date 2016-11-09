from datetime import datetime, timedelta


def model_to_dict(obj, exclude=None):
    """model对象转字典
    """
    d = vars(obj)
    d.pop('_state')
    if exclude:
        for key in exclude:
            d.pop(key)
    for key in d.keys():
        if isinstance(d[key], datetime):
            d[key] = _format_datetime(d[key])
    return d


def _format_datetime(dt):
    return (dt + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%H%z')
