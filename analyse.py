


def get_application(*, redis, user, password):
    def application(environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
    
        with r.pipeline() as pipe
            if environ["PATH_INFO"] == "/unique":
                pipe.zadd("analytics_unique", date.today())

            if environ["PATH_INFO"] == "/hit":
                referer = environ.get("HTTP_REFERER")
                pipe.zadd("analytics_referer", environ[referer])
                pipe.zadd("analytics_paths", environ["PATH"])
            pipe.execute()
    
    
    
        body = 'hello, world'.encode('utf-8')
        start_response(status, headers)
        return [body]
