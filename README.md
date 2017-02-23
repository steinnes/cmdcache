# cmdcache

Simple utility to cache the output of the given commands.  This springs from
writing bash completion scripts which rely on custom cli tools which retrieve
data from the cloud, causing every single tab-completion to result in a 800ms
or more delay, rendering the completion unusable.

## Setup

The easiest way to setup `cmdcache` is to use pip:

    $ pip install cmdcache

## Usage

Just prepend `cmdcache` before any shell commands in your shellscripts where you
expect to use the stdout, and are *OK* with it being cached.  Export the relevant
`CMDCACHE_*` vars (see Caching section below) to control behavior.

## Caching

### Keys

`cmdcache` constructs a key from the given command, stripping out all non
alphanumeric characters, then constructing a key with the following format:

`$CMDCACHE_DIR/$CMDCACHE_PREFIX.{key}.cmdcache`

The environment variable `CMDCACHE_DIR` defaults to `/tmp` and `CMDCACHE_PREFIX`
defaults to `default`.

### Storage

The cached output is stored in a file with the given key, and if its modification
time is less than `$CMDCACHE_MAX_AGE` `cmdcache` will return the output of the file
instead of running the command.

The environment variable `CMDCACHE_MAX_AGE` defaults to `10`, which means 10 seconds.


## Example

```
ses: ~ $ time cmdcache curl http://static.steinn.org/config.sample
THIS=is
A=sample
FILE=with
SOME=data

real	0m0.357s
user	0m0.066s
sys	0m0.048s

ses: ~ $ ls -ltr /tmp/|tail -1
-rw-r--r--  1 ses   wheel       37 Feb 23 13:16 default.curlhttpstaticsteinnorgconfigsample.cmdcache
```

If immediately re-run, the command is noticeably faster:

```
ses: ~ $ time cmdcache curl http://static.steinn.org/config.sample
THIS=is
A=sample
FILE=with
SOME=data

real	0m0.067s
user	0m0.042s
sys	0m0.021s
```


## Thanks

Thanks to @ninjaaron for making https://github.com/ninjaaron/fast-entry_points
without which this script would not be so useful when installed via `pip`.
