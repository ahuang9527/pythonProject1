location={}
location.host='cn.bing.com'
navigator={
    'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

// 异常捕获
function ps(){
    // try{
        verify_local()
        if(navigator['userAgent']){
            return 'hello world'
        }
    // }
    // catch(e){
    //     console.log('报错的内容',e)
    //     return 'hello rld'
    // }
}

function verify_local(){
    if(location.host.length>2) {
        return 'xxx'
    }
}
window=global
delete global
sss='undefined'==typeof exports ? global: window
console.log(sss)

console.log(ps())