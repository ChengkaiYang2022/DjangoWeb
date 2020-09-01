# coding:utf-8


def simple_app(environ, start_response):
    """web应用"""
    status = '200 OK'
    response_heads = [('Content-type', 'text/plain')]
    start_response(status, response_heads)
    return [b'Hello world!\n']
