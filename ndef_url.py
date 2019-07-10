import nfc
import ndef
from threading import Thread

def beam(llc):
    snep_client=nfc.snep.SnepClient(llc)
    snep_client.put_records([ndef.UriRecord("https://google.com")])

def connected(llc):
    Thread(target=beam, args=(llc,)).start()
    return True


clf=nfc.ContactlessFrontend()
assert clf.open('ttyS0') is True
clf.connect(llcp={'on-connect':connected})


