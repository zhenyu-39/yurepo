window.onload = function (){
    $("#deleteimage").click(function (event){
        event.preventDefault()
        let imageid = $(this).data("image-id")
         if (confirm("确定要删除吗")) {
            $.ajax({
                url: "/blog/delete/image/" +imageid,
                type: "POST",
                data: {
                    id: imageid,
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                },
                success: function (data) {
                    alert("删除成功");
                    window.location.href = "/taking";
                },
                error: function () {
                    alert("删除失败");
                }
            });
        }
    })
}