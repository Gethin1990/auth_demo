# encoding: utf-8
"""
基于单例模式实现具有时效性的内存缓存
"""
import threading
import uuid


class DataCache(object):
    """
    _cache 的数据结构如下所示：
    _cache:{
        "cache_id_1":{
            "value":"cache_value",
            "expired":"60s",
            "timer":"定时清理器实例",
        }
    }
    """

    # 默认 expired = 2*60*60s
    EXPIRED = 2 * 60 * 60

    # 添加线程锁，保证多线程安全
    __instance_lock = threading.Lock()

    # 初始化dict(）用来缓存数据
    __CACHE = dict()

    def __init__(self):
        self.__cache = DataCache.__CACHE

    def __new__(cls, *args, **kwargs):

        if not hasattr(DataCache, "_instance"):
            with DataCache.__instance_lock:
                if not hasattr(DataCache, "_instance"):
                    DataCache._instance = object.__new__(cls)
        return DataCache._instance

    def set(self, value, cache_id=None, expired=EXPIRED):
        """
        保存缓存
        :param value: 缓存数据
        :param cache_id: cache_id 默认值：None
        :param expired: 过期时间 默认值：EXPIRED
        :return: cache_id
        """
        if cache_id is None or cache_id == "":
            cache_id = str(uuid.uuid4())

        self._set_cache(value, cache_id, expired)

        return cache_id

    def delete(self, cache_id):
        """
        删除缓存
        :param cache_id: 缓存ID
        :return: None
        """
        self._clean_cache(cache_id)

    def get(self, cache_id):
        """
        获取缓存
        :param cache_id:缓存ID
        :return:
        """
        if self.__cache.has_key(cache_id):
            return self.__cache[cache_id]['value']
        else:
            return None

    def values(self):
        """
        获取所有值
        :return: {
        “cache_id_1”:"value1",
        “cache_id_2”:"value2"
        }
        """
        return {key: item['value'] for key, item in self.__cache.items()}

    def clear(self):
        """
        清空缓存
        :return: None
        """
        for cache_id in self.__cache.keys():
            self._clean_cache(cache_id)

    def _set_cache(self, value, cache_id, expired):
        # 删除缓存
        self._clean_cache(cache_id)
        # 设置时效监控线程
        timer = threading.Timer(expired, self._clean_cache, [cache_id])
        timer.start()
        self.__cache[cache_id] = {
            'timer': timer,
            'value': value
        }

    def _clean_cache(self, cache_id):
        if self.__cache.has_key(cache_id):
            timer = self.__cache[cache_id]['timer']
            timer.cancel()
            self.__cache.pop(cache_id)

