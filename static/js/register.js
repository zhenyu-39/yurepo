$(function () {
    function bindCaptchaBtnClick() {
        $('#captcha-btn').click(function (event) {
            let $this = $(this);
            let email = $("input[name='email']").val();

            // 修复邮箱格式验证的正则表达式（将小写a-zA-Z改为正确的大小写兼容写法）
            function validateEmail(email) {
                const pattern = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
                return pattern.test(email);
            }

            if (!email) {
                alert('请先输入邮箱！');
                return;
            }
            if (!validateEmail(email)) {
                alert('请输入有效的邮箱地址！');
                return;
            }

            // 取消按钮的点击事件
            $this.off('click');

            // 发送ajax请求
            $.ajax('/auth/captcha?email='+email,{
                method:'GET',
                success: function (result){
                    if(result['code'] === 200){
                        alert("验证码发送成功")
                    }else{
                        alert(result['message']);
                    }
                },
                fail:function (error){
                    console.log(error);
                }
            })

            // 倒计时
            let countdown = 60;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text('获取验证码');
                    // 清掉定时器
                    clearInterval(timer);
                    // 重新绑定点击事件
                    bindCaptchaBtnClick();
                } else {
                    countdown--;
                    $this.text(countdown + "s")
                }
            }, 1000)
        })
    }
    bindCaptchaBtnClick();
});