document.addEventListener('DOMContentLoaded',function () {
    $("#delete").click(function (event) {
        event.preventDefault(); // 阻止表单默认提交
        let blogid = $(this).data("blog-id");
        if (confirm("确定要删除吗")) {
            $.ajax({
                url: "/blog/delete/" +blogid,
                type: "POST",
                data: {
                    id: blogid,
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                },
                success: function (data) {
                    alert("删除成功");
                    window.location.href = "/";
                },
                error: function () {
                    alert("删除失败");
                }
            });
        }
    })
});
