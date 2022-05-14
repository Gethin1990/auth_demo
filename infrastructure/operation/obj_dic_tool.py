class objDicTool:
    @staticmethod
    def to_obj(obj:object,**data):
        obj.__dict__.update(data)