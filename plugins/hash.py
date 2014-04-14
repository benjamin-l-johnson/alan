from time import sleep
import hashlib
import irc.util
"""Module for hashing algorithms"""
event = "PRIVMSG"

def call(ircmessage, con):
    nick, channel, params = irc.util.parseprivmsg(ircmessage, con.nick)

    if len(params) == 1:
        return

    if not params[0] in ["sha1", "md5", "sha256", "sha512"]:
        return

    con.privmsg(channel, hash(" ".join(params[1:]), params[0]))


def hash(string, hashtype='sha1', blocksize=65536):
    hasher = hashlib.new(hashtype)
    buf = string.encode()
    if len(buf) > 0:
        hasher.update(buf)

    return hasher.hexdigest()