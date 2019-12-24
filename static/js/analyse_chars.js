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
    var myChart1 = echarts.init(document.getElementById('Business_type'));

    //var socket_code =
    //console.log(test_val);
    var charts_paras =Server.charts_paras;
    console.log(charts_paras);

    var years_money_accumulate = charts_paras['years_money_accumulate'];
    var company_money_accumulate = charts_paras['company_money_accumulate'];
    var trade_type_accmuldate = charts_paras['trade_type_accmuldate'];
    var relation_accumulate = charts_paras['relation_accumulate'];
    console.log(trade_type_accmuldate);

    var type_bar_data = [];
    var series_data = [];
    for(let KEY in  trade_type_accmuldate)
    {
        console.log(trade_type_accmuldate[KEY]);
        type_bar_data.push(String(KEY));
        series_data.push({value: trade_type_accmuldate[KEY], name: String(KEY)});
    }

    //console.log(years_money_accumulate.toString());
    // for (var value of years_money_accumulate) {
    //     // 	console.log("value:"+typeof(value));
    //
    //    console.log(value);
    // }


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


    var myChart2 = echarts.init(document.getElementById('Land_analysis'));



    var option2_source = [['product', '该公司交易金额', '总金额']];
    var total = total_price.total_price;
    var count = 1;
    //var series_data = [];
    for(let KEY in  company_money_accumulate)
    {
        console.log(company_money_accumulate[KEY]);
        option2_source.push(["公司"+String(count),company_money_accumulate[KEY],total]);
        count += 1;

    }

    option2 = {
        legend: {
            x: 'right',
            y: 'top',
            textStyle: {
                color: '#4ADEFE',
            }
        },
        grid: {
            x: 1,
            y: 50,
            x2: 0,
            y2: 45
        },
        tooltip: {},
        dataset: {
            source: option2_source
        },
        xAxis: {
            type: 'category',
            axisLine: {
                show: false,
                lineStyle: {
                    color: "#4ADEFE",
                },
            },
            // data: ["岳阳市","益阳市","长沙市","株洲市","衡阳市","永州市","娄底市","郴州市","湘潭市"],
            axisTick: {
                alignWithLabel: true
            }
        },
        yAxis: {
            axisLine: {
                lineStyle: {
                    color: "#4ADEFE",
                }
            },
            splitLine: {
                lineStyle: {
                    color: '#4ADEFE'
                }
            }
        },
        series: [
          {
              type: 'bar',
              barMaxWidth: '10',
              itemStyle: {
                  normal: {
                      color: '#4ADEFE'
                  },
              },
          },
          {
              type: 'bar',
              barMaxWidth: '10',
              itemStyle: {
                  normal: {
                      color: '#F3DB5C',
                  },
              },
          }
        ]
    };
    myChart2.setOption(option2);

     var datalist = [

        {
            "name": "years_changes",
        }
    ];

     var Axis = [];
     var years_counts = [];
    for(let KEY in  years_money_accumulate)
    {
        console.log(years_money_accumulate[KEY]);
        years_counts.push(years_money_accumulate[KEY]);
        Axis.push(String(KEY));

    }
    console.log(datalist);




    var myChart3 = echarts.init(document.getElementById('Information_Delivery'));

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

                data:Axis,
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
                data:years_counts

            }]
    };
    myChart3.setOption(option3);

     var Axis_relation = [];
     var relation_counts = [];
    for(let KEY in  relation_accumulate)
    {
        console.log(relation_accumulate[KEY]);
        relation_counts.push(relation_accumulate[KEY]);
        Axis_relation.push(String(KEY));

    }

    var myChart4 = echarts.init(document.getElementById('map'));

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

                data:Axis_relation,
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
                data:relation_counts

            }]
    };
    myChart4.setOption(option4);

    // 随机数据
    // var data = [{ "name": "长沙", "value": 46 }, { "name": "株洲", "value": 81 }, { "name": "湘潭", "value": 94 }, { "name": "衡阳", "value": 40 }, { "name": "邵阳", "value": 67 }, { "name": "岳阳", "value": 38 }, { "name": "常德", "value": 50 }, { "name": "张家界", "value": 48 }, { "name": "益阳", "value": 77 }, { "name": "郴州", "value": 78 }, { "name": "永州", "value": 57 }, { "name": "怀化", "value": 83 }, { "name": "娄底", "value": 43 }, { "name": "湘西", "value": 75 }];
    // option4 = {
    //     title: {
    //         text: ''
    //     },
    //     tooltip: {
    //         enabled: false
    //     },
    //     chart: {
    //         backgroundColor: 'transparent',
    //     },
    //     legend: {
    //         enabled: true,
    //     },
    //     colorAxis: {
    //         minColor: '#0666D5',
    //         maxColor: '#062A6C'
    //     },
    //     series: [{
    //         data: data,
    //         borderColor: '#6099EC',
    //         borderWidth: 0.5,
    //         mapData: Highcharts.maps['cn/hunan'],
    //         name: '',
    //         joinBy: ['name'], // 根据 name 属性进行关联
    //         states: {
    //             enabled: true,
    //             hover: {
    //                 color: '#F3DB5C'
    //             }
    //         },
    //         dataLabels: {
    //             enabled: true,
    //             color: '#4ADEFE',
    //             format: '{point.name}'
    //         },
    //         cursor: 'pointer',
    //         events: {
    //             click: function (e) {
    //                 if (e.point.name == "长沙") {
    //                     $(".list_num1 span").text('6666');
    //                     $(".list_num2 span").text('903.22');
    //                     $(".list_num3 span").text('1356.77');
    //
    //                     $(".circle_num1").text('1800.35');
    //                     $(".circle_num2").text('892.95');
    //                     $(".circle_num3").text('2016.15');
    //
    //                     option1.series[0].data = [
    //                         { value: 100, name: '土地经营权' },
    //                         { value: 240, name: '土地流转权' },
    //                         { value: 130, name: '房屋所有权' },
    //                         { value: 200, name: '集体建设用地' },
    //                         { value: 400, name: '林权' }
    //                     ]
    //                     myChart1.setOption(option1);
    //
    //                     data[0].color = "#F3DB5C";
    //                     new Highcharts.Map('map', option4);
    //                     numInit();
    //                 }
    //             }
    //         }
    //     }]
    // };
    // // 初始化图表
    // var map = new Highcharts.Map('map', option4);