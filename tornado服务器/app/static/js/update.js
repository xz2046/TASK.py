let x = option_china_map.legend[0].selected;
chart_china_map.on('legendselscted', function(params){
    //监听legned点击状态
    x = params.selected
})

//轮询版
/*setInterval(function(){
    $.ajax({url:'/update', 
        success:function(data){
            option_china_map.series[0].data = JSON.parse(data)[0];
            option_china_map.series[1].data = JSON.parse(data)[1];
            option_china_map.series[2].data = JSON.parse(data)[2];
            option_china_map.legend[0] = x;
            chart_china_map.setOption(option_china_map);
            console.log('成功');
        },
        complete:function(){
                //console.log('完成');
        },
        error:function(){
            //console.log('失败');
        }
    })},
    30000   
)*/

//创建一个websocket对象向update发送请求
//ws = new WebSocket('ws://192.168.1.249:8800/update');
ws = new WebSocket('ws://192.168.43.14:8800/update');
//ws = new WebSocket('ws://127.0.0.1:8800/update');

ws.onopen = function(){
    console.log('连接成功');
    ws.send('请求来了！！！')
}
ws.onmessage = function(event){
    console.log('接收到数据 更新数据。');
    console.log(event);
    option_china_map.series[0].data = JSON.parse(event.data)[0];
    option_china_map.series[1].data = JSON.parse(event.data)[1];
    option_china_map.series[2].data = JSON.parse(event.data)[2];
    option_china_map.legend[0] = x;
    chart_china_map.setOption(option_china_map);
    console.log('成功');
}