import hashlib


def md5(in_str, salt=None):
    in_str = '~*&^%$#@!)(-+' + in_str + '~*&^%$#@!)(-+'
    if salt:
        in_str += salt
    m = hashlib.md5()
    m.update(in_str.encode('utf-8'))
    return m.hexdigest()
