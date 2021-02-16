import requests

cookies = {
    'waptgshowtime': '2020711',
    'cowCookie': 'true',
    'HAList': 'a-sh-600095-^%^u54C8^%^u9AD8^%^u79D1^%^2Ca-sz-300558-^%^u8D1D^%^u8FBE^%^u836F^%^u4E1A^%^2Ca-sh-688027-^%^u56FD^%^u76FE^%^u91CF^%^u5B50^%^2Ca-sz-300842-^%^u5E1D^%^u79D1^%^u80A1^%^u4EFD^%^2Ca-sh-601888-^%^u4E2D^%^u56FD^%^u4E2D^%^u514D',
    'intellpositionL': '1522.39px',
    'qgqp_b_id': '2d65d06926b2b69e0c9fba6e0f32e4fc',
    'st_si': '57043238336711',
    'st_asi': 'delete',
    'intellpositionT': '855px',
    'st_pvi': '79671723949347',
    'st_sp': '2020-07-11^%^2015^%^3A00^%^3A00',
    'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.eastmoney.com^%^2F',
    'st_sn': '8',
    'st_psi': '20200711172828722-113300300813-4820091380',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '1^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
    ('rt', '53148657^'),
    ('cb', 'jQuery18307969277731974338_1594458875374^'),
    ('_', '1594459733361'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://push2.eastmoney.com/api/qt/clist/get?pn=1^&pz=50^&po=1^&np=1^&ut=b2884a393a59ad64002292a3e90d46a5^&fltt=2^&invt=2^&fid0=f4001^&fid=f62^&fs=m:0+t:6+f:^!2,m:0+t:13+f:^!2,m:0+t:80+f:^!2,m:1+t:2+f:^!2,m:1+t:23+f:^!2,m:0+t:7+f:^!2,m:1+t:3+f:^!2^&stat=1^&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^&rt=53148657^&cb=jQuery18307969277731974338_1594458875374^&_=1594459733361', headers=headers, cookies=cookies, verify=False)

a = response.text
print(a)