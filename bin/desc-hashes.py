#!/usr/bin/env python
"""
" @author VaL
" @copyright Copyright (C) 2013 VaL::bOK
" @license GNU GPL v2
"""

"""
" Extractes descriptor hashes from an image
"""
import sys
import os
parentdir = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
os.sys.path.insert( 0, parentdir )

import json
from core import *

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        sys.exit( 1 )

    fn = sys.argv[1]
    img = Image.read( fn )
    cv = cv2.SURF( 400 )
    kp,desc = cv.detectAndCompute( img.img, None )
    e = Extractor( img, kp, desc )
    imgs = e.descImages( False )
    result = {'DHash': {}}
    matcher = Matcher( [DHash] )
    hashes = matcher.hashes( imgs )[DHash]
    phs = {}
    for h in hashes:
        phs[str( h )] = h.dict()

    result['DHash'] = phs
    print json.dumps( result )
