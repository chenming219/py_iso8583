#! /usr/bin/env python
# -*- coding: utf-8 -*

import cfg_8583

class iso_8583:
    __8583_str=""
    __8583_cfg=None
    def __init__(self, iso_conf = None,iso_str = None):
        
        #tips:iso_conf为空，或者配置错误，劳资都是木有办法玩的。
        assert iso_conf != None,"iso_conf can not None"
        assert len(cfg_8583.ContentTypes) > 0 , "cfg_8583 err "  
        assert cfg_8583.ContentTypes.has_key(iso_conf),"iso_conf not in cfg_8583"  
            
        if iso_str != None:
            #unpack
            self.__8583_str = iso_str
            __8583_cfg = cfg_8583.ContentTypes[iso_conf]
        else:
            #pack
            __8583_cfg = cfg_8583.ContentTypes[iso_conf]