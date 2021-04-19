// 设置全局变量参数
var secretKey = "d7fb396d5fcb64966cb0182ead488ab3";
var accessKey = "7f9d6d6dc6619bd616bb0d8c9605689e";
var botId = 272807;
var code = 'rb000';

// 固定参数
var lastVolume = 0;

// 获取参数对象
function getParam(version, ak, method, args){
    return {
        'version': version,
        'access_key': ak,
        'method': method,
        'args': JSON.stringify(args),
        'nonce': new Date().getTime()
    }
}

// md5加密
function md5(param){
    let paramUrl = param.version + "|" + param.method + "|" + param.args + "|" + param.nonce + "|" + secretKey
    return Hash("md5", "hex", paramUrl);
}

// 获取请求URL
function getFinalUrl(param){
    let url = "https://www.fmz.com/api/v1?";
    return url + "access_key=" + accessKey + "&nonce=" + param.nonce + "&args=" + param.args + "&sign=" + param.sign + "&version=" + param.version + "&method=" + param.method;
}

// 获取API信息
function getAPIInfo(method, dateInfo){
    let param = getParam("1.0.0", accessKey, method, dateInfo);
    let md5Result = md5(param);
    param.sign = md5Result;
    let finalUrl = getFinalUrl(param);
    let info = HttpQuery(finalUrl);
    return JSON.parse(info);
}

// 用arguments关键字获取参数数组
function getArgs(){
    return [].slice.call(arguments);
}

// 根据合约成交量判断是否开市
function isTrading() {
    let records = _C(exchange.GetRecords);
    let newVolume = records[records.length - 1].Volume;
    if (newVolume == lastVolume) {
        return;
    } else if (lastVolume == 0) {
        lastVolume = newVolume;
        return;
    }
    lastVolume = newVolume;
    return true;
}

// 策略入口函数
function main() {
    SetErrorFilter('not login');
    while (true) {
        if (!exchange.IO("status")) {
            Sleep(10000);
            continue;
        }
        if (exchange.SetContractType(code)) break;
    }
    while (true) {
        let info = getAPIInfo('GetRobotDetail', getArgs(botId));
        if (isTrading()) {
            if (info.data.result.robot.status == 4) {
                getAPIInfo('RestartRobot', getArgs(botId));
                Log('启动策略')
            }
        } else {
            if (info.data.result.robot.status == 1) {
                getAPIInfo('StopRobot', getArgs(botId));
                Log('停止策略')
            }
        }
        Sleep(10000);
    }
}