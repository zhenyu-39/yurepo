document.addEventListener('DOMContentLoaded',function ()  {
    $("#deletecomment").click(function (event) {
        event.preventDefault(); // 阻止表单默认提交
        let commentId = $(this).data("comment-id");
        let blogid = $(this).data("blog-id");
        if (confirm("确定要删除吗")) {
            $.ajax({
                url: "/blog/delete/comment/" +commentId,
                type: "POST",
                data: {
                    id: commentId,blogid,
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                },
                success: function (data) {
                    alert("删除成功");
                    window.location.href = "/blog/detail/" +blogid;
                },
                error: function () {
                    alert("删除失败");
                }
            });
        }
    })
});