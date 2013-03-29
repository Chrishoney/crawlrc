# rcfile

## a tool for dcss rcfiles

Right now, this works. It is rough, but it works. If you want to test this out,
grab the code, and symlink the rcfile executable script to a location on your
PATH. If you want to test out the pexpect auto upload, check out dglexpect.py.
It will be added to the command-line interface soon.

Set the following environment variables to configure rcfile:

These set the default crawl account and server for downloading rcfiles:

`RCFILE_NAME`=default account

`RCFILE_SERVER`=default server

These only need to be set if you want to mess around with pexpect

`DGL_USER`=crawl account

`DGL_SERVER`=crawl server

`DGL_PASS`=crawl password

`DGL_KEY`=path to universal crawl key

One of the first things I will do is unify these environment variables and add
in an optional config file as an alternate to setting environment variables.
