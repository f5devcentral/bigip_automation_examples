from datetime import datetime

class FilterModule(object):
    def filters(self):
        return {
            'make_filename_unique': self.make_filename_unique
        }

    def make_filename_unique(self, filename):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        if ext:
            new_filename = f"{name}_{current_datetime}.{ext}"
        else:
            new_filename = f"{name}_{current_datetime}"
    
        return new_filename
