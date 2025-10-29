def write(fn: str, content: str, **kwargs):
    kwargs.setdefault('mode', 'w')
    kwargs.setdefault('encoding', 'utf-8')
    kwargs.setdefault('newline', '\n')
    kwargs.setdefault('errors', 'strict')
    kwargs.setdefault('buffering', 1)
    with open(fn, **kwargs) as f:
        f.write(content)
        
def read(fn: str, **kwargs):
    kwargs.setdefault('mode', 'r')
    kwargs.setdefault('encoding', 'utf-8')
    kwargs.setdefault('newline', '\n')
    kwargs.setdefault('errors', 'strict')
    kwargs.setdefault('buffering', 1)
    with open(fn, **kwargs) as f:
        return f.read()