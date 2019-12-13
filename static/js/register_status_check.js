// var data = {
//     "status":0
// };//这里的0代表正常状态，1代表成功注册 2代表用户名已经注册过 3表示用户名不符合规范 4代表密码不符合规范
  //6代码邮箱的格式不符合规范

// print("asdf");
function start_register(){
    var form= new FormData(document.getElementById("regist_form"));

    // for (var key of form.keys()) {
	// 	//console.log("key:"+typeof(key));
	// 	console.log(key);
	// }
	// for (var value of form.values()) {
	// 	//console.log("value:"+typeof(value));
	// 	    console.log(value);
	// }
    var values = {};
    for (var value of form) {
        // 	console.log("value:"+typeof(value));
       values[value[0]] = value[1];
       console.log(values);
    }
    //data = JSON({"data":1});
    console.log(values["userName"]);
    console.log(values["pwd"]);
    console.log(values["email"]);


    //$(document).ready(function() {
    //$(function() {
    console.log("=========");
    console.log("12312321");

        //print("asdfasdfdasf");
    $.ajax({
        type: 'POST',
        url: "/regist_check",
        data: form,
        dataType: 'json',
        processData:false,
        contentType:false,
        async: false,
        success: function (data) {
            console.log("123123123123");
            var status = data['status'];
            console.log(status);
            if (status === 0) {
                console.log("szdfadgsdfhg");
                alert("注册成功 快去登录吧！");
            } else if (status === 2) {
                alert("您的用户名已经注册过");
            } else if (status === 3) {
                alert("用户名不符合规范");
            } else if (status === 4) {
                alert("密码不符合规");
            } else if (status === 5) {
                alert("邮箱的格式不符合规范");
            } else {
                alert("错误代码！");
            }
        },
        error: function (xhr, type) {
            console.log("123123123123");
            //print("123132");
            alert(xhr);
        }

    });
    console.log("=========");
    //});
    // });
}



