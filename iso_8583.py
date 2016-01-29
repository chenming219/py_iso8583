#! /usr/bin/env python
# -*- coding: utf-8 -*

import cfg_8583
import deal_8583
import hexdump

class iso_8583:
    __8583_cfg=None
    __8583_str=""
    __8583_dic={}
    offset = 0
    bitmap = None
    __bitmap_list = []
    
    __deal_content_type_funcs=None
    __deal_len_type_funcs=None
    
    def __init__(self, iso_conf = None,iso_str = None):
        
        #tips:iso_conf为空，或者配置错误，劳资都是木有办法玩的。
        assert iso_conf != None,"iso_conf can not None"
        assert len(cfg_8583.ContentTypes) > 0 , "cfg_8583 err "  
        assert cfg_8583.ContentTypes.has_key(iso_conf),"iso_conf not in cfg_8583"  
            
        if iso_str != None:
            #unpack
            self.__8583_str = iso_str
            self.__8583_cfg = cfg_8583.ContentTypes[iso_conf]
            self.__deal_content_type_funcs=deal_8583.deal_content_type("unpack")
            self.__deal_len_type_funcs=deal_8583.deal_len_type("unpack")
        else:
            #pack
            self.__8583_cfg = cfg_8583.ContentTypes[iso_conf]
            
    def _get_info(self,domain):
        cfg_domain=self.__8583_cfg[domain]
        
        len_func=cfg_domain["len_type"]
        content_type_func=cfg_domain["content_type"]
        
        info={}
        info["len"],offset_len=getattr(self.__deal_len_type_funcs, len_func)(cfg_domain,self.__8583_str,self.offset)  
        self.offset += offset_len
        
        info["val"],offset_data=getattr(self.__deal_content_type_funcs, content_type_func)(self.__8583_str,info["len"],self.offset)  
        self.offset += offset_data
        
        return (domain,info)
    
    def _gen_bitmap_list(self):
        self.__bitmap_list = []
        index=1
        for x in self.bitmap:
            b="%4s" % bin(int(x,16))[2:]
            j=0
            for y in b:
                if y == '1':
                    self.__bitmap_list.append(index+j)
                j+=1
             
            index+=4
    
    def unpack(self):
        for domain in range(-6,0):
            if self.__8583_cfg.has_key(domain):
                #print domain,self.__8583_cfg[domain]
                t, v = self._get_info(domain)
                self.__8583_dic[t] = v
            
        self.bitmap = self.__8583_dic[-2]["val"]
        self._gen_bitmap_list()
        print "get bitmap list succ %s" % self.__bitmap_list
        
        for domain in self.__bitmap_list:
            if self.__8583_cfg.has_key(domain):
                #print domain,self.__8583_cfg[domain]
                t, v = self._get_info(domain)
                self.__8583_dic[t] = v
        
        
        return self.__8583_dic
            
    def ISO8583_testOutput(self):  
        for d in range(-6,128):
            if self.__8583_dic.has_key(d):
                print "[%s] [%08s] [%06s] [%03s] : %s" % \
                (
                 d,
                 self.__8583_cfg[d]["content_type"],
                 self.__8583_cfg[d]["len_type"],
                 self.__8583_dic[d]["len"],
                 self.__8583_dic[d]["val"]
                 )
            