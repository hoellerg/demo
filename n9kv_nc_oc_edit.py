#!/usr/bin/env python3
'''
ncclient support for Netconf edit-config opereation on nxos-7.0-3-I7-2.
'''

import credentials
from lxml import etree

# Supportet IANA interface types
IFTYPES = {'vlan': 'ianaift:l2vlan',            # VLAN
           'pc': 'ianaift:ieee8023adLag',       # Port Channel
           'eth': 'ianaift:ethernetCsmacd'}     # Any Ethernet


n9kv1 = dict(host='172.16.1.81',
             port=830,
             username=credentials.user,
             password=credentials.password,
             hostkey_verify=False,
             device_params={'name': 'nexus'},
             allow_agent=False,
             look_for_keys=False)


openconfig_interfaces_cfg = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name/>
      <config>
        <type/>
        <mtu/>
        <name/>
        <description/>
      </config>
      <hold-time>
        <config/>
      </hold-time>
      <subinterfaces>
        <subinterface>
          <index/>
          <config>
            <name/>
            <description/>
          </config>
        </subinterface>
      </subinterfaces>
    </interface>
  </interfaces>
</config>
'''

# Genereted via pyang -f sample-xml-skeleton \
# --sample-xml-skeleton-doctype=config openconfig-interfaces.yang
# Valid Example:
"""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
      <interface>
          <name>eth1/30</name>
          <config>
              <type>ianaift:ethernetCsmacd</type>
              <description>Guten morgen wuenscht NETCONF</description>
              <enabled>true</enabled>
              <name>eth1/30</name>
              <mtu>1500</mtu>
          </config>
          <hold-time>
              <config>
                  <up>100</up>
              </config>
          </hold-time>
      </interface>
  </interfaces>
</config>
"""
openconfig_bgp_cfg = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <bgp xmlns="http://openconfig.net/yang/bgp">
    <global>
      <config>
        <as/>
        <router-id/>
      </config>
    </global>
  <bgp>
</config>
'''

root = etree.fromstring(openconfig_interfaces_cfg)
for element in root:
    print(element)


def generate_int_cfg(name, **inputs):
    pass
