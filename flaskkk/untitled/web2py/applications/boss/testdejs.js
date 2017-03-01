/**
 * Created by feng.qian on 2016/4/26.
 */
$(document).ready(function () {
    $("button").click(function () {
        $("#1").text('111111111111');
        $("#2").text('222222222222')
    });

    $("#id11").click(function () {

        $("p").toggle(500);
    });
    
    $(".qqq").click(function () {
        $ (this).hide(500);
    });

    $("#buttondianji").click(function () {
        $("*.h2test").hide(500);
    });
    $(".cc").click(function () {
        $(this).toggle(500)
    });
     $(".cc2").click(function () {
        $(this).toggle(500)
    });
      $(".cc3").click(function () {
        $(this).toggle(500)
    });
    $("#buttonshow3fangkuai").click(function () {
       $(".cc,.cc2,.cc3").show(300)
    }) ;

    $("#kongge").click(function () {
        $(this).load("text.txt",function(responseTxt,statusTxt,xhr) {
            if (statusTxt=="scuuess")
                alert("okok");
            if(statusTxt=="error")
                alert("error"+xhr.status+xhr.statusText);
        });
    });

//
       var chart = {
      type: 'pie',
      options3d: {
         enabled: true,
         alpha: 45,
         beta: 0
      }
   };
   var title = {
      text: '群内各位老总以及小阿弟的工资能力'
   };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };

   var plotOptions = {
      pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          depth: 35,
          dataLabels: {
             enabled: true,
             format: '{point.name}'
          }
      }
   };
   var series= [{
         type: 'pie',
            name: '工资比例',
            data: [
                ['杨总',   14000],
                ['张总',       12000],
                {
                    name: '小钱',
                    y: 9000,
                    sliced: true,
                    selected: true
                },
                ['丹哥',    8000],
                ['小伙子',     2000]
            ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.plotOptions = plotOptions;
   json.series = series;
   $('#container').highcharts(json);
    //


    

});