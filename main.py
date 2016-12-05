#encoding: utf-8
from collections import namedtuple
from PIL import Image, ImageDraw, ImageFont
import os.path

# label setting for 20
Label = namedtuple('Label', ['name', 'jp', 'id','trainId','category','categoryId','hasInstances','ignoreInEval','color'])

font_path = '/System/Library/Fonts/ヒラギノ角ゴ ProN W3.otf'

labellist = [
    #       name                          id    trainId   category            catId     hasInstances   ignoreInEval   color
    Label(  'road'                 , u'道路',  7 ,        0 , 'flat'            , 1       , False        , False        , (128, 64,128) ),
    Label(  'sidewalk'             , u'歩道',  8 ,        1 , 'flat'            , 1       , False        , False        , (244, 35,232) ),
    Label(  'building'             , u'建物',  11 ,        2 , 'construction'    , 2       , False        , False        , ( 70, 70, 70) ),
    Label(  'guard rail'           , u'ガードレール',  14 ,        3 , 'construction'    , 2       , False        , True         , (180,165,180) ),
    Label(  'fence'                , u'フェンス',  13 ,        4 , 'construction'    , 2       , False        , False        , (190,153,153) ),
    Label(  'pole'                 , u'ポール',  17 ,        5 , 'object'          , 3       , False        , False        , (153,153,153) ),
    Label(  'traffic light'        , u'信号',  19 ,        6 , 'object'          , 3       , False        , False        , (250,170, 30) ),
    Label(  'traffic sign'         , u'標識',  20 ,        7 , 'object'          , 3       , False        , False        , (220,220,  0) ),
    Label(  'vegetation'           , u'草や木など',  21 ,        8 , 'nature'          , 4       , False        , False        , (107,142, 35) ),
    Label(  'terrain'              , u'自然な地面',  22 ,        9 , 'nature'          , 4       , False        , False        , (152,251,152) ),
    Label(  'sky'                  , u'空',  23 ,       10 , 'sky'             , 5       , False        , False        , ( 70,130,180) ),
    Label(  'person'               , u'人',  24 ,       11 , 'human'           , 6       , True         , False        , (220, 20, 60) ),
    Label(  'unlabeled'            , u'ラベル無し',   0 ,       12 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    Label(  'car'                  , u'車',  26 ,       13 , 'vehicle'         , 7       , True         , False        , (  0,  0,142) ),
    Label(  'truck'                , u'トラック',  27 ,       14 , 'vehicle'         , 7       , True         , False        , (  0,  0, 70) ),
    Label(  'bus'                  , u'バス',  28 ,       15 , 'vehicle'         , 7       , True         , False        , (  0, 60,100) ),
    Label(  'train'                , u'電車',  31 ,       16 , 'vehicle'         , 7       , True         , False        , (  0, 80,100) ),
    Label(  'motorcycle'           , u'バイク',  32 ,       17 , 'vehicle'         , 7       , True         , False        , (  0,  0,230) ),
    Label(  'bicycle'              , u'自転車',  33 ,       18 , 'vehicle'         , 7       , True         , False        , (119, 11, 32) ),
    Label(  'lanemkgsdriv'         , u'白線',  34 ,       19 , 'flat'            , 1       , False        , True         , (128,  0,192) ),
]

def main():
    print("class number: %d" % len(labellist))
    font = ImageFont.truetype(font_path, 20, encoding='UTF-8')

    img = Image.new("RGB", (800, 150), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for l in xrange(len(labellist)):
        raw = l / 4
        colum = l % 4
        color = labellist[l].color
        name = labellist[l].jp

        print raw
        print colum
        print color
        print "="*10

        draw.polygon((800 - 200*(colum+1), 30*raw) + (800 - 200*(colum), 30*raw) + (800 - 200*(colum), 30*(raw+1)) + (800 - 200*(colum+1), 30*(raw+1)),
                     fill=color, outline=color)
        draw.text((800 - 200*(colum+1) + 5, 30*raw + 5), name, font=font, fill=(255, 255, 255))


    output_dir = "output"
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    seg_name = "%s/%s_seg.png" % (output_dir, "color")
    img.save(seg_name)




if __name__ == '__main__':
    main()