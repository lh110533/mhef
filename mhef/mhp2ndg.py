DATA_ENCODE_TABLE = b'\xc0\xa8\xca\x07KnHo\xd6\x921,\x9d\xfb\xe1Pa\xc6\xe4R>\x12\xad3\xae\xeb\xf3/ki{S\x96\xc4\xb1\x9c\x1c\xc5 \x86\x19\x13\xe9j&ux\x8cC\xedzf]\x18\x1d\xe8p\xa5^\xf2_X\x05F\r\x97\x9e|\xeae\xdd$\x8fIB\xaf\xf4%\xb8+\x08r\x17\xd9\xa4\xd3\x93q[@\xb2.\x0b~L\x04\xf7\x11\xc17y\xa7)\xbc\x1bV\x8b\xfa\x8d6;m\xd4W\x83\xbd\x1f\xd7b\x84\xf5\xda\xd5\xab\xcc\xa2G\x88\x9a-\xc7\xdf\xcb\x02(A\xa9=\xd8\xa1#<\x81l\\\xd0h\xc9\xbf\x99\x01\xbe\xf9\xfc\xec\xb7\n\x82\x89\xdc\x91\xef\x14\xcf4J\x03\xd1\xba5\x8a\x06\xff8\xa0\xf0\xce}\x0cv\xc2\xb3\xac\t\x94UT\x80\xa3\x95\xbb\xa60*\xf6g\x1e\xfewcd\x87`\x00\xb0\x98D\xeeM\xe5\xc3\xcdQ"s\x9b\xe0\x1at\xc8Z?N\xe6\xaa\x7f!\xf1Y\x9f\xb9\x90O\xe2\xfd\xb4\x16\xe3\xf8\x0e\xe7\x15\x859:\xde\x0f\xd2\xb6\x8e\'\xdb\xb52E\x10'
DATA_DECODE_TABLE = b'\xcb\x96\x85\xa6_>\xab\x03P\xb7\x9c\\\xb2@\xef\xf6\xffa\x15)\xa2\xf1\xecR5(\xd9h$6\xc4t&\xe2\xd5\x8cGM,\xfa\x86f\xc1O\x0b\x81[\x1b\xc0\n\xfd\x17\xa4\xa9mc\xad\xf3\xf4n\x8d\x89\x14\xddY\x87J0\xce\xfe?~\x06I\xa5\x04^\xd0\xde\xe8\x0f\xd4\x13\x1f\xba\xb9iq=\xe4\xdcX\x904:<\xca\x10v\xc7\xc8E3\xc3\x92\x1d+\x1c\x8fo\x05\x078WQ\xd6\xda-\xb3\xc6.d2\x1eC\xb1]\xe1\xbb\x8e\x9drw\xf2\'\xc9\x7f\x9e\xaaj/l\xf9H\xe7\xa0\tV\xb8\xbd A\xcd\x95\x80\xd7#\x0cB\xe5\xae\x8b}\xbcT9\xbfe\x01\x88\xe0{\xb6\x16\x18K\xcc"Z\xb5\xeb\xfc\xf8\x9bN\xe6\xa8\xbegs\x97\x94\x00b\xb4\xd2!%\x11\x82\xdb\x93\x02\x84|\xd3\xb0\xa3\x91\xa7\xf7Upz\x08u\x8aSy\xfb\x9fF\xf5\x83\xd8\x0e\xe9\xed\x12\xd1\xdf\xf07*D\x19\x9a1\xcf\xa1\xaf\xe3;\x1aLx\xc2`\xee\x98k\r\x99\xea\xc5\xac'
DATA_KEY_DEFAULT = (0x2345, 0x7f8d)
DATA_KEY_MODIFIER = (0xffd9, 0xfff1)


SAVEDATA_ENCODE_TABLE = b':\x11rn/z#\xf0k\\\xcaAW]\xb2\xa8\x06_\xc9\xd8\x17\x82\xbb\xd2\x88\x86\'G\xc7)[\x04\x8e\xae^3I\xdb\xa5{1\xb7\xb5\x84\xf6v\x81\xado\xe09\x87\xc0\xabhM\x05\x92w\xff\x996,\x07\nY\xfa\xbcT\xe1\x94=\x1fX\xa6\xaaS.\x89\xeb\x9c\x98\x1b\xd6\xc10\x00\xf4\xef}\xbf\xe8\x0c\xc4\xac\xf3\xeax\xbe\xaf\xb0\x08\xa1\x90`*\xd4b;\xa7\xd9\xed|\xf5\xec\xba\x9bJ\x0f<\x7f\xc6$U\x01C"\x8a\xa0pegP\x1d\x96B\xce \x03\x12\xe3N\x95&\xe4\xb8\xd7H\xd0\xc3\xb9\x80\x18\xd5\x024!\x8b\xdf\xe9ay\x0e\x93\xa3c\x1a\x9d\xb3\xcd\xe6\x14-\xdc\xa4\x9e(u\xa9f\x91\xbd\xd3jm\xfbZ\x8c\xe7d\x97\x19F\xfe2\xf2\x9f8\x9a\x10?l\xe2\xd1E\x15\xb4\xde@V\xe5>\xf9\xc85\x16i\xfc\x85\x8fQ\xa2\xc5\xee\xb6\x8dt\xcc\xb1O%\xfd~\x1c\t\x13K7\xcf\xdaL\xf7\xc2R+\xf1\x1e\xf8\x0b\x83\xcbD\rsq\xdd'
SAVEDATA_DECODE_TABLE = b'V|\x9a\x8a\x1f8\x10?e\xea@\xf8\\\xfc\xa2v\xc7\x01\x8b\xeb\xab\xcd\xd7\x14\x98\xbf\xa6R\xe9\x85\xf6H\x89\x9c~\x06z\xe6\x8f\x1a\xb0\x1di\xf4>\xacM\x04U(\xc2#\x9b\xd6=\xed\xc52\x00lwG\xd3\xc8\xd0\x0b\x87}\xfb\xcc\xc0\x1b\x93$u\xec\xf07\x8d\xe5\x84\xdc\xf3LD{\xd1\x0cIA\xba\x1e\t\r"\x11h\xa0k\xa5\xbd\x82\xb3\x836\xd8\xb7\x08\xc9\xb8\x030\x81\xfe\x02\xfd\xe2\xb1-:a\xa1\x05\'pY\xe8x\x97.\x15\xf9+\xda\x193\x18N\x7f\x9d\xbb\xe1 \xdbg\xb49\xa3F\x8e\x86\xbeQ<\xc6tP\xa7\xaf\xc4\x80f\xdd\xa4\xae&Jm\x0f\xb2K5^/!cd\xe4\x0e\xa8\xce*\xe0)\x91\x96s\x16C\xb5bZ4T\xf2\x95]\xdey\x1c\xd5\x12\n\xfa\xe3\xa9\x88\xee\x94\xcb\x17\xb6j\x99S\x92\x13n\xef%\xad\xff\xcf\x9e1E\xca\x8c\x90\xd2\xaa\xbc[\x9f`Oro\xdfX\x07\xf5\xc3_Wq,\xf1\xf7\xd4B\xb9\xd9\xe7\xc1;'
SAVEDATA_KEY_DEFAULT = (0xdfa3, 0x215f)
SAVEDATA_KEY_MODIFIER = (0xffef, 0xff8f)
SAVEDATA_HASH_SALT_NA = b'3Nc94Hq1zOLh8d62Sb69'
SAVEDATA_HASH_SALT_JP = b'S)R?Bf8xW3#5h9lGU8wR'
SAVEDATA_HASH_SALT_EU = SAVEDATA_HASH_SALT_NA


PSPSAVEDATA_KEY_NA = b'J\x1f\xf3Y\xae\xb6\xef\xf8\x1c\xa8\xcb#\xbc\xa5{\xb3'
PSPSAVEDATA_KEY_JP = b'\xcd\x1f Y\xaep\xefh\xdc\xa2E\x13\xb4Z\xdb\n'
PSPSAVEDATA_KEY_EU = PSPSAVEDATA_KEY_NA


QUEST_KEY_DEFAULT = (0xff9d, 0xffa9, 0xffc7, 0xfff1)
QUEST_KEY_MODIFIER = (0x1709, 0x3df3, 0x747b, 0xb381)
QUEST_HASH_SALT_NA =  b'Vd6gh8F30wA86Ex5'
QUEST_HASH_SALT_JP = b'37wyS2Jfc3x5w9oG'
QUEST_HASH_SALT_EU = QUEST_HASH_SALT_NA
