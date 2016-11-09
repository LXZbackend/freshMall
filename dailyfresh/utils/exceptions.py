class EcomException(Exception):

    """
    项目异常基类
    """
    code = 501
    message = '服务器内部错误!'
