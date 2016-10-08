# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:05:03 2016

@author: chyam
"""

import flickr_api
from flickr_api.api import flickr
import json

def main():
    # credentials to access flickr api
    initialise()
    photos_xml = flickr.photos.search(tags='street art', lat=51.452705, lon=-2.595146, radius=0.6, radius_units='km', extras='geo, url_l')
    photos_json = xmltojson(photos_xml)
    
    photo = photos_json['rsp']['photos']['photo']

    d={}
    dlist=[]

    for p in photo:
        d['id'] = p['@id']
        d['lon'] = p['@longitude']
        d['lat'] = p['@latitude']
        d['url'] = p['@url_l']
        dlist.append(d.copy())
             
        
    #dlist_json = json.dumps(dlist)

    with open('./photos_list.json', 'w') as f:
        json.dump(dlist, f, sort_keys = True)

        
    return

def xmltojson(xml_string, xml_attribs=True):
    import json
    import xmltodict
    d = xmltodict.parse(xml_string, xml_attribs=xml_attribs)
    return json.loads(json.dumps(d, indent=4))
    
def initialise():
    from ConfigParser import SafeConfigParser
    parser = SafeConfigParser()
    parser.read('config.ini')
    API_KEY = parser.get('credential', 'API_KEY');
    API_SECRET = parser.get('credential', 'API_SECRET')
    flickr_api.set_keys(api_key = API_KEY, api_secret = API_SECRET )
    return
    
if __name__ == '__main__':
    main()
    