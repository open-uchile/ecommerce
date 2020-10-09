from .production import *

# Change syslog-based loggers which don't work inside docker containers
LOGGING['handlers']['local'] = {'class': 'logging.NullHandler'}

""" 
LOGGING['formatters']['json'] = {
    '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
}

LOGGING['handlers']['json'] = {
    'level': 'INFO',
    'class': 'logging.StreamHandler',
    'formatter': 'json',
}

LOGGING['loggers']['']['handlers'] = ['json']
 """#LOGGING['handlers']['local'] = {'class': 'logging.StreamHandler'}
""" 
PAYMENT_PROCESSORS = (
    'ecommerce.extensions.payment.processors.webpay.Webpay',
)

# Enable themes
ENABLE_COMPREHENSIVE_THEMING = True
 """

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

DEBUG=False