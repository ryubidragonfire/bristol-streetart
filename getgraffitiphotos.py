# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:05:03 2016

@author: chyam
"""

import flickr_api
from flickr_api.api import flickr

def main():
    # credentials to access flickr api
    initialise()
    photos_xml = flickr.photos.search(tags='street art', lat=51.452705, lon=-2.595146, radius=1, radius_units='km', extras='geo, url_l')
    photos_json = xmltojson(photos_xml)
    
    photo = photos_json['rsp']['photos']['photo']

    print photo[0]    


    #geo = flickr.photos.geo.getLocation(photo_id='28007228350')
    #print geo
    
    #test_xmltojson()

    return

def xmltojson(xml_string, xml_attribs=True):
    import json
    import xmltodict
    d = xmltodict.parse(xml_string, xml_attribs=xml_attribs)
    return json.loads(json.dumps(d, indent=4))
        
## deprecated
#def test_xmltojson():
#    data = xmltojson('./test.xml')
#    names = data['employees']['person']
#    for n in names:
#        print n
#    return
    
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
    