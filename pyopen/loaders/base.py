
class BaseLoader(object):
    extensions = None

    @classmethod
    def matches(cls, filename):
        assert cls.extensions is not None, (
            "Class %s must define matches() or extensions list" % cls)
        return any(filename.endswith(x) for x in cls.extensions)