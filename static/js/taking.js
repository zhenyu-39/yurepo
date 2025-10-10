window.onload = function (){
  $("#submit-btn-1").click(function (event){
  //   阻止按钮的默认行为
    event.preventDefault();

    let content = $("textarea[name='content']").val();
    if(!content || content.trim().length === 0){
      alert('内容不能为空');
      return;
    }
    let csrfmiddlewaretoken=$("input[name='csrfmiddlewaretoken']").val()
    $.ajax({
      url:'blog/taking',
      method:'POST',
      data:{content, csrfmiddlewaretoken},
      success:function (result){
        if(result && result['code']===200){
          // 刷新当前页以显示新留言
          window.location.reload()
        }else{
          // 未登录或返回非JSON
          let msg = '请先登录';
          if(result && typeof result === 'object' && result['message']){
            msg = result['message'];
          }
          alert(msg);
        }
      },
      error:function (){
        // 被登录拦截或其它错误
        alert('请先登录');
      }
    })
  })
}