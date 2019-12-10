import redis
try:
    from datadog_checks.base import AgentCheck
except ImportError:
    from checks import AgentCheck

__version__ = "1.0.0"

class QueueCheck(AgentCheck):
    def check(self, instance):
        host = instance.get('host', '')
        port = instance.get('port', '')
        password = instance.get('password', '')
        queues = instance.get('queues', [])
        tags = instance.get('tags', [])

        r = redis.Redis(host=host,port=port,password=password, db=0)
        for q in queues:
            q_len = r.llen(q)
            self.gauge("redis.%s" % q, q_len, tags=tags)
