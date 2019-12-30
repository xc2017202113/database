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

    var noflow_scale_change = Server.charts_paras['noflow_scale_change'];
    console.log(noflow_scale_change);
    console.log("=============");
    var Axis_relation_noflow = [];
    var relation_counts_noflow = [];
    for(let KEY in  noflow_scale_change)
    {

        relation_counts_noflow.push(noflow_scale_change[KEY]);
        Axis_relation_noflow.push(String(KEY));

    }

    var myChart1 = echarts.init(document.getElementById('noflow_scale_change'));

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

                data:Axis_relation_noflow,
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
                data:relation_counts_noflow

            }]
    };
    myChart1.setOption(option1);

    var flow_scale_change = Server.charts_paras['flow_scale_change'];
    var Axis_relation_flow = [];
    var relation_counts_flow = [];
    for(let KEY in  flow_scale_change)
    {

        relation_counts_flow.push(flow_scale_change[KEY]);
        Axis_relation_flow.push(String(KEY));

    }

    var myChart2 = echarts.init(document.getElementById('flow_scale_change'));

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

                data:Axis_relation_flow,
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
                data:relation_counts_flow

            }]
    };
    myChart2.setOption(option2);

    var flow_change = Server.charts_paras['flow_change'];
    var option2_source = [['product', '流动持股数量']];
    for(let KEY in  flow_change)
    {

       option2_source.push([String(KEY),flow_change[KEY]]);

    }

    var myChart3 = echarts.init(document.getElementById('flow_change'));

    option3 = {
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
    myChart3.setOption(option3);

    var noflow_change = Server.charts_paras['noflow_change'];
    var option_source = [['product', '持股数量']];
    for(let KEY in  noflow_change)
    {

       option_source.push([String(KEY),noflow_change[KEY]]);

    }

    var myChart4 = echarts.init(document.getElementById('noflow_change'));

    option4 = {
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
            source: option_source
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
    myChart4.setOption(option4);
