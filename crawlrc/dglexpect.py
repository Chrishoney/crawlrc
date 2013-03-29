import os
import sys
import pexpect

USERNAME = os.environ.get('DGL_USER')
PASSWORD = os.environ.get('DGL_PASS')
SSH_KEY = os.environ.get('DGL_KEY')
SSH_USER = 'crawl'
SSH_SERVERS ={'cao': 'crawl.akrasiac.org',
              'cdo': 'crawl.develz.org',
              'cszo': 'crawl.s-z.org',}

ESCAPE = chr(27)
PROMPT = '=>'
VIRUS_EXPECT = '"/dgldir'

CMD_LOGIN = 'l'
CMD_TRUNK = 't'
CMD_VIRUS = 'O'
CMD_VI_INPUT = 'i'
CMD_VI_WIPE = ':%d'
CMD_VI_SAVE = ':wq'
CMD_QUIT = 'q'

def expect(rcfile, server, key=SSH_KEY):
    # spawn child process
    server = SSH_SERVERS[server]
    cmd = 'ssh -Ci {0} {1}@{2}'.format(key, SSH_USER, server)
    child = pexpect.spawn(cmd)
    # login
    child.expect(PROMPT)
    child.send(CMD_LOGIN)
    child.expect(PROMPT)
    child.sendline(USERNAME)
    child.expect(PROMPT)
    child.sendline(PASSWORD)
    # select trunk
    child.expect(PROMPT)
    child.send(CMD_TRUNK)
    # virus works the best here
    child.expect(PROMPT)
    child.send(CMD_VIRUS)
    # wipe the file
    child.expect(VIRUS_EXPECT)
    child.sendline(CMD_VI_WIPE)
    ## enter insert mode and send a line at a time to dgl
    child.send(CMD_VI_INPUT)
    for line in rcfile:
        child.sendline(line)
    # back to normal mode, then save
    child.send(ESCAPE)
    child.sendline(CMD_VI_SAVE)
    # quit out of trunk menu, then main menu
    child.send(CMD_QUIT)
    child.send(CMD_QUIT)
    print "finished"
    child.close()

if __name__ == '__main__':
    if os.environ.get('DGL_SERVER'):
        server = os.environ.get('DGL_SERVER')
    else:
        server = 'cszo'
    rc_path = sys.argv[1]
    with open(rc_path) as f:
        rcfile = [line.strip() for line in f]
    expect(rcfile, server)
