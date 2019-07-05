import logging
from logging.config import dictConfig
import os

import bottle
from bottle import request, response
from bottle import get
from logdna import LogDNAHandler

app = application = bottle.default_app()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] <%(asctime)s> %(pathname)s %(module)s.%(funcName)s[%(lineno)d] :: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logdna': {
            'level': 'DEBUG',
            'class': 'logging.handlers.LogDNAHandler',
            'key': os.environ.get('KEY'),
            'options': {
                'app': 'ansible-manifold-demo',
            },
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logdna'],
            'level': 'DEBUG'
        }
    }
}

dictConfig(LOGGING)

logger = logging.getLogger()


@get('/health')
def health_handler():
    response.status = 204
    logger.info("health check")
    return

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port = 8000)
