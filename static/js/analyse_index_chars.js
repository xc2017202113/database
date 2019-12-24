 function OSnow() {
        var agent = navigator.userAgent.toLowerCase();
        var isMac = /macintosh|mac os x/i.test(navigator.userAgent);
        if (agent.indexOf("win32") >= 0 || agent.indexOf("wow32") >= 0) {
            $(".main").css("height", "880px");
        }
        if (agent.indexOf("win64") >= 0 || agent.indexOf("wow64") >= 0) {
            $(".main").css("height", "880px");
        }
        if (isMac) {

        }
    }
    OSnow();
    function numInit() {
        $('.counter-value').each(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 2500,
                easing: 'swing',
                step: function (now) {
                    $(this).text(now.toFixed(0));
                }
            });
        });
    }

    numInit();
    // 基于准备好的dom，初始化echarts实例
    var i = 0;


    //var socket_code =
    //console.log(test_val);
    var charts_paras =Server.charts_paras;


    var years_CR_5_index_accumulate = charts_paras['years_CR_5_index_accumulate'];
    var years_CR_10_index_accumulate = charts_paras['years_CR_10_index_accumulate'];
    var years_Z_index_accumulate = charts_paras['years_Z_index_accumulate'];
    var years_Herfindahl_5_index_accumulate = charts_paras['years_Herfindahl_5_index_accumulate'];


    var Axis_CR_5_index = [];
     var years_CR_5_index = [];
    for(let KEY in  years_CR_5_index_accumulate)
    {

        years_CR_5_index.push(years_CR_5_index_accumulate[KEY]);
        Axis_CR_5_index.push(String(KEY));

    }


    var myChart1 = echarts.init(document.getElementById('CR_5_index'));

    option1 = {
        legend: {
            x: 'right',
            y: 'top',
            data:['years_changes'],
            textStyle: {
                color: '#EEEE00',
            }
        },
        xAxis:{

                data:Axis_CR_5_index,
        axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },


            },
        yAxis:{
            axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#EEEE00'
                }
            }
        },
        series:[{
                name:'apple',
                type:'line',
                itemStyle:{
                    normal:{ color: "#8DEEEE" }
                    },
                lineStyle:{
                    normal:{
                        width:2,
                        color: "#8DEEEE"  }//线条的颜色及宽度
                    },
                label: {//线条上的数字提示信息
                    normal: {
                        show: true,
                        position: 'top'
                    }

                    },
                smooth: true,//线条平滑                    //data为每年apple的数量
                data:years_CR_5_index

            }]
    };
    myChart1.setOption(option1);



     var Axis_CR_10_index = [];
     var years_CR_10_index = [];
    for(let KEY in  years_CR_10_index_accumulate)
    {

        years_CR_10_index.push(years_CR_10_index_accumulate[KEY]);
        Axis_CR_10_index.push(String(KEY));

    }


      var myChart2 = echarts.init(document.getElementById('CR_10_index'));

    option2 = {
        legend: {
            x: 'right',
            y: 'top',
            data:['years_changes'],
            textStyle: {
                color: '#EEEE00',
            }
        },
        xAxis:{

                data:Axis_CR_10_index,
        axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },


            },
        yAxis:{
            axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#EEEE00'
                }
            }
        },
        series:[{
                name:'apple',
                type:'line',
                itemStyle:{
                    normal:{ color: "#8DEEEE" }
                    },
                lineStyle:{
                    normal:{
                        width:2,
                        color: "#8DEEEE"  }//线条的颜色及宽度
                    },
                label: {//线条上的数字提示信息
                    normal: {
                        show: true,
                        position: 'top'
                    }

                    },
                smooth: true,//线条平滑                    //data为每年apple的数量
                data:years_CR_10_index

            }]
    };
    myChart2.setOption(option2);

     var Axis_Herfindahl_5_index = [];
     var years_Herfindahl_5_index = [];
    for(let KEY in  years_Herfindahl_5_index_accumulate)
    {

        years_Herfindahl_5_index.push(years_Herfindahl_5_index_accumulate[KEY]);
        Axis_Herfindahl_5_index.push(String(KEY));

    }


    var myChart3 = echarts.init(document.getElementById('Herfindahl_5_index'));

    option3 = {
        legend: {
            x: 'right',
            y: 'top',
            data:['years_changes'],
            textStyle: {
                color: '#EEEE00',
            }
        },
        xAxis:{

                data:Axis_Herfindahl_5_index,
        axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },


            },
        yAxis:{
            axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#EEEE00'
                }
            }
        },
        series:[{
                name:'apple',
                type:'line',
                itemStyle:{
                    normal:{ color: "#8DEEEE" }
                    },
                lineStyle:{
                    normal:{
                        width:2,
                        color: "#8DEEEE"  }//线条的颜色及宽度
                    },
                label: {//线条上的数字提示信息
                    normal: {
                        show: true,
                        position: 'top'
                    }

                    },
                smooth: true,//线条平滑                    //data为每年apple的数量
                data:years_Herfindahl_5_index

            }]
    };
    myChart3.setOption(option3);

    var myChart4 = echarts.init(document.getElementById('z_index'));

     var Axis_z_index = [];
     var years_z_index = [];
    for(let KEY in  years_Z_index_accumulate)
    {

        years_z_index.push(years_Z_index_accumulate[KEY]);
        Axis_z_index.push(String(KEY));

    }
    option4 = {
        legend: {
            x: 'right',
            y: 'top',
            data:['years_changes'],
            textStyle: {
                color: '#EEEE00',
            }
        },
        xAxis:{

                data:Axis_z_index,
        axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },


            },
        yAxis:{
            axisLine: {
                lineStyle: {
                    color: "#EEEE00",
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#EEEE00'
                }
            }
        },
        series:[{
                name:'apple',
                type:'line',
                itemStyle:{
                    normal:{ color: "#8DEEEE" }
                    },
                lineStyle:{
                    normal:{
                        width:2,
                        color: "#8DEEEE"  }//线条的颜色及宽度
                    },
                label: {//线条上的数字提示信息
                    normal: {
                        show: true,
                        position: 'top'
                    }

                    },
                smooth: true,//线条平滑                    //data为每年apple的数量
                data:years_z_index

            }]
    };
    myChart4.setOption(option4);

