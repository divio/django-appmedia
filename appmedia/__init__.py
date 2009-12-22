VERSION = (1, 0, 0, 'final')
if VERSION[-1] != "final":
    __version__ = '.'.join(map(str, VERSION))
else:
    __version__ = '.'.join(map(str, VERSION[:-1]))
