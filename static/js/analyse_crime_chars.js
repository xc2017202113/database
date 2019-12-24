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
    var myChart1 = echarts.init(document.getElementById('crime_position'));

    //var socket_code =
    //console.log(test_val);
    var charts_paras =Server.charts_paras;
    console.log(charts_paras);

    var years_crime_position = charts_paras['years_crime_position']; //饼图 案件地位的变化
    var years_crime_change = charts_paras['years_crime_change']; //折线图 年度涉案情况变化
    var year_money_change = charts_paras['year_money_change'];
    var crime_type = charts_paras['crime_type'];


    var type_bar_data = [];
    var series_data = [];
    for(let KEY in  years_crime_position)
    {

        type_bar_data.push(String(KEY));
        series_data.push({value: years_crime_position[KEY], name: String(KEY)});
    }



    // 指定图表的配置项和数据
    option1 = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            x: 'center',
            y: 'bottom',
            data: type_bar_data,
            textStyle: {
                color: '#4ADEFE',
            }
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: ['30%', '55%'],
                center: ['45%', '35%'],
                avoidLabelOverlap: false,
                data: series_data,
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ],
        color: ['#F3DB5D', '#009AFF', '#F77474', '#28DCCF', '#FF5937']
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart1.setOption(option1);


    var myChart2 = echarts.init(document.getElementById('year_crime_change'));




     var Axis_relation_chart2 = [];
     var relation_counts_chart2 = [];
    for(let KEY in  years_crime_change)
    {

        relation_counts_chart2.push(years_crime_change[KEY]);
        Axis_relation_chart2.push(String(KEY));

    }



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

                data:Axis_relation_chart2,
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
                data:relation_counts_chart2

            }]
    };

    myChart2.setOption(option2);

     var myChart3 = echarts.init(document.getElementById('year_money_change'));




     var Axis_relation_chart3 = [];
     var relation_counts_chart3 = [];
    for(let KEY in  year_money_change)
    {

        relation_counts_chart3.push(year_money_change[KEY]);
        Axis_relation_chart3.push(String(KEY));

    }



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

                data:Axis_relation_chart3,
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
                data:relation_counts_chart3

            }]
    };

    myChart3.setOption(option3);


     var type_bar_data_4 = [];
    var series_data_4 = [];
    for(let KEY in  crime_type)
    {

        type_bar_data_4.push(String(KEY));
        series_data_4.push({value: crime_type[KEY], name: String(KEY)});
    }


    var myChart4 = echarts.init(document.getElementById('crime_type'));
    // 指定图表的配置项和数据
    option4 = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            x: 'center',
            y: 'bottom',
            data: type_bar_data_4,
            textStyle: {
                color: '#4ADEFE',
            }
        },
        series: [
            {
                name: '访问来源',
                type: 'pie',
                radius: ['30%', '55%'],
                center: ['45%', '35%'],
                avoidLabelOverlap: false,
                data: series_data_4,
                itemStyle: {
                    emphasis: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ],
        color: ['#F3DB5D', '#009AFF', '#F77474', '#28DCCF', '#FF5937']
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart4.setOption(option4);

