# Scrapy settings for map_data project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'map_data'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['map_data.spiders']
NEWSPIDER_MODULE = 'map_data.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

