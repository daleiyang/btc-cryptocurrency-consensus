from bitcoin.rpc import RawProxy
p = RawProxy()
info = p.getblockchaininfo()
print(info)
#print(info['blocks'])

