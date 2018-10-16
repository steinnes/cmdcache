import os
import re
import sh
import sys
import time


MAX_AGE = int(os.environ.get('CMDCACHE_MAX_AGE', 10))  # default to 10 seconds


def _cache_key(cmds):
    disallowed_chars = re.compile("[^a-zA-Z0-9]+")
    return "{}/{}.{}.cmdcache".format(
        os.environ.get('CMDCACHE_DIR', '/tmp'),
        os.environ.get('CMDCACHE_PREFIX', 'default'),
        disallowed_chars.sub("", cmds)[:80])


def _is_fresh(key):
    try:
        stat = os.stat(key)
        if (time.time() - stat.st_mtime) < MAX_AGE:
            return True
    except OSError:
        pass

    return False


def _load(key):
    if _is_fresh(key):
        try:
            with open(key) as fp:
                return fp.read()
        except IOError:
            pass
    return None


def _store(key, res):
    if sys.version_info[0] == 2:
        buf = unicode(res).decode('utf-8')
    else:
        buf = str(res)

    with open(key, 'w') as fp:
        fp.write(buf)
    return buf


def get_cached(cmds):
    cmds = cmds
    key = _cache_key("".join(cmds))
    stored = _load(key)

    if stored is None:
        cmd = getattr(sh, cmds[0])
        if cmds[1:]:
            res = cmd(cmds[1:])
        else:
            res = cmd()
        return _store(key, res)
    return stored


def main():
    if len(sys.argv) < 2:
        print("Usage: {} <normal command here>".format(os.path.basename(sys.argv[0])))
        print("")
        print("Control behaviour with env vars:")
        print("")
        print("CMDCACHE_MAX_AGE (age in seconds)")
        print("CMDCACHE_PREFIX (defaults to /tmp/cmdcache.)")
        sys.exit(1)
    sys.stdout.write(get_cached(sys.argv[1:]))


if __name__ == "__main__":
    main()

