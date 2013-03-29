# supported servers
_servers = ('cao', 'cdo', 'cszo')
# supported versions
_versions = ('0.10', '0.11', 'trunk')

# static portion of url
_base_urls = {
    'cao': 'http://crawl.akrasiac.org/rcfiles',
    'cdo': 'http://crawl.develz.org/configs',
    'cszo': 'http://dobrazupa.org/rcfiles',
}

# cao and cszo use the same directory structure
_cao_pathnames = [''.join(['crawl-', v]) for v in ('0.10', '0.11', 'git')]

# dicts that return the proper path for each version
_paths = {
    'cao': dict(zip(_versions, _cao_pathnames)),
    'cdo': dict(zip(_versions, _versions)),
    'cszo': dict(zip(_versions, _cao_pathnames)),
}


class Server(object):
    _versions = _versions
    _servers = _servers
    _base_urls = _base_urls
    _paths = _paths
    def __init__(self, server):
        assert server in self._servers
        self._base = self._base_urls[server]
        self._paths = self._paths[server]

    def _path(self, version):
        return '/'.join([self._base, self._paths[version]])

    def rcfile(self, name, version='trunk'):
        assert version in self._versions
        # use index number for 2.6 compatibility
        path = self._path(version)
        fname = '{0}.rc'.format(name)
        return '/'.join([path, fname])


servers = {'cao': Server('cao'),
           'cdo': Server('cdo'),
           'cszo': Server('cszo')}

versions = _versions
