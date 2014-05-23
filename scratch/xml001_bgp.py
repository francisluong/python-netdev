#!/usr/bin/env python


from lxml import etree
parser = etree.XMLParser(remove_blank_text=True)
xslt_lit = etree.parse('remove_namespaces.xslt', parser)
transform = etree.XSLT(xslt_lit)
filepath = 'zz.bgp-information.xml'
bgp_rpc = etree.parse(filepath)
bgp_rpc = transform(bgp_rpc)
bgp_peers = bgp_rpc.xpath('//bgp-peer')
for peer in bgp_peers:
    #print etree.tostring(peer, pretty_print=True)
    address = peer.xpath('peer-address')[0].text
    asn = peer.xpath('peer-as')[0].text
    state = peer.xpath('peer-state')[0].text
    print "Peer {}, AS: {}, State: {}".format(address,asn,state)
