import os
import sys
import optparse
from urllib2 import urlopen, Request, HTTPError
from crawl import servers, versions
from utils import clip

USER_AGENT = 'rcfile - a crawl rcfile tool. python urllib2'

def get_parser():
    usage = "usage: %prog [-c | -u] [-v version] name server"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-v", "--version", dest="version", default="trunk",
                      help="Specify crawl version.")
    parser.add_option("-u", "--url", action="store_true", dest="url",
                      help="Output url to stdout")
    parser.add_option("-c", "--copy", action="store_true", dest="copy",
                      help="Copy url to clipboard")
    return parser

def main():
    parser = get_parser()
    options, args = parser.parse_args()
    default_name = os.environ.get('RCFILE_NAME')
    default_server = os.environ.get('RCFILE_SERVER')

    if len(args) == 0:
        if default_name and default_server:
            name, server = default_name, default_server
        else:
            parser.error('Missing parameters')
               
    elif len(args) == 1:
        arg = args[0]
        if arg in servers.keys():
            if default_name:
                name, server = default_name, arg
            else:
                parser.error('No name specified')
        elif arg not in servers.keys():
            if default_server:
                name, server = arg, default_server
            else:
                parser.error('No server specified')

    elif len(args) == 2:
        name, server = args

    else:
        parser.error("Incorrect arguments")

    if server not in servers.keys():
        parser.error("Invalid server.")

    version = options.version
    if version not in versions:
        parser.error("Invalid crawl version.")

    url = servers[server].rcfile(name, version)

    if options.copy or options.url:
        if options.copy:
            clip(url)
        if options.url:
            sys.stdout.write(url + '\n')
            sys.exit()
           
    else:
        request = Request(url)
        request.add_header('User-agent', USER_AGENT)

        try:
            response = urlopen(request)
        except HTTPError, e:
            sys.exit('{0} {1}'.format(e.code, e.reason))
                
        for line in response.read():
            sys.stdout.write(line)

if __name__ == '__main__':
    main()
