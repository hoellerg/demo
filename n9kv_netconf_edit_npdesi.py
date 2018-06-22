#!/usr/bin/env python3

from ncclient import manager
import credentials
import json
from lxml import etree
from ncclient.operations.rpc import RPCError


def main():
    with manager.connect(host='172.16.1.11',
                         port=830,
                         username=credentials.user,
                         password=credentials.password,
                         hostkey_verify=False,
                         device_params={'name': 'nexus'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as cisco_manager:

        descr_cfg = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <interfaces xmlns="http://openconfig.net/yang/interfaces">
              <interface>
                  <name>eth1/33</name>
                  <config>
                      <type>ianaift:ethernetCsmacd</type>
                      <description>Guten morgen wuenscht NETCONF</description>
                      <enabled>true</enabled>
                      <name>eth1/33</name>
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
        '''

        bgp_cfg = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <bgp xmlns="http://openconfig.net/yang/bgp">
            <global>
              <config>
                <as>55</as>
                <router-id>7.7.7.7</router-id>
              </config>
            </global>
          </bgp>
        </config>
        '''

        bgp_cfg_reset = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <bgp xmlns="http://openconfig.net/yang/bgp">
          </bgp>
        </config>
        '''
        '''
        <bgp xmlns="http://openconfig.net/yang/bgp">
            <global>
                <config>
                    <as>50</as>
                    <router-id>1.2.3.4</router-id>
                </config>
            </global>
        </bgp>
    '''

        lcl_rt_cfg = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <local-routes xmlns="http://openconfig.net/yang/local-routing">
                <static-routes>
                    <static>
                        <config>
                            <set-tag>0</set-tag>
                            <prefix>11.0.0.0/8</prefix>
                        </config>
                        <next-hops>
                            <next-hop>
                                <config>
                                    <index>null0+DROP+default</index>
                                    <metric>0</metric>
                                    <next-hop>DROP</next-hop>
                                </config>
                                <index>null0+DROP+default</index>
                                <interface-ref xmlns="http://openconfig.net/yang/interfaces">
                                    <config>
                                        <interface>null0</interface>
                                    </config>
                                </interface-ref>
                            </next-hop>
                        </next-hops>
                        <prefix>11.0.0.0/8</prefix>
                    </static>
                </static-routes>
            </local-routes>
        </config>
        '''

        try:
            resp = cisco_manager.edit_config(bgp_cfg, target='running',
                                             default_operation='replace')
            print(resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                if not attr.startswith('__'):
                    print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()
