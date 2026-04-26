var target={
    name:"lzz",
    age:22,
    lili:{
        zs:"lll"
    }
};

function XlProxy(obj,name){
    return new Proxy(obj,{
        get(target,p,receiver){
            temp=Reflect.get(target,p,receiver)
            console.log(`对象${target}-->get了属性-->${p}值是-->${temp}`);
            if(typeof temp=='object'){
                // 对于对象套对象进行挂代理
                temp=XlProxy(temp,name+'-->'+p)
            }
            return temp
        }
    })
}

sss=XlProxy(target,'target')
sss.name
sss.lili.zs