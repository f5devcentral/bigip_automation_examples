# filter_plugins/custom_filters.py

from datetime import datetime

class FilterModule(object):
    def filters(self):
        return {
            'get_date_time': self.get_date_time
        }

    def get_date_time(self, ignore):
        return datetime.now().isoformat()
