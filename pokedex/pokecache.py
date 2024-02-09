import threading
import time
from datetime import datetime, timedelta
import functools
from functools import partial


class CacheEntry:
    def __init__(self, val, created_at):
        self.val = val
        self.created_at = created_at

class Cache:
    def __init__(self, interval):
        self.cache = {}
        self.mux = threading.Lock()
        self.interval = interval
        self.start_reap_loop()

    def add(self, key, val):
        with self.mux:
            self.cache[key] = CacheEntry(val, datetime.utcnow())

    def get(self, key):
        with self.mux:
            cache_entry = self.cache.get(key)
            if cache_entry is None:
                return None, False
            else:
                return cache_entry.val, True

    def start_reap_loop(self):
        reap_loop = partial(self.reap_loop)
        threading.Thread(target=reap_loop, daemon=True).start()

    def reap_loop(self):
        while True:
            time.sleep(self.interval.total_seconds())
            self.reap()

    def reap(self):
        with self.mux:
            time_past = datetime.utcnow() - timedelta(seconds=self.interval)
            keys_to_delete = [k for k, v in self.cache.items() if v.created_at < time_past]
            for key in keys_to_delete:
                del self.cache[key]
